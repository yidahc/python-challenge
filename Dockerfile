FROM  python:3.6   
# what image we want to use to run this container

# Installing only requirements first, into tmp directory, so this process 
# is cached properly whenever another file changes
COPY requirements.txt /tmp

# Install Requirements
RUN pip install -r /tmp/requirements.txt 

# Opening and assigning working directory (like cd app) this directory was hosted by docker-compose from src folder
WORKDIR /app

# Expose flask's port
EXPOSE 5000
# in docker container this will run on port 5000 with ip address docker assigns it (ip address can be referenced by name of container)

# Run the server
CMD python server.py 
