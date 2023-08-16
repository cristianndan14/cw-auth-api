from swagger_server.models.response_reset_password import ResponseResetPassword
from swagger_server.repository.reset_password_repository import ResetPasswordRepository
from swagger_server.models.request_reset_password import RequestResetPassword
from swagger_server.utils.logs.logging import log as Logging


class ResetPasswordUseCase:

    def __init__(self, reset_password_repository: ResetPasswordRepository, log: Logging):
        self.log = log
        self.reset_password_repository = reset_password_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def reset_password(self, body: RequestResetPassword, internal_transaction_id: str):
        try:
            request = body.data.to_dict()

            user = self.reset_password_repository.get_user(request.get('code_email'), internal_transaction_id, body.external_transaction_id)

            if user is None:
                response = ResponseResetPassword(
                    code=-1,
                    message="El usuario ingresado no existe.",
                    data=[],
                    internal_transaction_id=internal_transaction_id,
                    external_transaction_id=body.external_transaction_id
                )
                return response, 404
            
            if user.token_reset_password != request.get('token'):
                response = ResponseResetPassword(
                    code=-1,
                    message="El token ingresado es inválido.",
                    data=[],
                    internal_transaction_id=internal_transaction_id,
                    external_transaction_id=body.external_transaction_id
                )
                return response, 400
            
            change_password = self.reset_password_repository.change_password(user, request.get('password'), internal_transaction_id, body.external_transaction_id)

            response = ResponseResetPassword(
                code="200",
                message="Contraseña reestablecida exitosamente",
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response
            
        except Exception as ex:
            response = ResponseResetPassword(
                code=-1,
                message=str(ex),
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response, 500