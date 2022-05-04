from flask import Flask, request, redirect, render_template, session, url_for, jsonify
from api.api import api

import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

# register blueprint
app.register_blueprint(api, url_prefix='/api')
app.config["JSON_AS_ASCII"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["JSON_SORT_KEYS"]=False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/loaderio-ce8dc6e38fb4f981f9c63b872310eda0/")
def test():
    return render_template("test.html")




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
