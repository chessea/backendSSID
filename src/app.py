from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__)

#CORS

CORS(app)

# Routes
from merakiData import  routes

load_dotenv()

################################