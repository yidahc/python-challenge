from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_solutions():
    Solutions = [[0, 2, 4, 1, 3], [0, 3, 1, 4, 2], [1, 3, 0, 2, 4], [1, 4, 2, 0, 3], [2, 0, 3, 1, 4], [2, 4, 1, 3, 0], [3, 0, 2, 4, 1], [3, 1, 4, 2, 0], [4, 1, 3, 0, 2], [4, 2, 0, 3, 1]] 
    return render_template('show_solutions.html', solutions=Solutions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')