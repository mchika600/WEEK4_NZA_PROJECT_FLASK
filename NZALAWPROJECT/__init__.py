from flask import Flask

# Config imports
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import for Flask Login
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

# Login Flow config
sign_in = LoginManager(app)
sign_in.sign_in_view = 'sign_in' # This specifies what page to load for non-authoed users

from NZALAWPROJECT import routes, models