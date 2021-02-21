from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "0101010101"

from my_app import routes
