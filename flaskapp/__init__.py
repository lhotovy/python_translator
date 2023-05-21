from flask import Flask

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
SECRET_KEY="Deepl secret key goes here",
)

from flaskapp import routes
