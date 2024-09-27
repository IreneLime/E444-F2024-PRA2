FROM python:3.12-alpine

#Set up work directory
WORKDIR /home

#Copy everything from here to image
COPY . /home

# Set up the environment
RUN python -m venv venv
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Run hello.py
ENV FLASK_APP=hello.py
CMD ["flask", "run", "--host=0.0.0.0"]
