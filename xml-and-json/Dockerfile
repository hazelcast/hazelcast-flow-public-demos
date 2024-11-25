FROM maven:3.9.9-amazoncorretto-21 AS builder

RUN mkdir -p /usr/src/films-xml
COPY films-xml /usr/src/films-xml

RUN mvn -f /usr/src/films-xml/pom.xml clean package

FROM eclipse-temurin:21-jammy

RUN addgroup --system worker --gid 1000 && \
    adduser --system worker --ingroup worker --uid 1001

RUN mkdir -p /opt/service/
RUN chown worker:worker /opt/service/

USER worker
WORKDIR /opt/service/

EXPOSE 80

HEALTHCHECK --interval=10s \
            --timeout=3s \
            --start-period=30s \
            CMD curl -s http://localhost/actuator/ping > /dev/null || exit 1

COPY --from=builder --chown=worker /usr/src/films-xml/target/appassembler /opt/service/

CMD $BEFORE_START_COMMAND && ./bin/films-xml --server.port=80 $OPTIONS
