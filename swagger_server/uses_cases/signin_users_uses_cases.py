from swagger_server.models.response_signin import ResponseSignin
from swagger_server.repository.signin_users_repository import SigninUsersRepository
from swagger_server.models.request_signin import RequestSignin
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.utils.encrypt import encrypt_password


class SigninUsersUseCase:

    def __init__(self, signin_users_repository: SigninUsersRepository, log: Logging):
        self.log = log
        self.signin_users_repository = signin_users_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def login_user(self, body: RequestSignin, internal_transaction_id: str):
        try:
            request = body.data.to_dict()

            user = self.signin_users_repository.get_user(request.get('code_email'), internal_transaction_id, body.external_transaction_id)

            if user.password != encrypt_password(request.get('password')):
                response = ResponseSignin(
                    code="400",
                    message="Usuario o contraseña inválida.",
                    data= [],
                    internal_transaction_id=internal_transaction_id,
                    external_transaction_id=body.external_transaction_id
                )
                return response, 400
            
            response = ResponseSignin(
                code="200",
                message="Inicio de sesión exitoso.",
                data=user.to_json(),
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response
        
        except Exception as ex:
            response = ResponseSignin(
                code=-1,
                message=str(ex),
                data= [],
                internal_transaction_id=internal_transaction_id,
                external_transaction_id=body.external_transaction_id
            )
            return response, 500