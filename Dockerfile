FROM python:3.8

COPY . /AWSS3

WORKDIR /AWSS3

RUN pip3 install -r requirements.txt

EXPOSE 80

CMD [ "python3", "app.py","--host=0.0.0.0" ]