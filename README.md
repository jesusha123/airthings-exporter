# Airthings Exporter

Prometheus exporter for Airthings devices.

## Requirements

- Python 3
- Airthings device

## Setup

- Register your Airthings device to sync with the cloud following the instructions manual
- Check the Airthings app or the [web dashboard](https://dashboard.airthings.com) to obtain your device serial number. This is your client id
- Go to the [Airthings Integrations webpage](https://dashboard.airthings.com/integrations/api-integration) and request an API Client to obtain a client secret
- Install airthings-exporter
```shell
pip install airthings-exporter
```

## Usage

```shell
# Start server (1 device)
airthings-exporter --client-id [client_id] --client-secret [client_secret] --device-id [device_id]

# Start server (2 devices)
airthings-exporter --client-id [client_id] --client-secret [client_secret] --device-id [device_id_1] --device-id [device_id_2]

# Test server works
curl -s localhost:8000
```

## Tested Devices

- Airthings View Plus
- Airthings Wave Mini

## Example Prometheus configuration file (prometheus.yml)

```yml
scrape_configs:
  - job_name: 'airthings'
    scrape_interval: 5m
    scrape_timeout: 10s
    static_configs:
      - targets: ['localhost:8000']
```

## API limitations

Airthings API for consumers allows only up to 120 requests per hour. Every scrape in prometheus sends one request per device to the Airthings API. Make sure the configured prometheus scrape interval does not exceed the limit.
