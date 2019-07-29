from flask import Flask, jsonify
from crud import nQueens

app = Flask(__name__)

# this will run on local computer on http://0.0.0.0:5001/solutions
@app.route('/solutions', methods=["GET"])
def get_solutions():
    results = nQueens(10)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
