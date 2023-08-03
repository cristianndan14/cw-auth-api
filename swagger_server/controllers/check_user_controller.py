import connexion

from swagger_server.models.request_check_user import RequestCheckUser  # noqa: E501
from swagger_server.models.response_check_user import ResponseCheckUser  # noqa: E501
from swagger_server.models.check_user_data import CheckUserData

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging

from swagger_server.models.db.user_model import User


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
                # Cambia 'code_email' por el campo que identifica al usuario en la tabla (supongo que 'code_email' es el campo correcto)
                code_email = body.code_email

                # Realizar la consulta a la base de datos usando la instancia de SQLAlchemy
                user = User.query.filter_by(code_email=code_email).first()
                
                # Verificar si se encontró el usuario en la base de datos
                if user:

                    data = CheckUserData(code_email=user.code_email, profile=user.profile, status=user.status, name=user.name)

                    # Creemos el objeto ResponseCheckUser con los datos del usuario en la sección 'data'
                    response = ResponseCheckUser(
                        code="200",
                        message="Datos obtenidos exitosamente",
                        data=data,
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )

                else:
                    # Usuario no encontrado, creemos un objeto ResponseCheckUser con el mensaje de usuario no encontrado y sin datos
                    response = ResponseCheckUser(
                        code="404",
                        message=message,
                        data=[],
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )
                    
                    return response, 404
                    
            except Exception as ex:

                # En caso de error, creemos un objeto ResponseCheckUser con un mensaje de error genérico y sin datos
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
