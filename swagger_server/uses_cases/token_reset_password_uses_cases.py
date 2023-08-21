import secrets

from swagger_server.models.response_token_reset_password import ResponseTokenResetPassword
from swagger_server.repository.token_reset_password_repository import TokenResetPasswordRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_token_reset_password import RequestTokenResetPassword
from swagger_server.services.token_reset_password_service import TokenResetPasswordService


class TokenResetPasswordUseCase:

    def __init__(self, user_repository: TokenResetPasswordRepository, log: Logging):
        self.log = log
        self.user_repository = user_repository
        self.token_reset_password_service = TokenResetPasswordService()
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
    
    def recovery_password(self, body: RequestTokenResetPassword, internal_transaction_id: str):
        try:
            user = self.user_repository.get_user(body.code_email, internal_transaction_id, body.external_transaction_id)
            
            if user is None:
                response = ResponseTokenResetPassword(
                    code=1,
                    message="El usuario ingresado no existe",
                    data=[],
                    internal_transaction_id=internal_transaction_id,
                    external_transaction_id=body.external_transaction_id
                )
                return response, 404

            if user.token_reset_password is None:
                token_reset_password = secrets.token_hex(8)
                save_token = self.user_repository.create_token(user, token_reset_password, internal_transaction_id, body.external_transaction_id)
            
            response_token_xtrim = self.token_reset_password_service.get_token_xtrim(internal_transaction_id, body.external_transaction_id)
            #print(response_token_xtrim)
            if response_token_xtrim.get("code") != 0:
                response = ResponseTokenResetPassword(
                    code=response_token_xtrim.get("code"),
                    message=response_token_xtrim.get("message"),
                    data=[],
                    internal_transaction_id=response_token_xtrim.get("internal_transaction_id"),
                    external_transaction_id=response_token_xtrim.get("external_transaction_id")
                )
                return response, 400
            
            token_xtrim = response_token_xtrim["data"]["token"]
            #print(token_xtrim)
            send_recovery_token = self.token_reset_password_service.send_email_recovery_token(token_xtrim, user.token_reset_password, user.email, internal_transaction_id, body.external_transaction_id)
            #print(send_recovery_token)
            if send_recovery_token.get("code") != "0":
                response = ResponseTokenResetPassword(
                    code=send_recovery_token.get("code"),
                    message=send_recovery_token.get("message"),
                    data=[],
                    internal_transaction_id=send_recovery_token.get("internal_transaction_id"),
                    external_transaction_id=send_recovery_token.get("external_transaction_id")
                )
                return response, 400
            
            response = ResponseTokenResetPassword(
                code=0,
                message=send_recovery_token.get('message'),
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )

            return response
        except Exception as ex:
            response = ResponseTokenResetPassword(
                code=1,
                message=str(ex),
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response, 500