FROM python:3.8

WORKDIR /code

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN pip install poetry==1.1.4
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

EXPOSE 5000

ENV PYTHONPATH $PYTHONPATH:/code
RUN which pip
RUN which python
CMD python todo_list_api/api.py
