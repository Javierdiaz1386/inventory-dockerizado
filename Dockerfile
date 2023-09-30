FROM python:3.11

RUN mkdir -p /home/app

WORKDIR /home/app

COPY . /home/app

EXPOSE 8000

RUN pip install -r /home/app/requirements.txt

RUN cd /home/app 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]  