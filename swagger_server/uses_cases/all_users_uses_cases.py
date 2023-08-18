from swagger_server.models.response_all_users import ResponseAllUsers
from swagger_server.repository.all_users_repository import AllUsersRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_all_users import RequestAllUsers


class AllUsersUseCase:

    def __init__(self, user_repository: AllUsersRepository, log: Logging):
        self.log = log
        self.user_repository = user_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def get_all_users(self, body: RequestAllUsers, internal_transaction_id: str):
        
        users_data = self.user_repository.get_users(body.external_transaction_id, internal_transaction_id)

        if users_data:
            response = ResponseAllUsers(
                code="200",
                message="Datos obtenidos exitosamente.",
                data=users_data,
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response
        else:
            response = ResponseAllUsers(
                code="404",
                message="No hay usuarios registrados aun.",
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response, 404