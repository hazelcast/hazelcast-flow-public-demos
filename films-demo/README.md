# Hazelcast Flow Films Demo - Basic Services

This repo contains services required for the Hazelcast Flow films demo

Specifically:
 * A database containing films
 * A Rest API containing listings, telling us where we can watch these films
 * A Kafka topic, that tells use when new releases are announced

This demo is "naked" - the services don't contain any Flow or Taxi code or concepts.

Throughout the demo, services and data sources are imported through the UI, and then edited in the UI to add semantic data.

There are other ways to import data sources, not covered in this demo, such as:
 * Embedding metadata in OpenAPI and Protobuf specs
 * Publishing schemas directly to Hazelcast Flow (from applications)

These are covered in other demos.

