FROM python:3.6
EXPOSE 8000

ADD ./randomapp randomapp 
WORKDIR /randomapp

RUN pip install -r /randomapp/requirements.txt
CMD [ "python", "/randomapp/manage.py", "runserver", "0.0.0.0:8000"]