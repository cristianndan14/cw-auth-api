from swagger_server.resources.db import db
from swagger_server.models.db.permission_role_model import Role
from swagger_server.models.db.goals_model import Goals
from swagger_server.utils.encrypt import encrypt_password
from sqlalchemy.orm.exc import NoResultFound


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100))
    code_email = db.Column(db.String(100), index=True)
    email = db.Column(db.String(100))
    id_goal = db.Column(db.Integer, db.ForeignKey('goals.id_goal'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    leader = db.Column(db.Integer)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    profile = db.Column(db.String(100))
    sales_channel = db.Column(db.String(100))
    status = db.Column(db.String(100))
    token_reset_password = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now())

    role = db.relationship(Role, backref=db.backref('users', lazy=True))
    goals = db.relationship(Goals, backref=db.backref('users', lazy=True))

    def __init__(self, payload):
        self.city = payload.get('city')
        self.code_email = payload.get('code_email')
        self.email = payload.get('email')
        self.leader = payload.get('leader')
        self.name = payload.get('name')
        self.password = payload.get('password')
        self.phone = payload.get('phone')
        self.profile = payload.get('profile')
        self.role_id = payload.get('role_id')
        self.goals = payload.get('goals')
        self.sales_channel = payload.get('sales_channel')
        self.status = payload.get('status')

    def encrypt_password(self):
        # Ciframos la contraseña solo si se proporciona una contraseña válida
        if self.password:
            self.password = encrypt_password(self.password)

    def to_json(self):
        """
        It takes the object and returns a dictionary representation of it
        :return: A dictionary with the keys and values of the user object.
        """
        role_data = self.role.to_json() if self.role else None
        goals_data = self.goals.to_json() if self.goals else None

        return {
            "id": self.id,
            "city": self.city,
            "code_email": self.code_email,
            "email": self.email,
            "leader": self.leader,
            "name": self.name,
            "phone": self.phone,
            "profile": self.profile,
            "role": role_data,
            "goals": goals_data,
            "sales_channel": self.sales_channel,
            "status": self.status,
            "token_reset_password": self.token_reset_password,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    @staticmethod
    def get_user_by(code_email):
        try:
            result = User.query.filter_by(code_email=code_email).first()
            return result
        except NoResultFound:
            return None

    def save(self):
        """
        The save function is a method that is called on an instance of the User class. 
        It adds the instance to the database and commits the changes
        """
        self.encrypt_password()
        db.session.add(self)
        db.session.commit()
    
    def destroy(self):
        db.session.delete(self)
        db.session.commit()
