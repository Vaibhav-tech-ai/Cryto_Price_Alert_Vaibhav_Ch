from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import logging
import uvicorn
from typing import Optional
from pymongo import MongoClient
from functions import *

app= FastAPI()
@app.get('/')
def index():
    return {'message':'hello'}

@app.post('/alerts/create/')
def create(
    uname: str = Form(...),
    name: str = Form(...),
    price: int= Form(...),
    crypto: str= Form(...)):

    uname = uname
    price = price
    crypto = crypto
    status= "created"

    doCreate(uname=uname, name=name, price=price, crypto=crypto, status=status)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Inserted successfully",
        }
    )

@app.post('/alerts/delete/')
def delete(
    uname: str = Form(...),
    price: int = Form(...),
    crypto: str = Form(...)):

    response=doDelete(uname=uname,crypto=crypto, price=price)

    if response:
        return JSONResponse(
        status_code=200,
        content={
            "message": "Deleted the Alert",
        }
    )
    else:
        return JSONResponse(
            status_code=404,
            content={
                "message":"error in deleting"
            }
        )

if __name__ == "__main__":
    uvicorn.run(
        app,
        port=5000,
        host="127.0.0.1",
    )

