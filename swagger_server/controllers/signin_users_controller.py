import connexion

from swagger_server.models.request_signin import RequestSignin  # noqa: E501
from swagger_server.uses_cases.signin_users_uses_cases import SigninUsersUseCase
from swagger_server.repository.signin_users_repository import SigninUsersRepository

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class SigninView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        signin_users_repository = SigninUsersRepository(mysql, log)
        self.signin_users_use_case = SigninUsersUseCase(signin_users_repository, log)

    def signin(self):  # noqa: E501
        """Inicio de sesion de usuarios

        Inicio de sesion de usuarios # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseSignin
        """
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "signin"
        package_name = __name__
        log = self.log
        start_time = default_timer()

        if connexion.request.is_json:

            body = RequestSignin.from_dict(connexion.request.get_json())  # noqa: E501
            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)
            
            response = self.signin_users_use_case.login_user(body, internal_transaction_id)

            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internal_transaction_id, body.external_transaction_id, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response