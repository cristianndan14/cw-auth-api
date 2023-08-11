from swagger_server.models.response_delete_user import ResponseDeleteUser  # noqa: E501
from swagger_server.models.user_data import UserData

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internal_transaction_id
from swagger_server.utils.logs.logging import log as logging

from swagger_server.models.db.user_model import User
from urllib.parse import quote


class DeleteUserView(MethodView):

    def __init__(self):
        self.log = logging()
        self.msg_log = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'


    def delete_user(self, code_email):  # noqa: E501
        """Eliminar usuario.

        Eliminar usuario. # noqa: E501

        :param code_email: 
        :type code_email: str

        :rtype: ResponseDeleteUser
        """
        start_time = default_timer()
        response = ""
        internal_transaction_id = str(generate_internal_transaction_id())
        function_name = "delete_user"
        package_name = __name__
        log = self.log

        try:
            user = User.query.filter_by(code_email=code_email).first()

            if user:
                user.destroy()

                response = ResponseDeleteUser(
                    code="200",
                    data=user.to_json(),
                    message="Usuario eliminado exitosamente",
                    internal_transaction_id=internal_transaction_id
                )
                return response, 200
            else:
                response = ResponseDeleteUser(
                    code="404",
                    message=f"No se encontró el usuario con el code_email '{code_email}'.",
                    internal_transaction_id=internal_transaction_id
                )
                return response, 404

        except Exception as ex:
            message = str(ex)
            log = logging()
            log.critical(
                self.msg_log,
                internal_transaction_id, function_name, package_name, message)

            response = ResponseDeleteUser(
                code=-1,
                message=message,
                internal_transaction_id=internal_transaction_id
            )
            return response, 500

        finally:
            end_time = default_timer()
            message = f"end request: {function_name} - Procesada en : {round((end_time - start_time) * 1000)} milisegundos "
            log = logging()
            log.info(
                self.msg_log,
                internal_transaction_id, function_name, package_name, message)

