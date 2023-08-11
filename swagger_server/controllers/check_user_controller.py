import connexion
import requests

from swagger_server.models.request_check_user import RequestCheckUser  # noqa: E501
from swagger_server.models.response_check_user import ResponseCheckUser  # noqa: E501
from swagger_server.models.check_user_data import CheckUserData

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging

from swagger_server.models.db.user_model import User

from swagger_server.config.access import access


class CheckUserView(MethodView):


    def __init__(self):
        self.log = logging()
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'


    def get_user(self):  # noqa: E501
        """Obtener un usuario

        Obtener un usuario # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseCheckUser
        """
        start_time = default_timer()
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "get_user"
        package_name = __name__
        log = self.log

        if connexion.request.is_json:
            body = RequestCheckUser.from_dict(connexion.request.get_json())
            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)
            
            try:
                code_email = body.code_email
                user = User.query.filter_by(code_email=code_email).first()
                
                if user:
                    response = ResponseCheckUser(
                        code="200",
                        message="Datos obtenidos exitosamente",
                        data=user.to_json(),
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )
                    return response, 200
                
                api = access().get("SERVICES").get("CEDULA_VENTAS")

                api_url = api.get("URL")
                api_headers = api.get("HEADERS")
                api_request = api.get("REQUEST")
                api_request.update({"identificationNumber": code_email})

                response_api = requests.post(api_url, json=api_request ,headers=api_headers).json()

                if response_api.get("code") == 200:

                    response = {
                        "code": "201",
                        "message": "Datos obtenidos de la cedula de ventas",
                        "api_data": response_api.get("data"),
                        "internal_transaction_id": internal_transaction_id,
                        "external_transaction_id": external_transaction_id
                    }

                    return response, 201
                else:
                    response = ResponseCheckUser(
                        code="404",
                        message="Usuario inexistente",
                        data=[],
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )
                    return response, 404
                    
            except Exception as ex:
                message = str(ex)
                log = logging()
                log.critical(
                    self.msg_log,
                    internal_transaction_id, external_transaction_id, function_name, package_name, message)

                response = ResponseCheckUser(
                    code=-1,
                    message=message,
                    data= [],
                    internal_transaction_id=internal_transaction_id,
                    external_transaction_id=external_transaction_id
                )
                
            finally: 
                end_time = default_timer()
                message = f"end request: {function_name} - Procesada en : {round((end_time - start_time) * 1000)} milisegundos "
                log = logging()
                log.info(
                    self.msg_log,
                    internal_transaction_id, external_transaction_id, function_name, package_name, message)

        return response
