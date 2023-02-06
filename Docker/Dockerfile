FROM debian:bullseye-slim

RUN apt-get update -y && apt-get install -y curl python3 python3-pip python3-dev wget
RUN ln -s /usr/bin/python3 /usr/bin/python

COPY requirements.txt /tmp/

RUN pip3 install --upgrade pip
RUN pip3 install --requirement /tmp/requirements.txt

RUN apt-get clean
RUN pip3 cache remove purge

EXPOSE 8888

RUN mkdir -p /workspace
WORKDIR /workspace
CMD jupyter lab --ip=0.0.0.0 --port=8899 --no-browser --allow-root --NotebookApp.token=