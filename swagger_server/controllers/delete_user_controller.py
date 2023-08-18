from swagger_server.models.response_delete_user import ResponseDeleteUser  # noqa: E501
from swagger_server.uses_cases.delete_user_uses_cases import DeleteUserUseCase
from swagger_server.repository.delete_user_repository import DeleteUserRepository

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class DeleteUserView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        delete_user_repository = DeleteUserRepository(mysql, log)
        self.delete_user_use_case = DeleteUserUseCase(delete_user_repository, log)

    def delete_user(self, code_email: str):  # noqa: E501
        """Eliminar usuario.

        Eliminar usuario. # noqa: E501

        :param code_email: 
        :type code_email: str

        :rtype: ResponseDeleteUser
        """
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "delete_user"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        message = f"start request: {function_name}"
        log.info(
            self.msg_log,
            internal_transaction_id, function_name, package_name, message)

        response = self.delete_user_use_case.delete_user(code_email, internal_transaction_id)

        end_time = default_timer()
        log.info("ITID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internal_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
        return response
    

