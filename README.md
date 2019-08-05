# N Queens #

## My solution of the N-Queens challenge. ##

## AKA My first full-stack Python app, Dockerized and tested with Travis CI and Pytest ##

## Summary ##
  > Fun intro to Python and Docker-Compose producing a well-tested full-stack CRUD app with an API container that uses SQLAlchemy to store all N Queens solutions for a given N (where N <= 12) into a postgress image running in a seperate container and a surprise Front-End container that uses Flask to send requests to the API image and shows all solutions using a Bootstrap template. On command, Docker-Compose builds and runs all services seperately for seperation of concerns and without the need to install dependencies or worry about your local setup.

## Requirements ##
  > docker-compose version 3.3 
  > On Windows and Mac it comes with Docker, on Linux it must be installed seperately.
  > https://docs.docker.com/toolbox/toolbox_install_windows/

## How to Get Started ##
  > Ater cloning repo, build docker images by running the following commands from root directory:
  > - docker-compose build
  > - docker-compose up

## Loading Solutions ##
  > Only tested for up to 12 queens.
  > HTTP requests can be sent to api server on 127.0.0.1:5001
  > Example to add solutions for 10 queens: curl -XPOST -H "Content-type: application/json" -d \'{"n": "10"}' \'127.0.0.1:5001/add'
  > Once added, all solutions can be viewed on 127.0.0.1:5001/show
  > Bonus client-side for easier interaction with api on http://127.0.0.1:5000

## Trigger Testing / Travis CI Build ##
  > Any merge requests from this repo to origin master branch of this repo will trigger the Travis CI build which uses Pytest to run parallel tests on Python 2.7, 3.5 and 3.6 on functions that produce the N Queens solutions and tests that the api is able to produce all solutions for N=10, store each one correctly in db, query them from db, manipulate them properly and send them back.