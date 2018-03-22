FROM python:3.6

EXPOSE 8000
WORKDIR /randomapp
ADD ./entry_point.sh /entry_point.sh
RUN chmod +x /entry_point.sh
ADD ./randomapp /randomapp

RUN pip install -r /randomapp/requirements.txt \
    && pip install gunicorn

CMD [ "/entry_point.sh"]