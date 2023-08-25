from swagger_server.models.db.user_model import User
from swagger_server.repository.base_repository import BaseRepository


class AllUsersRepository(BaseRepository):
    
    def get_users(self, internal_transaction_id, external_transaction_id):
        try:
            users = User.query.all()
            if users:
                data = [u.to_json() for u in users]
                return data
            else:
                return []
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.critical(self.msg_log,internal_transaction_id, external_transaction_id, "get_all_users", __name__, error)
            return ""