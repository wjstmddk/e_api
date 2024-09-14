from fastapi import FastAPI, Response
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from typing import List
import os
import uvicorn
from pydantic import BaseModel
from db.database import enginconn
from db.models import Test

enginee=enginconn()
app=FastAPI()
session=enginee.sessionmaker()

class Data(BaseModel):
    id: int
    connect_status: int
    
class inputdata(BaseModel):
    connect_status: int

origins=[
    "http://localhost",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

def db_data():
    result=session.query(Test.id, Test.connect_status).all()
    data=[ Data(id=row[0],connect_status=row[1]) for row in result]
    return data

@app.get("/")
async def root():
    return  RedirectResponse(url="http://localhost:80")

@app.get("/data", response_model=List[Data])
async def dbdata():
    data=db_data()
    print("data send", data)
    return data

@app.post("/getdata")
async def receive_data(inputdata:inputdata):
    print(inputdata)
    data=Test(connect_status=inputdata.connect_status)
    session.add(data)
    session.commit()
    session.close()
    return {"message": "Data received", "data": inputdata}

# if __name__=="__main__":
#     uvicorn.run(app,host="127.0.0.1",port=80)