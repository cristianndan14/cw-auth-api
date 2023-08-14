import connexion

from swagger_server.models.request_signin import RequestSignin  # noqa: E501
from swagger_server.models.response_signin import ResponseSignin  # noqa: E501
from swagger_server.models.db.user_model import User

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.utils.encrypt import encrypt_password


class SigninView(MethodView):

    def __init__(self):
        self.log = logging()
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'


    def signin(self):  # noqa: E501
        """Inicio de sesion de usuarios

        Inicio de sesion de usuarios # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseSignin
        """
        start_time = default_timer()
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "signin"
        package_name = __name__
        log = self.log

        if connexion.request.is_json:

            body = RequestSignin.from_dict(connexion.request.get_json())  # noqa: E501

            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)
            
            try:
                request = body.data.to_dict()

                code_email = request.get('code_email')
                password = encrypt_password(request.get('password'))
                
                user = User.query.filter_by(code_email=code_email).first()
                
                if user.password == password:
                    response = ResponseSignin(
                        code="200",
                        message="Inicio de sesión exitoso.",
                        data=user.to_json(),
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )
                else:
                    response = ResponseSignin(
                    code="400",
                    message="Contraseña incorrecta.",
                    data= [],
                    internal_transaction_id=internal_transaction_id,
                    external_transaction_id=external_transaction_id
                    )
                    return response, 400
                
            except Exception as ex:
                message = str(ex)
                log = logging()
                log.critical(
                    self.msg_log,
                    internal_transaction_id, external_transaction_id, function_name, package_name, message)

                response = ResponseSignin(
                    code=-1,
                    message=message,
                    data= [],
                    internal_transaction_id=internal_transaction_id,
                    external_transaction_id=external_transaction_id
                )
            
            finally:
                end_time = default_timer()
                message = f"end request: {function_name} - Procesada en : {round((end_time - start_time) * 1000)} milisegundos "
                log = logging()
                log.info(
                    self.msg_log,
                    internal_transaction_id, external_transaction_id, function_name, package_name, message)
                
        return response
