import requests, os
from flask import Flask, render_template

RESULTS_API_SERVER = os.environ['RESULTS_API_SERVER']
app = Flask(__name__)

# this will run on local computer on http://0.0.0.0:5000
@app.route('/')
def show_solutions():
    Solutions = requests.get(RESULTS_API_SERVER + "/solutions").json()  
    # this is where the results-api is running within its container
    return render_template('show_solutions.html', solutions=Solutions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    