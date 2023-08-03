import connexion

from swagger_server.models.request_all_users import RequestAllUsers  # noqa: E501
from swagger_server.models.response_all_users import ResponseAllUsers  # noqa: E501
from swagger_server.models.user_data import UserData

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging

from swagger_server.models.db.user_model import User


class AllUsersView(MethodView):

    def __init__(self):
        self.log = logging()
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'


    def all_users(self):  # noqa: E501
        """Obtener todos los usuarios

        Obtener todos los usuarios # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseCheckUser
        """
        start_time = default_timer()
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "all_users"
        package_name = __name__
        log = self.log

        if connexion.request.is_json:

            body = RequestAllUsers.from_dict(connexion.request.get_json())
            
            external_transaction_id = body.external_transaction_id
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internal_transaction_id, external_transaction_id, function_name, package_name, message)
            
            try:

                # Realizar la consulta a la base de datos usando la instancia de SQLAlchemy
                users = User.query.all()
                
                # Verificar si se encontró el usuario en la base de datos
                if users:

                    #data = [UserData(u.to_json()) for u in user]

                    data = [u.to_json() for u in users]
                    # Creemos el objeto ResponseCheckUser con los datos del usuario en la sección 'data'
                    response = ResponseAllUsers(
                        code="200",
                        message="Datos obtenidos exitosamente",
                        data=data,
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )

                else:
                    # Usuario no encontrado, creemos un objeto ResponseCheckUser con el mensaje de usuario no encontrado y sin datos
                    response = ResponseAllUsers(
                        code="404",
                        message=message,
                        data=[],
                        internal_transaction_id=internal_transaction_id,
                        external_transaction_id=external_transaction_id
                    )
                    
            except Exception as ex:

                # En caso de error, creemos un objeto ResponseCheckUser con un mensaje de error genérico y sin datos
                message = str(ex)
                log = logging()
                log.critical(
                    self.msg_log,
                    internal_transaction_id, external_transaction_id, function_name, package_name, message)

                response = ResponseAllUsers(
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
