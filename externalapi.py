from os import uname
from time import time
import requests
from pymongo import MongoClient
from time import sleep

client=MongoClient("mongodb+srv://test:test@cluster0.bquy3.mongodb.net/?retryWrites=true&w=majority")
db=client.get_database('Krypto')
users_collection=db.User
alert_collection = db.Alert


def getPriceData():
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    dictionary_crypto = response.json()
    symbol_price_dict = {}
    for x in dictionary_crypto:
        symbol_price_dict[x["symbol"]] = x["current_price"]
    return symbol_price_dict

def getAlerts():
    alerts_list = []

    response = alert_collection.find({"status": "created"})
    for each_query in response:
        tup = (each_query["uname"],each_query["crypto"], each_query["price"])
        alerts_list.append(tup)
    
    return alerts_list

def updateAlert(uname, crypto, price):
    filter = {
        "uname": uname,
        "crypto": crypto,
        "price": price
    }
    new_value = {"$set":{"status": "triggered"}}
    document = alert_collection.update_one(filter, new_value)

if __name__ == "__main__":
    threshold = 100
    while True:
        symbol_price_dict = getPriceData()
        alerts_list = getAlerts()

        for alert in alerts_list:
            current_price = symbol_price_dict[alert[1].lower()]
            lower_range  = current_price - threshold
            higher_range = current_price + threshold

            if alert[2] > lower_range and alert[2]< higher_range:
                #trigger 
                print(f"Triggered!! {alert[0]} SYMBOL: {alert[1]}  CURRENT PRICE: {current_price} TARGET: {alert[2]}")
                updateAlert(alert[0], alert[1], alert[2])
            else:
                continue
        
        print("Sleeping for sometime and going to next iteration")
        sleep(5)