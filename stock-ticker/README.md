# Hazelcast Flow Stock-Ticker Demo 

This repo contains services required for the Hazelcast Flow stock-ticker demo.

This demo includes an example Taxi project which reads events from a Kafka topic
and shows how data policies can be used to control access to data in the stream
based on the User's Role.

Flow is configured with an Identity Provider in this demo.  The Identity Provider
is Hazelcast Management Center which is configured with these users:


| User       | Role        | Description                      |
|------------|-------------|----------------------------------|
| admin      | Full access | Full access to all features      |
| user       | readwrite   | Read and write access            |
| readonly   | readonly    | Read-only access                 |
| metrics    | metricsonly | Access to metrics only           |

The password for each user is `changeme!`.

## Data Access Policies
The taxi project includes some example Data Access Policies, which are useful for controlling access to data in the stream based on the User's Role.
These can be viewed in the UI under "Policies".

The following Data Access Policies are included in the project:

| Policy Name          | Description                                                   |
|----------------------|---------------------------------------------------------------|
| RestrictedStockTrade | Sets the price field to null when Admin role not present      |
| FilterTicker         | Obfuscates the Ticker symbol when Admin role not present      |



## Prerequisites

To use these files, you must first have the following installed:

- [Docker](https://docs.docker.com/engine/installation/)
- [docker-compose](https://docs.docker.com/compose/install/)

## How to use

The following steps will run a local instance of the Hazelcast Flow using the default configuration file (`docker-compose.yml`):

1. Clone this repository.
2. Change directory into the root of the project.
3. Set up the Hazelcast License
```bash
cp .env.example .env
```

> **⚠️ Important**
> You must create the file .env and populate it with the license information:
>   - MC_LICENSE contains the Hazelcast license
>   - MC_APPLICATION_CLIENT_SECRET contains the credentials for Flow API consumers to retrieve
>     authentication tokens for the OAuth Client Credentials Flow.

4. Run the `docker-compose up` command.

```bash
git clone https://github.com/hazelcast/hazelcast-flow-public-demos.git
cd hazelcast-flow-public-demos/stock-ticker

docker-compose up -d
```


Some exposed endpoints:
- http://localhost:9021 - Hazelcast Flow UI
- http://localhost:8080 - Management Center UI
