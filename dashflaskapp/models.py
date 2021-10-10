from dashflaskapp import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.password}')"