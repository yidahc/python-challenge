import requests 
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for

RESULTS_API_SERVER = 'os.environ['RESULTS_API_SERVER']'
app = Flask(__name__)

@app.route('/view')
def show_solutions():
    Results = requests.get(RESULTS_API_SERVER + "/").json()
    return render_template('show_solutions.html', solutions=Results)


@app.route('/', methods=['GET', 'POST'])
def add_solutions():
    if request.method == 'GET':
        return render_template('add_solutions.html')
    else:
        json = {
            'n': request.form['n']
        }
        response = requests.post(RESULTS_API_SERVER + "/add", json=json)
        if response.status_code == 200:
            return redirect(url_for('show_solutions'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')