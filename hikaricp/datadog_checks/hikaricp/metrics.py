METRIC_MAP = {
    ## Micrometer Metrics
    "hikaricp_connections": "connections",
    "hikaricp_connections_active": "connections.active",
    "hikaricp_connections_idle": "connections.idle",
    "hikaricp_connections_max": "connections.max",
    "hikaricp_connections_pending": "connections.pending",
    "hikaricp_connections_timeout": "connections.timeout",
    "hikaricp_connections_acquire_seconds": "connections.acquire.seconds",
    "hikaricp_connections_acquire_seconds_max": "connections.acquire.seconds.max",
    "hikaricp_connections_acquire_seconds_sum": "connections.acquire.seconds.sum",
    "hikaricp_connections_creation_seconds": "connections.creation.seconds",
    "hikaricp_connections_creation_seconds_max": "connections.creation.seconds.max",
    "hikaricp_connections_creation_seconds_sum": "connections.creation.seconds.sum",
    "hikaricp_connections_usage_seconds": "connections.usage.seconds",
    "hikaricp_connections_usage_seconds_max": "connections.usage.seconds.max",
    "hikaricp_connections_usage_seconds_sum": "connections.usage.seconds.sum",

    ## Additional Prometheus Metrics
    "hikaricp_active_connections": "connections.active",
    "hikaricp_idle_connections": "connections.idle",
    "hikaricp_max_connections": "connections.max",
    "hikaricp_min_connections": "connections.min",
    "hikaricp_pending_threads": "threads.pending",
    "hikaricp_connection_timeout": "connections.timeout",
    "hikaricp_connection_acquired_nanos": "connections.acquired.nanos",
    "hikaricp_connection_creation_millis": "connections.creation.millis",
    "hikaricp_connection_usage_millis": "connections.usage.millis",
}
