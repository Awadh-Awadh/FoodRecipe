from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap


 #extensions instance creation

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    #blueprints registration

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    #extensions instance initializations
    bootstrap.init_app(app)
    
    from .requests import configure_request
    configure_request(app)
    return app