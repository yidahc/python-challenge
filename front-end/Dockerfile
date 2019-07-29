FROM  python:3.6 
  
COPY ./src/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt 

WORKDIR /app

EXPOSE 5432
CMD python server.py