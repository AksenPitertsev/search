import json

def get_spn(toponym: json) -> str:
    values = toponym.get("boundedBy").get("Envelope").values()
    x1, y1 = map(float, next(values).split())
    x2, y2 = map(float, next(values).split())
    return f"{x2 - x1}, {y2 - y1}"


def get_ll(toponym: json) -> str:
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    return ",".join([toponym_longitude, toponym_lattitude])
