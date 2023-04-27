from flask import Flask



# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
SECRET_KEY="gd6df5g4fhfg64h6fggh46gh",
)

from flaskapp import routes
