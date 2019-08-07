import requests, os
from flask import Flask, render_template, request, redirect, url_for

RESULTS_API_SERVER = os.environ['RESULTS_API_SERVER']
app = Flask(__name__)

# this will run on local computer on http://0.0.0.0:5000
@app.route('/solutions')
def show_solutions():
    # RESULTS_API_SERVER is where the results-api is running within its container
    Solutions = requests.get(RESULTS_API_SERVER + "/show").json()  
    # rendering html template using Solutions (response from api) as an argument to use in template, under name solutions
    return render_template('show_solutions.html', solutions=Solutions)


@app.route('/', methods=['GET', 'POST'])
def add_solutions():
    if request.method == 'GET':
        # when page first loads, render template that allows user to input value for N
        return render_template('add_solutions.html')
    else:
        # send post request with value of n as a json for api to add solutions to db
        json = {
            'n': request.form['n']
        }
        response = requests.post(RESULTS_API_SERVER + "/add", json=json)
        # checking solutions have been correctly added
        if response.status_code == 200:
            # redirect to view solutions we just added
            return redirect(url_for('show_solutions'))  


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')