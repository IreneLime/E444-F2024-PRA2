FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN apt-get update && apt-get install -y python3.12-venv python3-pip-whl python3-setuptools-whl
RUN python3 -m venv /home/demo/venv

ADD requirements.txt /home/demo

RUN /home/demo/venv/bin/pip install -r /home/demo/requirements.txt

ADD templates /home/demo/
ADD hello.py /home/demo/

CMD ["/home/demo/venv/bin/python3 /home/demo/hello.py"]

ENTRYPOINT ["/bin/bash", "-c"]