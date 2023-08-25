from swagger_server.models.db.user_model import User
from swagger_server.repository.base_repository import BaseRepository


class CheckUserRepository(BaseRepository):
    
    def get_user(self, body, internal_transaction_id, external_transaction_id):
        try:
            code_email = body.code_email
            user = User.query.filter_by(code_email=code_email).first()
            return user.to_json()
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.critical(self.msg_log,internal_transaction_id, external_transaction_id, "get_user", __name__, error)
            return ""