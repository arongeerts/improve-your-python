FROM python:3.7

WORKDIR /code

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN pip install poetry==1.1.4
RUN poetry install

COPY . .

EXPOSE 5000

ENV PYTHONPATH $PYTHONPATH:/code

CMD python todo_list_api/api.py
