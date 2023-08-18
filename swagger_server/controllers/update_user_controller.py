import connexion

from swagger_server.models.request_update_user import RequestUpdateUser  # noqa: E501
from swagger_server.uses_cases.update_user_uses_cases import UpdateUserUseCase
from swagger_server.repository.update_user_repository import UpdateUserRepository

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class UpdateUserView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        update_user_repository = UpdateUserRepository(mysql, log)
        self.update_user_use_case = UpdateUserUseCase(update_user_repository, log)

    def update_user(self, code_email):  # noqa: E501
        """Actualizar usuario.

        Actualizar usuario. # noqa: E501

        :param code_email: 
        :type code_email: str
        :param body: 
        :type body: dict | bytes

        :rtype: ResponseUpdateUser
        """
        start_time = default_timer()
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "update_user"
        package_name = __name__
        log = self.log

        if connexion.request.is_json:

            body = RequestUpdateUser.from_dict(connexion.request.get_json())  # noqa: E501
            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)

            response = self.update_user_use_case.save_changes(code_email, body, internal_transaction_id)

            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internal_transaction_id, body.external_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response            