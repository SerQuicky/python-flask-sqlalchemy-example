from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Set up the SQLAlchemy Database (use any sql database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Solikamsk@localhost/Neblun'


# init the sqlalchemy- and mashmallow object 
db = SQLAlchemy(app)
ma = Marshmallow(app)


if __name__ == "__main__":
    from entities.brand.routes import *
    from entities.vehicle.routes import *

    app.run(debug=True)
