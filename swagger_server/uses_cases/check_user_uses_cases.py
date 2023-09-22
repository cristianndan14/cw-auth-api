from swagger_server.models.response_check_user import ResponseCheckUser
from swagger_server.repository.check_user_repository import CheckUserRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_check_user import RequestCheckUser
from swagger_server.services.check_user_service import CheckUserService


class CheckUserUseCase:

    def __init__(self, user_repository: CheckUserRepository, log: Logging):
        self.log = log
        self.user_repository = user_repository
        self.check_user_service = CheckUserService()
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def check_user(self, body: RequestCheckUser, internal_transaction_id: str):

        user_db = self.user_repository.get_user(body.code_email, internal_transaction_id, body.external_transaction_id)

        if user_db is None:
            user_cedula_ventas = self.check_user_service.check_vendor(body.code_email, internal_transaction_id, body.external_transaction_id)
            
            if user_cedula_ventas["code"] == 200:
                if user_cedula_ventas["data"]["status"] != "ACTIVO":
                    response = ResponseCheckUser(
                        code=1,
                        message="Usuario Inactivo.",
                        data={"code_email": body.code_email, "status": "Inactivo"},
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=body.external_transaction_id
                    )
                    return response, 403
                else:
                    return user_cedula_ventas, 201
            else:
                response = ResponseCheckUser(
                    code="404",
                    message="El usuario ingresado no existe.",
                    data=[],
                    internal_transaction_id=internal_transaction_id,
                    external_transaction_id=body.external_transaction_id
                )
                return response, 404

        if user_db.status is not True:
            response = ResponseCheckUser(
                code=1,
                message="Usuario Inactivo.",
                data={"code_email": user_db.code_email, "status": "Inactivo"},
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response, 403
        
        if user_db:
            response = ResponseCheckUser(
                code="200",
                message="Datos obtenidos exitosamente.",
                data=user_db.to_json(),
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response