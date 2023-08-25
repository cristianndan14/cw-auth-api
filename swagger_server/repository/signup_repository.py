from swagger_server.models.db.user_model import User
from swagger_server.repository.base_repository import BaseRepository


class SignupRepository(BaseRepository):
    
    def register_vendor(self, vendor: dict, internal_transaction_id: str, external_transaction_id: str):
        try:
            new_vendor = User(vendor)
            new_vendor.save()
            return new_vendor.to_json()
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.critical(self.msg_log,internal_transaction_id, external_transaction_id, "register_vendor", __name__, error)
            return error, 500