from flask import Flask
from app.main.views import main

def create_app():
    app = Flask(__name__)
    if app.config['ENV'] == 'production':
        app.config.from_object('config.ProductionConfig')
    elif app.config['ENV'] == 'testing':
        app.config.from_object('config.TestingConfig')
    elif app.config['ENV'] == 'development':
        app.config.from_object('config.DevelopmentConfig')
    
    app.register_blueprint(main)
    return app