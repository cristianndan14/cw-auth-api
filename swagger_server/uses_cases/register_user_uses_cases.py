from swagger_server.models.response_register_user_by_admin import ResponseRegisterUserByAdmin
from swagger_server.repository.register_user_repository import RegisterUserRepository
from swagger_server.models.request_register_user_by_admin import RequestRegisterUserByAdmin
from swagger_server.utils.logs.logging import log as Logging


class RegisterUserUseCase:

    def __init__(self, register_user_repository: RegisterUserRepository, log: Logging):
        self.log = log
        self.register_user_repository = register_user_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def new_user(self, body: RequestRegisterUserByAdmin, internal_transaction_id: str):
        try:
            user = body.data.to_dict()
            data = self.register_user_repository.register_user(user, internal_transaction_id, body.external_transaction_id)
            
            response = ResponseRegisterUserByAdmin(
                code="200",
                message="Usuario registrado con éxito.",
                data=data,
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response
        except Exception as ex:
            response = ResponseRegisterUserByAdmin(
                code=-1,
                message=str(ex),
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response, 400