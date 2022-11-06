import requests


def get_content_type(url):
    response = requests.get(url)
    if response:
        return response.headers['Content-Type']
    else:
        raise RuntimeWarning

