import requests as requests
from prometheus_client.metrics_core import GaugeMetricFamily
from prometheus_client.registry import Collector


class CloudCollector(Collector):
    def __init__(self, client_id, client_secret, device_id):
        self.client_id = client_id
        self.client_secret = client_secret
        self.device_id = device_id

    def collect(self):
        gauge_metric_family = GaugeMetricFamily('airthings_gauge', 'Airthings sensor values')
        data = self.__get_cloud_data__()
        self.__add_samples__(gauge_metric_family, data)
        yield gauge_metric_family

    def __add_samples__(self, gauge_metric_family, data):
        labels = {'device_id': self.device_id}
        if 'battery' in data:
            gauge_metric_family.add_sample('airthings_battery_percent', value=data['battery'], labels=labels)
        if 'co2' in data:
            gauge_metric_family.add_sample('airthings_co2_parts_per_million', value=data['co2'], labels=labels)
        if 'humidity' in data:
            gauge_metric_family.add_sample('airthings_humidity_percent', value=data['humidity'], labels=labels)
        if 'pm1' in data:
            gauge_metric_family.add_sample('airthings_pm1_micrograms_per_cubic_meter',
                                           value=float(data['pm1']),
                                           labels=labels)
        if 'pm25' in data:
            gauge_metric_family.add_sample('airthings_pm25_micrograms_per_cubic_meter',
                                           value=float(data['pm25']),
                                           labels=labels)
        if 'pressure' in data:
            gauge_metric_family.add_sample('airthings_pressure_hectopascals',
                                           value=float(data['pressure']),
                                           labels=labels)
        if 'radonShortTermAvg' in data:
            gauge_metric_family.add_sample('airthings_radon_short_term_average_becquerels_per_cubic_meter',
                                           value=float(data['radonShortTermAvg']),
                                           labels=labels)
        if 'temp' in data:
            gauge_metric_family.add_sample('airthings_temperature_celsius', value=data['temp'], labels=labels)
        if 'voc' in data:
            gauge_metric_family.add_sample('airthings_voc_parts_per_billion', value=data['voc'], labels=labels)

    def __get_cloud_data__(self):
        access_token = self.__get_access_token__()
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(
            f'https://ext-api.airthings.com/v1/devices/{self.device_id}/latest-samples',
            headers=headers)
        data = response.json()['data']
        return data

    def __get_access_token__(self):
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": "read:device:current_values"
        }
        token_response = requests.post(
            'https://accounts-api.airthings.com/v1/token',
            data=data)
        return token_response.json()['access_token']
