import connexion
import re

from swagger_server.models.request_register_user_by_admin import RequestRegisterUserByAdmin  # noqa: E501
from swagger_server.models.response_register_user_by_admin import ResponseRegisterUserByAdmin  # noqa: E501
from swagger_server.models.register_user_by_admin_data import RegisterUserByAdminData
from swagger_server.models.db.user_model import User

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging


class RegisterUserView(MethodView):

    def __init__(self):
        self.log = logging()
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
    
    
    def register_user(self):  # noqa: E501
        """Registrar usuario

        Registrar usuario desde el administrador # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseRegisterUserByAdmin
        """
        start_time = default_timer()
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "register_user"
        package_name = __name__
        log = self.log

        if connexion.request.is_json:

            body = RequestRegisterUserByAdmin.from_dict(connexion.request.get_json())

            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)
        
            try:

                new_user = body.data.to_dict()
                code_email = new_user.get('code_email')
                password = new_user.get('password')
                
                user_exist = User.query.filter_by(code_email=code_email).first()

                if user_exist:
                    
                    response = ResponseRegisterUserByAdmin(
                        code="400",
                        message=f"Ya existe un usuario con el code_email {code_email}",
                        data= [],
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )

                    return response, 400

                patron = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#=_+-])[A-Za-z\d@$!%*?&#=_+-]{7,}$"
                
                if not re.match(patron, password):

                    response = ResponseRegisterUserByAdmin(
                        code="400",
                        message="La contraseña debe contener al menos 7 carateres compuestos por Mayúsculas, números y caracteres especiales",
                        data= [],
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )

                    return response, 400

                if code_email is not None:
                    print(f"new user: {new_user}")
                    user = User(new_user)
                    user.save()
                    print(f"user: {user}")
                    response = ResponseRegisterUserByAdmin(
                        code="200",
                        message="Usuario creado exitosamente",
                        data=[],
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )
                else:
                    response = ResponseRegisterUserByAdmin(
                        code="400",
                        message="Para crear un usuario, necesita registrar un code_email",
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
                
                response = ResponseRegisterUserByAdmin(
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
