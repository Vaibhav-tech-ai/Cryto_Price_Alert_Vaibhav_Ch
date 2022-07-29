from fastapi import Query
from pymongo import MongoClient

client=MongoClient("mongodb+srv://test:test@cluster0.bquy3.mongodb.net/?retryWrites=true&w=majority")
db=client.get_database('Krypto')
users_collection=db.User
alert_collection = db.Alert


def doCreate(uname, name, price, crypto,status):
    '''
    Already signed User --> Dont created the document again 
        Check run --> To find out if the user exists --> return that user alredy exist
    '''
    record={
        "uname": uname,
        "name": name
    }
    record_alert = {
        "uname": uname,
        "crypto": crypto,
        "price": price,
        "status": status
    }
    result=users_collection.insert_one(record)
    result_alert = alert_collection.insert_one(record_alert)

    # print(result)

def doDelete(uname,crypto,price):
    filter = {
        "uname": uname,
        "crypto": crypto,
        "price": price
    }
    new_value = {"$set":{"status": "deleted"}}
    document = alert_collection.update_one(filter, new_value)
    return 1

#print(create("vaibhav",20000,"BTC"))