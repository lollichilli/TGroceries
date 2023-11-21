"""App config file"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Flask app
app = Flask(__name__)

this_dir = os.path.abspath(os.path.dirname(__file__))
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(this_dir, "products.sqlite3")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://yklvxguuvotzto:3c1e9942c8036f27fd4eafc5d25b0dd40ab9e2201a4fdd7f3e8716f2f0f87dee@ec2-44-213-228-107.compute-1.amazonaws.com:5432/dfaoa2eatsqsnt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# DB object
db = SQLAlchemy(app)

# Marshmallow object
mm = Marshmallow(app)

