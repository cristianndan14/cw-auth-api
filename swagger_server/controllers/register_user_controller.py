import connexion

from swagger_server.models.request_register_user_by_admin import RequestRegisterUserByAdmin  # noqa: E501
from swagger_server.uses_cases.register_user_uses_cases import RegisterUserUseCase
from swagger_server.repository.register_user_repository import RegisterUserRepository

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class RegisterUserView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        register_user_repository = RegisterUserRepository(mysql, log)
        self.register_user_use_case = RegisterUserUseCase(register_user_repository, log)    
    
    def register_user(self):  # noqa: E501
        """Registrar usuario

        Registrar usuario desde el administrador # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseRegisterUserByAdmin
        """
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "register_user"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:
            body = RequestRegisterUserByAdmin.from_dict(connexion.request.get_json())
            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)
        
            response = self.register_user_use_case.new_user(body, internal_transaction_id)

            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internal_transaction_id, body.external_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response