from swagger_server.models.response_update_user import ResponseUpdateUser
from swagger_server.repository.update_user_repository import UpdateUserRepository
from swagger_server.models.request_update_user import RequestUpdateUser
from swagger_server.utils.logs.logging import log as Logging


class UpdateUserUseCase:

    def __init__(self, update_user_repository: UpdateUserRepository, log: Logging):
        self.log = log
        self.update_user_repository = update_user_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def save_changes(self, code_email: str, body: RequestUpdateUser, internal_transaction_id: str):
        try:
            user = self.update_user_repository.get_user(code_email, internal_transaction_id, body.external_transaction_id)
            
            if user is None:
                response = ResponseUpdateUser(
                    code="404",
                    message="Usuario inexistente",
                    data=[],
                    internal_transaction_id=internal_transaction_id,
                    external_transaction_id=body.external_transaction_id
                )
                return response, 404
            
            data = body.data.to_dict()

            user_updated = self.update_user_repository.update_user(user, data, internal_transaction_id, body.external_transaction_id)

            response = ResponseUpdateUser(
                code="200",
                message="Usuario actualizado",
                data=user_updated,
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response
        
        except Exception as ex:
            response = ResponseUpdateUser(
                code=-1,
                message=str(ex),
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response, 400