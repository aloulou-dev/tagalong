""" Geoapify Connector: find the tourist attractions for the given city that the user inputs """

import requests

API_KEY = "6349f894db4e4bb595616daf7354f261"

GEOCODE_URL = "https://api.geoapify.com/v1/geocode/search"
PLACES_URL = "https://api.geoapify.com/v2/places"

def geocode_city(city):
    """ Turn a city name into a (lat, lon) coordinate from the user input """
    params = {"text": city, "limit" : 1, "apiKey": API_KEY}
    response = requests.get(GEOCODE_URL, params=params, timeout=10)
    response.raise_for_status()
    features = response.json()["features"]
    if not features:
        raise ValueError(f"Could not find a location for city: {city}")
    props = features[0]["properties"]
    print("WE are at", props["formatted"])
    return props["lat"], props["lon"], props["place_id"]


def get_attractions (city, limit = 10, radius =10000):
    """ returns list of attractions for the given city, limit is the number of results to return, radius is the search radius in meters """
    lat, lon, place_id = geocode_city(city)
    params = {"categories": "tourism.sights,entertainment.museum", "filter" : f"place:{place_id}", "bias": f"proximity:{lon},{lat}", "limit": limit, "apiKey": API_KEY,}
    response = requests.get(PLACES_URL, params=params, timeout=10)
    response.raise_for_status()
    features = response.json()["features"]
    attractions = []
    for feature in features:
        name = feature["properties"].get("name")
        if name:
            attractions.append(name)
    return attractions



if __name__ ==  "__main__":
    city = input("Enter a city: ")
    for name in get_attractions(city):
        print("-", name)


