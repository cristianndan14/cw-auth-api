import connexion
import re

from swagger_server.models.request_signup import RequestSignup  # noqa: E501
from swagger_server.models.response_signup import ResponseSignup  # noqa: E501
from swagger_server.models.db.user_model import User
from swagger_server.models.user_data import UserData

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging


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
                request_api = body.api_data.to_dict()

                code_email = request.get('code_email')
                password = request.get('password')
                name = request.get('name')

                patron = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#=_+-])[A-Za-z\d@$!%*?&#=_+-]{7,}$"
                

                if re.match(patron, password) and name:

                    new_vendor = {
                        "code_email": code_email,
                        "profile": "vendor",
                        "name": name,
                        "phone": request_api.get("cellphone"),
                        "email": request_api.get("email"),
                        "city": request_api.get("city"),
                        "status": request_api.get("status"),
                        "role": 1,
                        "leader": request_api.get("leader"),
                        "sales_channel": request_api.get("salesChannel"),                      
                        "password": password
                    }

                    add_vendor = User(new_vendor)
                    
                    add_vendor.save()

                    data = UserData(
                        code_email=add_vendor.code_email,
                        profile=add_vendor.profile,
                        name=add_vendor.name,
                        phone=add_vendor.phone,
                        email=add_vendor.email,
                        city=add_vendor.city,
                        status=add_vendor.status,
                        role_id=add_vendor.role_id,
                        leader=add_vendor.leader,
                        sales_channel=add_vendor.sales_channel
                    )
                    
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
                        message="La contraseña debe contener al menos 7 carateres compuestos por Mayúsculas, números y caracteres especiales" if not re.match(patron, password) else "Ingrese un nombre",
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

