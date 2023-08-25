from swagger_server.models.db.user_model import User
from swagger_server.repository.base_repository import BaseRepository


class RegisterUserRepository(BaseRepository):

    def register_user(self, user, internal_transaction_id: str, external_transaction_id: str):
        try:
            register_user = User(user)
            register_user.save()
            return register_user.to_json()
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.critical(self.msg_log,internal_transaction_id, external_transaction_id, "register_user", __name__, error)
            return error, 500