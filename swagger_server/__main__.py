#!/usr/bin/env python3

import connexion
from connexion.resolver import MethodViewResolver
from swagger_server import encoder
from swagger_server.resources.db import db
from swagger_server.config.access import access

config = access()


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'auth-ms'}, pythonic_params=True,
                resolver=MethodViewResolver("swagger_server.controllers"))
    app.app.config["SQLALCHEMY_DATABASE_URI"] = config.get("SQLALCHEMY_DATABASE_URI")
    db.init_app(app.app)
    app.run(port=2057, debug=True)



if __name__ == '__main__':
    main()
