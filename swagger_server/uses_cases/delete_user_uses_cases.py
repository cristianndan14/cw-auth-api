from swagger_server.models.response_delete_user import ResponseDeleteUser
from swagger_server.repository.delete_user_repository import DeleteUserRepository
from swagger_server.utils.logs.logging import log as logging


class DeleteUserUseCase:

    def __init__(self, user_repository: DeleteUserRepository, log: logging):
        self.log = log
        self.user_repository = user_repository
        self.msg_log = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def delete_user(self, code_email: str, internal_transaction_id: int):

        data = self.user_repository.delete_user(code_email, internal_transaction_id)

        if data:
            response = ResponseDeleteUser(
                code="200",
                message="Usuario eliminado de la base de datos.",
                data=data,
                internal_transaction_id=internal_transaction_id
            )
            return response
        else:
            response = ResponseDeleteUser(
                code="200",
                message="El usuario ingresado no existe.",
                data=[],
                internal_transaction_id=internal_transaction_id
            )
            return response, 404