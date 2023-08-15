import connexion

from swagger_server.models.request_update_user import RequestUpdateUser  # noqa: E501
from swagger_server.models.response_update_user import ResponseUpdateUser  # noqa: E501

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging

from swagger_server.models.db.user_model import User

from swagger_server.config.access import access


class UpdateUserView(MethodView):

    def __init__(self):
        self.log = logging()
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'

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

            try:
                user = User.query.filter_by(code_email=code_email).first()
                
                if user is None:
                    response = ResponseUpdateUser(
                        code="404",
                        message="Usuario inexistente",
                        data=[],
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )
                    return response, 404
                
                data = body.data.to_dict()
                print(f"user encontrado: {user.to_json()}")
                print(f"data ingresada: {data}")
                user.status = data.get("status")
                user.role_id = data.get("role_id")
                user.name = data.get("name")
                user.last_name = data.get("last_name")
                user.city = data.get("city")
                user.address = data.get("address")
                user.email = data.get("email")
                user.cellphone = data.get("cellphone")
                user.department = data.get("department")
                user.identification_number = data.get("identification_number")
                user.password = data.get("password")
                print(f"user actualizado: {user.to_json()}")

                user.save()

                response = ResponseUpdateUser(
                    code="200",
                    message="Usuario actualizado",
                    data=user.to_json(),
                    internal_transaction_id=internal_transaction_id,
                    external_transaction_id=external_transaction_id
                )
                return response
                    
            except Exception as ex:
                message = str(ex)
                log = logging()
                log.critical(
                    self.msg_log,
                    internal_transaction_id, external_transaction_id, function_name, package_name, message)

                response = ResponseUpdateUser(
                    code=-1,
                    message=message,
                    data= [],
                    internal_transaction_id=internal_transaction_id,
                    external_transaction_id=external_transaction_id
                )
                return response
                
            finally: 
                end_time = default_timer()
                message = f"end request: {function_name} - Procesada en : {round((end_time - start_time) * 1000)} milisegundos "
                log = logging()
                log.info(
                    self.msg_log,
                    internal_transaction_id, external_transaction_id, function_name, package_name, message)
        
        return response
