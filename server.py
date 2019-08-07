import json
from __init__ import create_app
from flask import request
from models import db, Solution
from queens import nQueens, matrixBoards

app = create_app()

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    n = data['n']
    # use nQueens function to produce list of solution boards based on input value for n
    # After its already been run once, nQueens does not run with an empty array for results unless specified here at calltime
    results = nQueens(int(n), [], [])
    # gather amount of solutions generated for this value of n
    total = len(results)
    # for each board(list) in results list, add it as a new entry (instance of Solution class from models) into db, 
    # with its corresponding n and total amount of solutions for that n
    for result in results:
        entry = Solution(
        board = str(result),
        n = n,
        total = total
        )
        db.session.add(entry)
    # commit all additions to db
    db.session.commit()
    return json.dumps("Solutions Added"), 200

@app.route('/show', methods=["GET"])
# this will run on local computer on http://0.0.0.0:5001/show
def fetch():
    # query all entries(rows) in db
    solutions = Solution.query.all()
    all_solutions = []
    # iterate through queried solutions and 
    for solution in solutions:
        new_solution = {
            "id": solution.id,
            "board": solution.board,
            "n": solution.n,
            "total": solution.total
        }
    # restructure each class instance as dictionaries to store in all_solutions list
        all_solutions.append(new_solution)
    return json.dumps(all_solutions), 200
    # return list with nested dictionaries of all solutions as a json

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
