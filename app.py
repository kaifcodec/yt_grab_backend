from flask import Flask
from flask_cors import CORS
from config import Config
from routes import api

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
app.register_blueprint(api)

@app.route('/')
def index():
    return {"message": "YouTube Downloader Backend is Running!"}
