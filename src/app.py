from flask import Flask
from flask_cors import CORS
import config as c

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"