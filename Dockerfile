FROM python:3.7

WORKDIR /code
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV PYTHONPATH $PYTHONPATH:/code

CMD python todo_list_api/api.py
