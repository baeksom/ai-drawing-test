from flask import Flask, g
from db_connect import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@127.0.0.1:3306/ai-htp-test"
app.config['SQLARCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ekdwls'

db.init_app(app)

import tensorflow as tf

# 블루프린트
from api import main, drawing

app.register_blueprint(main.bp)
app.register_blueprint(drawing.bp)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
