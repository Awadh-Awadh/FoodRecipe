from flask import Flask
from config import config_options


 #extensions instance creation




def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    #blueprints registration

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register(auth_blueprint)

    #extensions instance initializations
    return app