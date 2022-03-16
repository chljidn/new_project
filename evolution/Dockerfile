FROM continuumio/miniconda3

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir /srv/evolution_project
ADD . /srv/evolution_project

# environment.yaml을 통해서 설치할 때, env 같이 쓸 것
RUN conda env create -f /srv/evolution_project/environment.yaml

# 환경변수 설정
ENV PATH /opt/conda/envs/evolution/bin:$PATH
ENV /bin/bash -c evolution
WORKDIR /srv/evolution_project



RUN pip install --upgrade pip
RUN pip install -r requirements.txt

