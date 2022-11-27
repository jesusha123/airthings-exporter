import argparse
import time
from prometheus_client import start_http_server, REGISTRY
from airthings.CloudCollector import CloudCollector

parser = argparse.ArgumentParser(
    prog='airthings-exporter',
    description='Prometheus exporter for Airthings devices')
parser.add_argument('--client-id')
parser.add_argument('--client-secret')
parser.add_argument('--device-id')
args = parser.parse_args()

REGISTRY.register(CloudCollector(args.client_id, args.client_secret, args.device_id))


def main():
    start_http_server(8000)
    print('Now listening on port 8000')
    while True:
        time.sleep(60)


if __name__ == '__main__':
    main()
