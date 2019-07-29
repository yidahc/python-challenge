import json
from __init__ import create_app
from flask import request
from config import DATABASE_CONNECTION_URI
from crud import nQueens, get_all
from models import db

app = create_app()


@app.route('/add', methods=['POST'])
def add():
    data = input("Enter N:")
    n = int(data)
    nQueens(n)
    db.session.commit()
    return ("Solutions Added"), 200

@app.route('/', methods=['GET'])
def fetch():
    all_solutions = get_all()
    return (all_solutions), 200


