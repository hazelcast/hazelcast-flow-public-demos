# Hazelcast Flow Films XML Demo 

This repo contains services required for the Hazelcast Flow films XML demo

This features a Rest API providing information about films, actors in XML format

This demo is "naked" - the services don't contain any Flow or Taxi code or concepts.
The taxi files used for the demo are described in the [tutorial](https://docs.hazelcast.com/flow/5.5/guides/work-with-xml)

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

For further instructions and guidelines, please refer to the [Flow Documentation](https://docs.hazelcast.com/flow/5.5/guides/work-with-xml).
