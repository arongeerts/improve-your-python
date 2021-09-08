FROM todo-api

COPY plugins/dynamodb .
RUN poetry install
