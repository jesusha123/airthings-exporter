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
# Start server
airthings-exporter --client-id [client_id] --client-secret [client_secret] --device-id [device_id]

# Test server works
curl -s localhost:8000
```

## Tested Devices

- Airthings View Plus
