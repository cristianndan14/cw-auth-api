from swagger_server.resources.db import db


class Permission(db.Model):
    __tablename__ = "permissions"
    permission_id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"))
    route_id = db.Column(db.Integer, db.ForeignKey("routes.route_id"))

    role = db.relationship("Role", back_populates="permissions")
    route = db.relationship("Route", back_populates="permissions")

    def __init__(self, payload):
        self.route_id = payload.get('route_id')
        self.role_id = payload.get('role_id')

    def to_json(self):
        return {
            "permission_id": self.permission_id,
            "role_id": self.role_id,
            "role_name": self.role.role_name if self.role else None,
            "route_data": {"route_id": self.route.route_id, "route_name": self.route.route_name}
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def destroy(self):
        db.session.delete(self)
        db.session.commit()


class Role(db.Model):
    __tablename__ = "roles"
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(100), unique=True)

    permissions = db.relationship("Permission", back_populates="role")

    def __init__(self, payload):
        self.role_name = payload.get('role_name')

    def to_json(self):
        permission_data = [
            {"route_id": permission.route_id, "route_name": permission.route.route_name}
            for permission in self.permissions
        ]

        return {
            "role_id": self.role_id,
            "role_name": self.role_name,
            "permissions": permission_data
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def destroy(self):
        db.session.delete(self)
        db.session.commit()


class Route(db.Model):
    __tablename__ = "routes"
    route_id = db.Column(db.Integer, primary_key=True)
    route_name = db.Column(db.String(100), unique=True)

    permissions = db.relationship("Permission", back_populates="route")

    def __init__(self, payload):
        self.route_name = payload.get('route_name')

    def to_json(self):
        return {
            "route_id": self.route_id,
            "route_name": self.route_name
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def destroy(self):
        db.session.delete(self)
        db.session.commit()