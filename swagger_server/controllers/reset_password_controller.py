import connexion

from swagger_server.models.request_reset_password import RequestResetPassword  # noqa: E501
from swagger_server.models.response_reset_password import ResponseResetPassword  # noqa: E501
from swagger_server.models.response_reset_password_data import ResponseResetPasswordData
from swagger_server.models.db.user_model import User

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.utils.encrypt import encrypt_password


class ResetPasswordView(MethodView):

    def __init__(self):
        self.log = logging()
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'


    def reset_password(self):  # noqa: E501
        """Resetear password

        Resetear password # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseResetPassword
        """
        start_time = default_timer()
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "reset_password"
        package_name = __name__
        log = self.log

        if connexion.request.is_json:

            body = RequestResetPassword.from_dict(connexion.request.get_json())  # noqa: E501
        
            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)
            
            try:
                request = body.data.to_dict()
                
                code_email = request.get('code_email')
                password = encrypt_password(request.get('password'))
                token_reset_password = request.get('token')

                user = User.query.filter_by(code_email=code_email).first()

                if user and user.token_reset_password == token_reset_password:
        
                    user.password = password
                    user.save()

                    data = ResponseResetPasswordData(code_email=code_email)

                    response = ResponseResetPassword(
                        code="200",
                        message="Contraseña reestablecida exitosamente",
                        data=data,
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )

                else:
                    response = ResponseResetPassword(
                        code=-1,
                        message=f"El code_email ingresado {code_email}, no pertenece a ningun usuario registrado." if not code_email else "El token ingresado es inválido",
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

                response = ResponseResetPassword(
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
