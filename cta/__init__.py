from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# Initializes Flask
app = Flask(__name__)

# initialize database
db = SQLAlchemy(app)

# Intialize Marshmallow
ma = Marshmallow(app)

# Load config
app.config.from_pyfile('../config.cfg')
# print(app.config['BROKER_URL'])
import cta.view
