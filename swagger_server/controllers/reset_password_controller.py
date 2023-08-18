import connexion

from swagger_server.models.request_reset_password import RequestResetPassword  # noqa: E501
from swagger_server.uses_cases.reset_password_uses_cases import ResetPasswordUseCase
from swagger_server.repository.reset_password_repository import ResetPasswordRepository

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class ResetPasswordView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        reset_password_repository = ResetPasswordRepository(mysql, log)
        self.reset_password_use_case = ResetPasswordUseCase(reset_password_repository, log)

    def reset_password(self):  # noqa: E501
        """Resetear password

        Resetear password # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseResetPassword
        """
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "reset_password"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:
            body = RequestResetPassword.from_dict(connexion.request.get_json())  # noqa: E501
            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)
            
            response = self.reset_password_use_case.reset_password(body, internal_transaction_id)

            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internal_transaction_id, body.external_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response