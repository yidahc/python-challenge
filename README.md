# N Queens [![Build Status](https://travis-ci.org/yidahc/python-challenge.svg?branch=master)](https://travis-ci.org/yidahc/python-challenge) #
My solution to the N-Queens puzzle, in the form of a full-stack Python app, Dockerized and passing Pytests on Travis CI builds.


## Description ##
  Fun intro to Python and Docker, using Python to generate solutions for a given N and producing an API container With Docker-Compose that uses Flask_SQLAlchemy for CRUD operations on solutions into a seperate PostgreSQL image.


## Requirements ##
  **Docker-Compose version 3.3** 
  
  - On Windows and Mac it comes with [Docker 1.8](https://docs.docker.com/toolbox/toolbox_install_windows/), on Linux it must be installed seperately

  - On command, Docker-Compose builds and runs all services seperately (along with a front-end just for fun) for seperation of concerns and without the need to install dependencies or worry about your local setup.


## How to Get Started ##
  Just clone repo and load the docker containers by running the following commands:
    
  ```bash
  git clone https://github.com/yidahc/python-challenge.git
  cd python-challenge
  docker-compose build
  docker-compose up
  ```


## Usage ##
  HTTP requests can be sent to api server on 127.0.0.1:5001

  Example post request with curl to add solutions for 10 queens: 

  ```bash
  curl -XPOST -H "Content-type: application/json" -d \'{"n": "10"}' \'127.0.0.1:5001/add'
  ```

  All solutions can be viewed on [http://127.0.0.1:5001/show](http://127.0.0.1:5001/show)

  Client-side for easier interaction with api on [http://127.0.0.1:5000](http://127.0.0.1:5000)


## Travis CI Build [![Build Status](https://travis-ci.org/yidahc/python-challenge.svg?branch=master)](https://travis-ci.org/yidahc/python-challenge) ##
  
  Runs Pytests that confirm we are producing the correct amount of solutions for a given N and that every board is a valid solution for that N (only tested for up to 12 queens)

    
## Roadmap ##
  > - Next version will include tests to confirm there are no duplicate solutions for a given N
>
  > - Test that the api is performing CRUD operations and sending the correct responses 
>
  > - And run parallel tests on Python 2.7, 3.5, 3.6 and 3.7
>

## Documentation and References Used

### N-queens and Python
- http://code.activestate.com/recipes/576647-eight-queens-six-lines/?fbclid=IwAR2agAgxDON-HRZieQm3hcSfXRIcho0PStTml6uScNrs-McgXf7nydvyZaM
- https://www.w3schools.com/python/python_syntax.asp
- https://github.com/BrunoTorresF/pyQueens/blob/master/pyQueens.py

### Pytest
- https://docs.pytest.org/en/latest/getting-started.html#getstarted
- https://www.guru99.com/pytest-tutorial.html?fbclid=IwAR2BRdcMLu4TUe5QwbC5fQFSb4le2y9zgUXX3yEsxuuRosBzgfl402-CyHg
- https://github.com/cuenca-mx/clabe-python/blob/master/test_clabe.py

### Postgres and SQLAlchemy
- https://vsupalov.com/flask-sqlalchemy-postgres/
- https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/?fbclid=IwAR2YYvFgPMvGfEIeFPSVsZ0XvIQCWpvzAWhcMr0lU-9jNL9ndvbbU3pPluQ
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

### Docker and Travis CI
- https://medium.com/@audretschjames/understanding-docker-as-if-it-were-a-gameboy-96c96392efbf
- https://docs.docker.com/samples/library/postgres/
- https://linuxhint.com/run_postgresql_docker_compose/
- https://medium.com/@hmajid2301/implementing-sqlalchemy-with-docker-cb223a8296de
- https://www.smartfile.com/blog/testing-python-with-travis-ci/