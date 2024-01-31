from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

    if app.config['DEBUG']:
        with app.app_context():
            db.create_all()

    return app