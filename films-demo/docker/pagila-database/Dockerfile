FROM postgres

ENV POSTGRES_DB pagila
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD admin

COPY *.sh /docker-entrypoint-initdb.d/
COPY *.sql /docker-entrypoint-initdb.d/dump/

EXPOSE 5432
CMD ["postgres"]
