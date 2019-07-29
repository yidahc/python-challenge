from flask import Flask
from flask import jsonify
from crud import nQueens

app = Flask(__name__)

@app.route('/')
def hello_world():
    results = nQueens(10)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
