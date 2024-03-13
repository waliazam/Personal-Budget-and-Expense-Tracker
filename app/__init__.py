from flask import Flask
from flask_login import LoginManager
from .models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

users = {}  # This will store users in memory

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

from app import routes
