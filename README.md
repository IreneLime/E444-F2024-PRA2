Flasky
======

This repository is forked from https://github.com/miguelgrinberg/flasky


Run Instruction:

(venv) $ set FLASK_APP=hello.py

(venv) $ flask run

Run on: http://127.0.0.1:5000

To build and run docker:

docker build -t flask-sample:latest .

docker run -d -p 5000:5000 flask-sample
