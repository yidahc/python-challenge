import json
from __init__ import create_app
from flask import request
from crud import nQueens
from models import db, Solution

app = create_app()

# this will run on local computer on http://0.0.0.0:5001/solutions
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    n = data['n']
    results = nQueens(n)
    for result in results:
      solution = Solution(
      solution = str(result),
      n = n
      )
      db.session.add(solution)
      db.session.commit()
    return json.dumps("Solutions Added"), 200

@app.route('/solutions', methods=["GET"])
def fetch():
    solutions = Solution.query.all()
    all_solutions = []
    for x in solutions:
        new_solution = {
            "id": x.id,
            "solution": x.solution,
            "n": x.n
        }

        all_solutions.append(new_solution)
    return json.dumps(all_solutions), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# connecting to postgress db learned on https://vsupalov.com/flask-sqlalchemy-postgres/