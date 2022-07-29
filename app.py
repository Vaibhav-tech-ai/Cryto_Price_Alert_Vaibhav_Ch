from http.client import HTTPException
from fastapi import FastAPI, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import logging
import uvicorn
from typing import Optional
from pymongo import MongoClient
from functions import *
from fastapi_jwt_auth import AuthJWT


class Settings(BaseModel):
    authjwt_secret_key:str='443ba904fe89fb986cac2dda3aeabca97de87fa2e4282c329e85eff505449e94'


@AuthJWT.load_config
def get_config():
    return Settings()

app= FastAPI()


@app.get('/')
def index():
    return {'message':'hello'}

@app.post('/alerts/create/')
def create(
    uname: str = Form(...),
    name: str = Form(...),
    price: int= Form(...),
    crypto: str= Form(...),
    Authorize:AuthJWT=Depends()):

    uname = uname
    price = price
    crypto = crypto
    status= "created"

    doCreate(uname=uname, name=name, price=price, crypto=crypto, status=status)

    if searchDb(uname) == False:
        access_token=Authorize.create_access_token(subject=uname)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Created Succesfully"
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

@app.post('/alerts/fetch/')
def fetch(
    uname: str = Form(...),
    status: Optional[str]  = Form(None)):
    response= doFetch(uname=uname,status=status)
    if response:
        return JSONResponse(
            status_code=200,
            content={
                "result": response
            }
        )
    else:
        return JSONResponse(
            status_code=200,
            content={
                "result": "No Alerts of this kind is available"
            }
        )

if __name__ == "__main__":
    uvicorn.run(
        app,
        port=5000,
        host="127.0.0.1",
    )

