from swagger_server.models.db.user_model import User
from swagger_server.repository.base_repository import BaseRepository


class DeleteUserRepository(BaseRepository):
    
    def delete_user(self, code_email, internal_transaction_id):
        try:
            print(code_email)
            user = User.query.filter_by(code_email=code_email).first()
            print(user)
            if user:
                user.destroy()
                return user.to_json()
            else:
                return []
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log, internal_transaction_id, "delete_user", __name__, error)
            return ""