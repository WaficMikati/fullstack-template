from app.routes.health import health_bp
from app.routes.users import users_bp
from app.routes.index import index_bp


def register_blueprints(app):
    app.register_blueprint(index_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
