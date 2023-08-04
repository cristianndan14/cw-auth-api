import connexion
import re
import requests

from swagger_server.models.request_signup import RequestSignup  # noqa: E501
from swagger_server.models.response_signup import ResponseSignup  # noqa: E501
from swagger_server.models.db.user_model import User
from swagger_server.models.response_reset_password_data import ResponseResetPasswordData

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging
from swagger_server.utils.encrypt import encrypt_password

from swagger_server.config.access import access


class SignupView(MethodView):

    def __init__(self):
        self.log = logging()
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'


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

            try:

                request = body.data.to_dict()

                code_email = request.get('code_email')
                password = encrypt_password(request.get('password'))

                patron = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#=_+-])[A-Za-z\d@$!%*?&#=_+-]{7,}$"

                api = access().get("SERVICES").get("CEDULA_VENTAS")

                api_url = api.get("URL")
                api_headers = api.get("HEADERS")
                api_request = api.get("REQUEST")

                api_request.update({"identificationNumber": code_email})

                response_api = requests.post(api_url, json=api_request ,headers=api_headers).json().logging()

                response_api_data = response_api.get("data")
                print(response_api_data)

                user_exist = User.query.filter_by(code_email=code_email).first()
                

                if user_exist:

                    response = ResponseSignup(
                        code=-1,
                        message=f"Ya existe un usuario con el code_email {code_email}",
                        data= [],
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )

                    return response, 400

                if re.match(patron, request.get('password')) and response_api.get("code") == 200:

                    new_vendor = {
                        "code_email": code_email,
                        "city": response_api_data.get("city"),
                        "status": response_api_data.get("status"),
                        "email": response_api_data.get("email"),
                        "phone": response_api_data.get("phone"),
                        "password": password,
                        "profile": "vendor",
                        
                    }

                    add_vendor = User(new_vendor)
                    
                    add_vendor.save()

                    data = ResponseResetPasswordData(code_email=add_vendor.code_email)
                    
                    response = ResponseSignup(
                        code="200",
                        message="Vendedor registrado exitosamente.",
                        data= data,
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )

                else:
                    response = ResponseSignup(
                        code=-1,
                        message="La contraseña no cumple los requisitos de seguridad. Debe contener al menos 7 carateres compuestos por Mayúsculas, números y caracteres especiales" if not re.match(patron, request.get('password')) 
                                    else response_api.get("message"),
                        data= [],
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )

                    return response, 400

            except Exception as ex:

                message = str(ex)
                log = logging()
                log.critical(
                    self.msg_log,
                    internal_transaction_id, external_transaction_id, function_name, package_name, message)

                response = ResponseSignup(
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

