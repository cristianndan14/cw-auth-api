from swagger_server.models.db.user_model import User
from swagger_server.repository.base_repository import BaseRepository


class SigninUsersRepository(BaseRepository):
    
    def get_user(self, code_email: str, internal_transaction_id: str, external_transaction_id: str):
        try:
            user = User.query.filter_by(code_email=code_email).first()
            return user
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log,internal_transaction_id, external_transaction_id, "get_user", __name__, error)
            return error, 500