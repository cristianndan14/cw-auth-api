from swagger_server.resources.db import db
from swagger_server.models.db.permission_role_model import Role
from swagger_server.utils.encrypt import encrypt_password


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    code_email = db.Column(db.String(100), index=True)
    status = db.Column(db.Boolean)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    city = db.Column(db.String(100))
    address = db.Column(db.String(100))
    email = db.Column(db.String(100))
    cellphone = db.Column(db.String(100))
    department = db.Column(db.String(100))
    identification_number = db.Column(db.String(50))
    entry_date = db.Column(db.Date)
    password = db.Column(db.String(100))
    token_reset_password = db.Column(db.String(100))

    role = db.relationship(Role, backref=db.backref('users', lazy=True))

    def __init__(self, payload):
        
        self.code_email = payload.get('code_email')
        self.status = payload.get('status')
        self.role_id = payload.get('role_id')
        self.name = payload.get('name')
        self.last_name = payload.get('last_name')
        self.city = payload.get('city')
        self.address = payload.get('address')
        self.email = payload.get('email')
        self.cellphone = payload.get('cellphone')
        self.department = payload.get('department')
        self.identification_number = payload.get('identification_number')
        self.entry_date = payload.get('entry_date')
        self.password = payload.get('password')
        
    def encrypt_password(self):
        if self.password:
            self.password = encrypt_password(self.password)

    def to_json(self):
        """
        It takes the object and returns a dictionary representation of it
        :return: A dictionary with the keys and values of the user object.
        """
        role_data = self.role.to_json() if self.role else None

        return {
            "id": self.id,
            "code_email": self.code_email,
            "status": self.status,
            "role": role_data,
            "name": self.name,
            "last_name": self.last_name,
            "city": self.city,
            "address": self.address,
            "email": self.email,
            "cellphone": self.cellphone,
            "department": self.department,
            "identification_number": self.identification_number,
            "entry_date": self.entry_date,
        }

    def save(self):
        """
        The save function is a method that is called on an instance of the User class. 
        It adds the instance to the database and commits the changes
        """
        self.encrypt_password()
        db.session.add(self)
        db.session.commit()
    
    def destroy(self):
        db.session.expunge(self)

        self.role = None
        
        user_to_delete = db.session.merge(self)
        db.session.delete(user_to_delete)
        db.session.commit()
