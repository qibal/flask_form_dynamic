from flask import Flask
from config import Config
from app.database import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database
    init_db(app)
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    return app