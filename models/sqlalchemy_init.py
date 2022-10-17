from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from core import app
db = SQLAlchemy(app, session_options={'expire_on_commit':True})
migrate = Migrate(app, db)