## Kafka Kurulum

Install using Docker compose

```
docker-compose up -d
```

Get image name
```
docker ps
```

Create Kafka topic
```
docker-compose exec kafka kafka-topics --create \
  --topic <topic-name> \
  --bootstrap-server kafka:9092 \
  --partitions 3 \
  --replication-factor 1
```

Update Kafka topic
```
docker-compose exec kafka kafka-topics --alter \
  --topic <topic-name> \
  --partitions 5 \
  --bootstrap-server kafka:9092
```

To see topics
```
docker-compose exec kafka kafka-topics --bootstrap-server kafka:9092 --list
docker-compose exec kafka kafka-topics --describe --topic <topic-name>> --bootstrap-server kafka:9092
```

# Kafka Producer Configuration Reference

This table lists **all key Kafka Producer settings**, their English explanations, and possible values. Useful for `kafka-python` or general Kafka producers.

| Setting | Description | Possible Values / Default |
|---------|-------------|---------------------------|
| `bootstrap_servers` | Kafka broker addresses to connect to | List of host:port strings, e.g., `["kafka:9092"]` |
| `acks` | Determines how many broker acknowledgements the producer requires before considering a request complete | `'all'` / `'1'` / `'0'` (default `'1'`) |
| `compression_type` | Compression for messages to reduce network load | `'gzip'`, `'snappy'`, `'lz4'`, `'zstd'`, or `None` |
| `retries` | Number of retry attempts if send fails | Integer ≥ 0 (default `0`) |
| `retry_backoff_ms` | Wait time between retries | Milliseconds (default `100`) |
| `linger_ms` | Delay to wait before sending a batch of messages (for batching) | Milliseconds (default `0`) |
| `batch_size` | Maximum batch size in bytes for a single partition | Bytes (default `16384`) |
| `buffer_memory` | Total memory for buffering messages waiting to be sent | Bytes (default `33554432` = 32 MB) |
| `max_in_flight_requests_per_connection` | Max number of unacknowledged requests the client will send on a single connection | Integer ≥ 1 (default `5`) |
| `client_id` | Optional identifier for the producer client | String (default `""`) |
| `key_serializer` | Function to serialize message keys | Python callable (default `None`) |
| `value_serializer` | Function to serialize message values | Python callable (default `None`) |
| `transactional_id` | ID for enabling transactions | String (default `None`) |
| `enable_idempotence` | Enable idempotent producer to avoid duplicate messages | `True` / `False` (default `False`) |
| `acks_for_idempotence` | Acks required when idempotence is enabled | Must be `'all'` |
| `request_timeout_ms` | Max time for broker to respond before failing | Milliseconds (default `30000`) |
| `metadata_max_age_ms` | Max age of metadata before refresh | Milliseconds (default `300000`) |
| `max_request_size` | Maximum size of a request sent to broker | Bytes (default `1048576` = 1 MB) |
| `delivery_timeout_ms` | Total time to deliver a message (including retries) | Milliseconds (default `120000`) |
| `linger_ms` | Time to wait before sending a batch | Milliseconds (default `0`) |
| `max_block_ms` | Max time producer.send() will block if buffer is full | Milliseconds (default `60000`) |
| `interceptor_classes` | List of producer interceptor classes | List of strings (default `[]`) |
| `security_protocol` | Protocol for broker connection | `'PLAINTEXT'`, `'SSL'`, `'SASL_PLAINTEXT'`, `'SASL_SSL'` (default `'PLAINTEXT'`) |
| `ssl_cafile` | Path to CA certificate | File path |
| `ssl_certfile` | Path to client certificate | File path |
| `ssl_keyfile` | Path to client private key | File path |
| `ssl_check_hostname` | Whether to verify broker hostname in SSL cert | `True` / `False` |
| `sasl_mechanism` | SASL mechanism for authentication | `'PLAIN'`, `'SCRAM-SHA-256'`, `'SCRAM-SHA-512'`, `'GSSAPI'`, `'OAUTHBEARER'` |
| `sasl_plain_username` | Username for SASL/PLAIN | String |
| `sasl_plain_password` | Password for SASL/PLAIN | String |
| `max_block_ms` | Max time for `send()` to block when buffer is full | Milliseconds (default `60000`) |
| `api_version` | Kafka API version to use | Tuple `(major, minor, patch)` or `'auto'` |
| `linger_ms` | Time to wait before sending batch | Milliseconds (default `0`) |
| `reconnect_backoff_ms` | Wait time before reconnecting to broker | Milliseconds (default `50`) |
| `reconnect_backoff_max_ms` | Max wait time for reconnect | Milliseconds (default `1000`) |
| `request_timeout_ms` | Max time to wait for broker response | Milliseconds (default `30000`) |

> **Tip:** For most use cases, the essential settings are: `bootstrap_servers`, `acks`, `retries`, `batch_size`, `linger_ms`, `value_serializer`. The rest are for fine-tuning reliability, batching, security, or transactional behavior.

# Kafka Consumer Configuration Reference

This table lists **all key Kafka Consumer settings**, their English explanations, and possible values. Useful for `kafka-python` or general Kafka consumers.

| Setting | Description | Possible Values / Default |
|---------|-------------|---------------------------|
| `bootstrap_servers` | Kafka broker addresses to connect to | List of host:port strings, e.g., `["kafka:9092"]` |
| `group_id` | Consumer group identifier | String (required for group management) |
| `auto_offset_reset` | What to do when no offset is found for a partition | `'earliest'`, `'latest'`, `'none'` (default `'latest'`) |
| `enable_auto_commit` | Whether to automatically commit offsets | `True` / `False` (default `True`) |
| `auto_commit_interval_ms` | Interval between automatic offset commits | Milliseconds (default `5000`) |
| `session_timeout_ms` | Timeout for consumer group session | Milliseconds (default `10000`) |
| `heartbeat_interval_ms` | Interval for sending heartbeat to broker | Milliseconds (default `3000`) |
| `fetch_min_bytes` | Minimum bytes to fetch from broker in a single request | Bytes (default `1`) |
| `fetch_max_bytes` | Max bytes per fetch request | Bytes (default `52428800` = 50 MB) |
| `fetch_max_wait_ms` | Max wait time if `fetch_min_bytes` not met | Milliseconds (default `500`) |
| `max_partition_fetch_bytes` | Max bytes per partition per fetch | Bytes (default `1048576` = 1 MB) |
| `consumer_timeout_ms` | Timeout for blocking `for message in consumer` | Milliseconds (default `None`) |
| `value_deserializer` | Function to deserialize message values | Python callable (default `None`) |
| `key_deserializer` | Function to deserialize message keys | Python callable (default `None`) |
| `client_id` | Identifier for consumer client | String (default `""`) |
| `max_poll_records` | Max records returned in a single poll | Integer ≥ 1 (default `500`) |
| `max_poll_interval_ms` | Max interval between calls to `poll()` | Milliseconds (default `300000`) |
| `partition_assignment_strategy` | Strategy for partition assignment in a group | `'Range'`, `'RoundRobin'`, `'StickyAssignor'` (default `'Range'`) |
| `isolation_level` | Reads committed or uncommitted messages | `'read_committed'`, `'read_uncommitted'` (default `'read_uncommitted'`) |
| `connections_max_idle_ms` | Max idle time for broker connections | Milliseconds (default `540000`) |
| `security_protocol` | Protocol for broker connection | `'PLAINTEXT'`, `'SSL'`, `'SASL_PLAINTEXT'`, `'SASL_SSL'` (default `'PLAINTEXT'`) |
| `ssl_cafile` | Path to CA certificate | File path |
| `ssl_certfile` | Path to client certificate | File path |
| `ssl_keyfile` | Path to client private key | File path |
| `ssl_check_hostname` | Verify broker hostname in SSL certificate | `True` / `False` |
| `sasl_mechanism` | SASL mechanism for authentication | `'PLAIN'`, `'SCRAM-SHA-256'`, `'SCRAM-SHA-512'`, `'GSSAPI'`, `'OAUTHBEARER'` |
| `sasl_plain_username` | Username for SASL/PLAIN | String |
| `sasl_plain_password` | Password for SASL/PLAIN | String |
| `api_version` | Kafka API version to use | Tuple `(major, minor, patch)` or `'auto'` |
| `request_timeout_ms` | Max time to wait for broker response | Milliseconds (default `40000`) |
| `retry_backoff_ms` | Wait time before retrying failed requests | Milliseconds (default `100`) |

> **Tip:** For most applications, the essential settings are: `bootstrap_servers`, `group_id`, `auto_offset_reset`, `enable_auto_commit`, and `value_deserializer`. The rest are for fine-tuning performance, reliability, or security.



# Kafka Docker Compose Environment Variables

| Variable | Description | Typical Production Value | Notes |
|----------|-------------|--------------------------|-------|
| KAFKA_BROKER_ID | Unique ID for the broker in the Kafka cluster | 1, 2, 3… | Must be unique per broker |
| KAFKA_ZOOKEEPER_CONNECT | Zookeeper connection string | zookeeper:2181 | For single-node: zookeeper:2181; for HA: zk1:2181,zk2:2181,… |
| KAFKA_LISTENERS | Comma-separated list of listeners the broker binds to | PLAINTEXT://0.0.0.0:9092 | Can add SSL/SASL listeners for security |
| KAFKA_ADVERTISED_LISTENERS | How the broker advertises itself to clients | PLAINTEXT://kafka:9092 | In prod often uses hostname/FQDN reachable from outside |
| KAFKA_LISTENER_SECURITY_PROTOCOL_MAP | Maps listener names to security protocols | PLAINTEXT:PLAINTEXT | Use SSL or SASL for security in prod |
| KAFKA_INTER_BROKER_LISTENER_NAME | Listener for broker-to-broker communication | PLAINTEXT | Usually same as a secured listener in prod |
| KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR | Replication factor for internal topics (__consumer_offsets, __transaction_state) | 3 | Prod: >1 for fault tolerance, default 1 in local Docker setups |
| KAFKA_NUM_PARTITIONS | Default number of partitions for new topics | 12–24 | Production topics usually have multiple partitions for parallelism |
| KAFKA_AUTO_CREATE_TOPICS_ENABLE | Enable auto-creation of topics | false | Recommended false in prod to avoid accidental topics |
| KAFKA_MIN_INSYNC_REPLICAS | Minimum ISR (in-sync replicas) for producing messages | 2 | Prod: ≥2 to guarantee durability |
| KAFKA_DEFAULT_REPLICATION_FACTOR | Default replication factor for new topics | 3 | Prod: ≥3 for high availability |
| KAFKA_LOG_RETENTION_HOURS | How long messages are retained | 168 (7 days) | Can be days/weeks depending on storage |
| KAFKA_LOG_RETENTION_BYTES | Max size per partition | Unlimited or per disk quota | Controls retention by size instead of time |
| KAFKA_MESSAGE_MAX_BYTES | Max message size accepted | 1000012 | Increase if sending large payloads |
| KAFKA_REPLICA_FETCH_MAX_BYTES | Max bytes a follower fetches per request | 1048576 | Increase for large messages/partitions |
| KAFKA_DEFAULT_REPLICATION_FACTOR | Default replication factor for new topics | 3 | Usually equal to number of brokers in prod cluster |
| KAFKA_DELETE_TOPIC_ENABLE | Allow deletion of topics | true | Should be true if you need topic deletion; false blocks deletion |
| KAFKA_AUTO_LEADER_REBALANCE_ENABLE | Auto leader election | true | Helps balance partitions among brokers |
| KAFKA_CONFLUENT_SUPPORT_METRICS_ENABLE | Confluent-specific metrics | false | Usually false if not using Confluent monitoring |
