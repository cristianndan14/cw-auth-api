from swagger_server.resources.db import db


class Permission(db.Model):
    __tablename__ = "permissions"
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    route = db.Column(db.String(100), unique=True)
    
    def to_json(self):
        return {
            "id": self.id,
            "role_id": self.role_id,
            "route": self.route
        }
    
    def save(self):
        """
        The save function is a method that is called on an instance of the User class.
        It adds the instance to the database and commits the changes
        """
        db.session.add(self)
        db.session.commit()

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    permissions = db.relationship(Permission, backref="role", lazy=True)

    def to_json(self):
        permission_data = [permission.route for permission in self.permissions]

        return {
            "id": self.id,
            "name": self.name,
            "permissions": permission_data
        }
    
    def save(self):
        """
        The save function is a method that is called on an instance of the User class.
        It adds the instance to the database and commits the changes
        """
        db.session.add(self)
        db.session.commit()