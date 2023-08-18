from swagger_client import consult_request
from swagger_server.config.access import access


class CheckUserService:

    def __init__(self):
        self.service_data = access()["SERVICES"]["CEDULA_VENTAS"]
        self.base_url = self.service_data["URL"]
        self.headers = self.service_data["HEADERS"]
        self.request_data = self.service_data["REQUEST"]
        self.content_type = "application/json; charset=utf-8"
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
    
    def check_vendor(self, code_email, internal_transaction_id, external_transaction_id):
        try:
            self.request_data["identificationNumber"] = code_email
            endpoint = ""
            method = "POST"
            response = consult_request.get_request(
                internal_transaction_id,
                external_transaction_id,
                self.base_url,
                endpoint,
                method,
                self.headers,
                self.request_data,
                payload=None
            )
            return response.json()
        except Exception as ex:
            return {"error": str(ex)}, 500