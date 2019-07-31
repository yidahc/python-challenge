import requests, os
from flask import Flask, render_template, request, redirect, url_for

RESULTS_API_SERVER = os.environ['RESULTS_API_SERVER']
app = Flask(__name__)

# this will run on local computer on http://0.0.0.0:5000
@app.route('/solutions')
def show_solutions():
    Solutions = requests.get(RESULTS_API_SERVER + "/show").json()  
    # RESULTS_API_SERVER is where the results-api is running within its container
    return render_template('show_solutions.html', solutions=Solutions)


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