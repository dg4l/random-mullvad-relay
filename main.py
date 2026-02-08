#!/bin/python3
from random import randint
import requests
import pprint 
import json

url = "https://api.mullvad.net/public/relays/wireguard/v1"

def get_allowed_relays(cities):
    ret = []
    relays = []
    for city in cities:
        for relay in city["relays"]:
            relays.append(relay)
    return [relay["hostname"] for relay in relays]

def get_allowed_cities(countries):
    ret = []
    allowed_countries = ["USA", "Canada"]
    for country in countries:
        if country["name"].lower() in [allowed.lower() for allowed in allowed_countries]:
            cities = country["cities"]
            for city in cities:
                ret.append(city)
    return ret

def main():
    response = requests.get(url)
    response_json = response.json()
    countries = response_json["countries"]
    cities = get_allowed_cities(countries)
    allowed_relays = get_allowed_relays(cities)
    random_relay_idx = randint(0, len(allowed_relays))
    chosen_relay = allowed_relays[random_relay_idx]
    print(chosen_relay)

if __name__ == "__main__":
    main()
