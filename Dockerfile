FROM  python:3.6   
# what image we want to use to run this container

# Installing only requirements first, into tmp directory, so this process 
# is cached properly whenever another file changes
COPY ./src/requirements.txt /tmp

# Install Requirements
RUN pip install -r /tmp/requirements.txt 

# Assigning working directory (cd app) this directory was hosted by docker-compose from src folder
WORKDIR /app   

# Expose flask's port
EXPOSE 5000

# Run the server
CMD python server.py 

# Docker and docker-compose learned here: 
# https://medium.com/@audretschjames/understanding-docker-as-if-it-were-a-gameboy-96c96392efbf