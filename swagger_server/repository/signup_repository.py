from swagger_server.models.db.user_model import User
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class SignupRepository:

    def __init__(self, mysql: db, log: logging ) -> None:
        self.log = log
        self.mysql = mysql
        self.sql_error_message = "Error durante la consulta en mysql :"
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def error_message_format(self, ex):
        return "Error durante la consulta en mysql : {}".format(ex)
    
    def register_vendor(self, vendor: dict, internal_transaction_id: str, external_transaction_id: str):
        try:
            new_vendor = User(vendor)
            new_vendor.save()
            return new_vendor.to_json()
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log,internal_transaction_id, external_transaction_id, "register_vendor", __name__, error)
            return error, 500