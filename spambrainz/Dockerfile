ARG UBUNTU_VERSION=18.04

FROM ubuntu:${UBUNTU_VERSION} as base

ENV LANG C.UTF-8

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

RUN python3 -m pip --no-cache-dir install --upgrade \
    pip \
    setuptools

RUN ln -s $(which python3) /usr/local/bin/python

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements_docker.txt

EXPOSE 5000 

ENTRYPOINT ["python"]

CMD ["sb_api.py"]
