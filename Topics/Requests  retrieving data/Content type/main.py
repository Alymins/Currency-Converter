import requests


def get_content_type(url):
    return f"{requests.get(url).headers['content-type']}"



