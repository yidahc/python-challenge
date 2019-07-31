import json
from __init__ import create_app
from flask import request
from models import db, Solution
from crud import nQueens

app = create_app()

# this will run on local computer on http://0.0.0.0:5001/solutions
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    n = data['n']
    results = nQueens(int(n), [], [])
    # for some reason, after its already bee run once, nQueens does not run
    #  with an empty array for results unless specified here at calltime
    print (results)
    total = len(results)
    for result in results:
        entry = Solution(
        array = str(result),
        n = n,
        total = total
        )
        db.session.add(entry)
    db.session.commit()
    return json.dumps("Solutions Added"), 200

@app.route('/show', methods=["GET"])
def fetch():
    solutions = Solution.query.all()
    all_solutions = []
    for x in solutions:
        new_solution = {
            "id": x.id,
            "array": x.array,
            "n": x.n,
            "total": x.total
        }

        all_solutions.append(new_solution)
    return json.dumps(all_solutions), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# connecting to postgress db learned on https://vsupalov.com/flask-sqlalchemy-postgres/