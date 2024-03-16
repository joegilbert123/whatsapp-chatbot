import requests


def make_request(url, method="get", *args, **kwargs):
    response = requests.request(url=url, method=method, *args, **kwargs)
    response.raise_for_status()
    return response.json()
