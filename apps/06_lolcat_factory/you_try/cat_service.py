import os
import shutil

import requests


def get_cat(output_dir, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_image(output_dir, name, data)


def get_data_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw


def save_image(directory, name, data):
    file_name = os.path.join(directory, name + '.jpg')
    with open(file_name, 'wb') as file:
        shutil.copyfileobj(data, file)
