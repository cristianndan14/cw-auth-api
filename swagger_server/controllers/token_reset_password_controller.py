import connexion
import requests
import secrets

from swagger_server.models.request_token_reset_password import RequestTokenResetPassword  # noqa: E501
from swagger_server.models.response_token_reset_password import ResponseTokenResetPassword  # noqa: E501
from swagger_server.models.db.user_model import User
from swagger_server.models.response_reset_password_data import ResponseResetPasswordData

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.utils.encrypt import encrypt_password

from swagger_server.config.access import access

class TokenResetPasswordView(MethodView):

    def __init__(self):
        self.log = logging()
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'


    def token_reset_password(self):  # noqa: E501
        """Generar token para resetear password

        Generar token para resetear password # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseTokenResetPassword
        """
        start_time = default_timer()
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "token_reset_password"
        package_name = __name__
        log = self.log

        if connexion.request.is_json:

            body = RequestTokenResetPassword.from_dict(connexion.request.get_json())  # noqa: E501

            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)

            try:
                code_email = body.code_email

                user = User.query.filter_by(code_email=code_email).first()

                if not user:
                    
                    response = ResponseTokenResetPassword(
                        code=-1,
                        message="No existe usuario con el code_email ingresado.",
                        data= [],
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )
                
                if user.token_reset_password is None:
                    token_password = secrets.token_hex(8)
                    user.token_reset_password = token_password
                    user.save()
                
                """ token_xtrim_api = access().get("SERVICES").get("TOKEN_XTRIM")
                token_xtrim_api_url = token_xtrim_api.get("URL")
                token_xtrim_api_request = token_xtrim_api.get("REQUEST")

                response_token_xtrim_api = requests.post(token_xtrim_api_url, json=token_xtrim_api_request).json()
                token_xtrim = response_token_xtrim_api.get("data", {}).get("token")
                print(token_xtrim)

                email_notificaciones_api = access().get("SERVICES").get("EMAIL_NOTIFICACIONES")
                email_notificaciones_api_url = email_notificaciones_api.get("URL")
                email_notificaciones_api_headers = email_notificaciones_api.get("HEADERS")
                email_notificaciones_api_request = email_notificaciones_api.get("REQUEST")

                email_notificaciones_api_headers.update({"Authorization": f"Bearer {token_xtrim}"})
                email_notificaciones_api_request.get("data").get("email").update({"to": user.email})
                email_notificaciones_api_request.get("data").get("template").get("variables").update(
                    [{"name": "fieldstr02", "value": user.token_reset_password},{"name": "fieldstr01", "value": "Token de recuperacion"}])

                response_email_notificaciones_api = requests.post(email_notificaciones_api_url, json=email_notificaciones_api_request, headers=email_notificaciones_api_headers)

                if response_email_notificaciones_api:

                    response = ResponseTokenResetPassword(
                        code="200",
                        message="El token de recuperacion de contraseña, fue enviado a su mail",
                        data= [],
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )

                    return response
                
                else: """
                    
                data = ResponseResetPasswordData(code_email=user.token_reset_password)

                response = ResponseTokenResetPassword(
                    code="200",
                    message="Token de recuperacion de contraseña generado con éxito",
                    data=data,
                    internal_transaction_id=internal_transaction_id,
                    external_transaction_id=external_transaction_id
                )

            except Exception as ex:

                message = str(ex)
                log = logging()
                log.critical(
                    self.msg_log,
                    internal_transaction_id, external_transaction_id, function_name, package_name, message)

                response = ResponseTokenResetPassword(
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

