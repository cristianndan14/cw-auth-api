from swagger_server.models.response_signup import ResponseSignup
from swagger_server.repository.signup_repository import SignupRepository
from swagger_server.models.request_signup import RequestSignup
from swagger_server.utils.logs.logging import log as Logging
from datetime import datetime


class SignupUseCase:

    def __init__(self, signup_repository: SignupRepository, log: Logging):
        self.log = log
        self.signup_repository = signup_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def new_vendor(self, body: RequestSignup, internal_transaction_id: str):
        try:
            request = body.data.to_dict()
            request_api = body.api_data.to_dict()

            if not request.get('name') and not request.get('last_name'):
                response = ResponseSignup(
                    code=-1,
                    message="Ingrese un nombre y apellido.",
                    data= [],
                    internal_transaction_id=internal_transaction_id,
                    external_transaction_id=body.external_transaction_id
                )
                return response, 400
            
            payload = {
                "code_email": request.get('code_email'),
                "status": 1 if request_api.get("status") == "ACTIVO" else None,
                "role_id": 1,
                "name": request.get('name'),
                "last_name": request.get('last_name'),
                "city": request_api.get("city"),
                "email": request_api.get("email"),
                "cellphone": request_api.get("cellphone"),
                "identification_number": request_api.get("identificationNumber"),
                "entry_date": datetime.utcnow().date(),    
                "password": request.get('password')
            }

            new_vendor = self.signup_repository.register_vendor(payload, internal_transaction_id, body.external_transaction_id)

            response = ResponseSignup(
                code="200",
                message="Vendedor registrado exitosamente.",
                data=new_vendor,
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response
        
        except Exception as ex:
            response = ResponseSignup(
                code=-1,
                message=str(ex),
                data=[],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response, 500