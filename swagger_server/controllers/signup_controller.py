import connexion

from swagger_server.models.request_signup import RequestSignup  # noqa: E501
from swagger_server.uses_cases.signup_uses_cases import SignupUseCase
from swagger_server.repository.signup_repository import SignupRepository

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class SignupView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        signup_repository = SignupRepository(mysql, log)
        self.signup_use_case = SignupUseCase(signup_repository, log)


    def signup(self):  # noqa: E501
        """Registrar vendedor

        Registrar vendedor # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseSignup
        """
        start_time = default_timer()
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "signup"
        package_name = __name__
        log = self.log

        if connexion.request.is_json:

            body = RequestSignup.from_dict(connexion.request.get_json())  # noqa: E501
            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)

            response = self.signup_use_case.new_vendor(body, internal_transaction_id)

            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internal_transaction_id, body.external_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response