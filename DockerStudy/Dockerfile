ARG UBUNTU_VERSION="20.04"

FROM ubuntu:${UBUNTU_VERSION} as builder-image
ARG PYTHON_VERSION="3.8"

ENV TZ=Asia/Kolkata \
    DEBIAN_FRONTEND=noninteractiv
    
WORKDIR /project
COPY src/ .
COPY requirements.txt .

RUN apt-get update 
RUN apt-get install --no-install-recommends -qqy 
RUN apt-get install -y python3-pip 
RUN apt-get install python${PYTHON_VERSION}-dev 
RUN apt-get install -y libpq-dev
RUN apt-get install -y postgresql postgresql-contrib

RUN pip3 install -r requirements.txt 
CMD ["python3", "manage.py", "migrate"]
CMD ["service","postgresql","start"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:3000"]
