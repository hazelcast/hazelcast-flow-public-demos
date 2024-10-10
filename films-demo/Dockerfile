FROM maven:3-amazoncorretto-23 AS builder

RUN mkdir -p /usr/src/online-listings-api
COPY online-listings-api /usr/src/online-listings-api/
COPY pom.xml /usr/src

RUN mvn -f /usr/src/pom.xml clean package

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

COPY --from=builder --chown=worker /usr/src/online-listings-api/target/appassembler /opt/service/

CMD $BEFORE_START_COMMAND && ./bin/online-listings-api --server.port=80 $OPTIONS
