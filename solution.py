import sys
from io import BytesIO
import requests
from PIL import Image

import geocoder

toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json",
}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    pass

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
delta = "0.005"

coords = geocoder.get_ll(toponym)
map_params = {
    "ll": coords,
    "spn": geocoder.get_spn(toponym),
    "l": "map",
    "pt": coords + ",pm2dirl",
}

# + ",pm2dir"

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()
