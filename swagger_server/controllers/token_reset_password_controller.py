import connexion

from swagger_server.models.request_token_reset_password import RequestTokenResetPassword  # noqa: E501
from swagger_server.repository.token_reset_password_repository import TokenResetPasswordRepository
from swagger_server.uses_cases.token_reset_password_uses_cases import TokenResetPasswordUseCase

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class TokenResetPasswordView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        token_reset_password_repository = TokenResetPasswordRepository(mysql, log)
        self.token_reset_password_use_case = TokenResetPasswordUseCase(token_reset_password_repository, log)

    def token_reset_password(self):  # noqa: E501
        """Generar token para resetear password

        Generar token para resetear password # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseTokenResetPassword
        """
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "token_reset_password"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:
            body = RequestTokenResetPassword.from_dict(connexion.request.get_json())  # noqa: E501
            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)

            response = self.token_reset_password_use_case.recovery_password(body, internal_transaction_id)
            
            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internal_transaction_id, body.external_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response