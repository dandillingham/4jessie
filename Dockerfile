#docker build -t my-app .
#docker run --rm -p 8080:8080 my-app

FROM ubuntu 

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN pip3 install flask 

COPY . /
WORKDIR /

EXPOSE 8080

CMD ["python3","my-form.py"]
