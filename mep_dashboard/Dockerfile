FROM docker.bank.swissquote.ch/itexploit/python:3.6

ARG projectFinalName
ARG pip_index_url
MAINTAINER it.operations@swissquote.ch

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV FLASK_APP run.py
ENV FLASK_DEBUG 1

#ADD target/${projectFinalName}  /app
COPY ./src/app /app

WORKDIR /app
#RUN pip3 install -i ${pip_index_url} -r requirements.txt
RUN pip3 install -i https://nexus.bank.swissquote.ch/repository/pypi/simple -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["flask"]
CMD ["run","-h", "0.0.0.0"]