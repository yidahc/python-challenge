import json
from flask import Flask, request
from config import DATABASE_CONNECTION_URI
from crud import nQueens, get_all
from models import db

def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()
    return flask_app

app = create_app()


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    n = data.n

    nQueens(n)
    
    return json.dumps("Solutions Added"), 200

@app.route('/', methods=['GET'])
def fetch():
    all_solutions = get_all()
    return json.dumps(all_solutions), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

