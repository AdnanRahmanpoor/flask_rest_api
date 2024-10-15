from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    api = Api(app)

    # import registration resources and auth routes
    from .resources import ResourceList, ResourceDetail
    from .auth import RegisterUser, LoginUser

    # Register API endpoints
    api.add_resource(RegisterUser, '/register')
    api.add_resource(LoginUser, '/login')
    api.add_resource(ResourceList, '/resource')
    api.add_resource(ResourceDetail, '/resource/<int:resource_id>')

    return app