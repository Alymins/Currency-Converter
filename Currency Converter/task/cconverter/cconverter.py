import requests
import json
import os

cache = ['usd', "eur"]
path = os.path.dirname(__file__)


def save_json(code: str):
    file_path = os.path.join(path, f'{code.lower()}.json')
    url = f"http://www.floatrates.com/daily/{code.lower()}.json"
    jason = requests.get(url).json()
    with open(file_path, "w") as file:
        json.dump(jason, file)
    return jason


def load_json(code: str):
    file_path = os.path.join(path, f'{code.lower()}.json')
    with open(file_path) as file:
        return json.load(file)


def menu():
    base_code = input()
    while True:
        exchange_code = input()
        if exchange_code:
            money = float(input())
            exchange = 0
            print("Checking the cache...")
            if exchange_code.lower() in cache:
                print("Oh! It is in the cache!")
                exchange = round(money * load_json(exchange_code)[base_code.lower()]["inverseRate"], 2)
            else:
                print("Sorry, but it is not in the cache!")
                exchange = round(money * save_json(exchange_code)[base_code.lower()]["inverseRate"], 2)
                cache.append(exchange_code.lower())
            print(f"You received {exchange} {exchange_code.upper()}.")
        else:
            break


menu()
