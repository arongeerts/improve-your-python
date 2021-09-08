FROM todo-api

COPY plugins/mysql .
RUN poetry install
