from swagger_client import consult_request
from swagger_server.config.access import access


class TokenResetPasswordService:

    def __init__(self):
        self.service_email_notifications = self.get_service("EMAIL_NOTIFICATIONS")
        self.service_get_token_xtrim = self.get_service("TOKEN_XTRIM")
        self.content_type = "application/json; charset=utf-8"
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
    
    def get_token_xtrim(self, internal_transaction_id, external_transaction_id):
        try:
            endpoint = ""
            response = consult_request.get_request(
                internal_transaction_id,
                external_transaction_id,
                self.service_get_token_xtrim["base_url"],
                endpoint,
                self.service_get_token_xtrim["method"],
                self.service_get_token_xtrim["headers"],
                self.service_get_token_xtrim["data"],
                payload=None
            )
            token_xtrim = response.json()["data"]["token"]
            return token_xtrim
        except Exception as ex:
            return {"error": str(ex), "code": 500}
    
    def send_email_recovery_token(self, token_xtrim, recovery_token, email, internal_transaction_id, external_transaction_id):
        try:
            destination = [email]
            self.service_email_notifications["data"]["data"]["email"]["to"] = destination
            self.service_email_notifications["data"]["data"]["template"]["variables"] = [
                {"name": "fieldstr02", "value": recovery_token},
                {"name": "fieldstr01", "value": "Titulo"}
            ]
            self.service_email_notifications["headers"] = {
                "Authorization": f"Bearer {token_xtrim}",
                "Content-Type": "application/json"
            }
            endpoint = ""
            response = consult_request.get_request(
                internal_transaction_id,
                external_transaction_id,
                self.service_email_notifications["base_url"],
                endpoint,
                self.service_email_notifications["method"],
                self.service_email_notifications["headers"],
                self.service_email_notifications["data"],
                payload=None
            )
            return response.json()
        except Exception as ex:
            return {"error": str(ex), "code": 500}
        
    def get_service(self, service):
        response_json = access()["SERVICES"][service]
        response = {
            "base_url": response_json.get("URL"),
            "headers": response_json.get("HEADERS"),
            "data": response_json.get("REQUEST"),
            "method": response_json.get("METHOD")
        }
        return response