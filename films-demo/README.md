# Hazelcast Flow Films Demo 

This repo contains services required for the Hazelcast Flow films demo

Specifically:
 * A database containing films
 * A Rest API containing listings, telling us where we can watch these films
 * A Kafka topic, that tells use when new releases are announced

This demo is "naked" - the services don't contain any Flow or Taxi code or concepts.

Throughout the demo, services and data sources are imported through the UI, and then edited in the UI to add semantic data.

## Prerequisites

To use these files, you must first have the following installed:

- [Docker](https://docs.docker.com/engine/installation/)
- [docker-compose](https://docs.docker.com/compose/install/)

## How to use

The following steps will run a local instance of the Hazelcast Flow using the default configuration file (`docker-compose.yml`):

1. Clone this repository.
2. Change directory into the root of the project.
3. Set up the Hazelcast Flow License
```bash
cp .env.example .env
```

> **⚠️ Important**
> You must create the file .env and populate it with the license information:
>   - MC_LICENSE contains the Hazelcast Flow license

4. Run the `docker compose up` command.

```bash
docker compose up -d
```

Some exposed endpoints:
- http://localhost:9021 - Hazelcast Flow UI
- http://localhost:8080 - Management Center UI

For further instructions and guidelines, please refer to the [Flow Documentation](https://docs.hazelcast.com/flow/5.5/guides/apis-db-kafka).