from swagger_server.models.db.user_model import User
from swagger_server.repository.base_repository import BaseRepository


class UpdateUserRepository(BaseRepository):
    
    def get_user(self, code_email: str, internal_transaction_id: str, external_transaction_id: str):
        try:
            user = User.query.filter_by(code_email=code_email).first()
            return user
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log,internal_transaction_id, external_transaction_id, "get_user", __name__, error)
            return error, 500
        
    def update_user(self, user: User, data: dict, internal_transaction_id: str, external_transaction_id: str):
        try:
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
            
            user.save()
            return user.to_json()
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log,internal_transaction_id, external_transaction_id, "update_user", __name__, error)
            return error, 500