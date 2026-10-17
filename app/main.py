# build b3efb115ae
# (auto) d07f7d
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
