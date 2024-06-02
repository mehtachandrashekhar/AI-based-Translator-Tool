from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes import bp as translate_bp
    app.register_blueprint(translate_bp)
    
    return app
