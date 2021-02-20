import requests
import time
from typing import Optional
import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import modules.netfunctions as netf
from config import HOST, PORT

moje_meno = netf.get_hostname()
moje_ip = netf.get_ip()
print('It is', moje_meno, 'My IP address:', moje_ip)

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="./templates")

#netf.map_loads("sk")

# Routes:


@app.get("/")
async def root(request: Request):
    """
    Ukáže zoznam zaevidovaných kryptomien
    """
    netf.map_loads("sk")
    localtime = time.asctime(time.localtime(time.time()))
    print("/; Čas:", localtime)
    return templates.TemplateResponse("home.html", {"request": request, "time": localtime})

@app.get("/kraj")
async def kraj(request: Request):
    """
    Ukáže zoznam zaevidovaných kryptomien
    """
    netf.map_loads("kraj")

    localtime = time.asctime(time.localtime(time.time()))
    print("/kraj; Čas:", localtime)
    return templates.TemplateResponse("home.html", {"request": request, "time": localtime})

@app.get("/okres")
async def kraj(request: Request):
    """
    Ukáže zoznam zaevidovaných kryptomien
    """
    netf.map_loads("okres")

    localtime = time.asctime(time.localtime(time.time()))
    print("/okres; Čas:", localtime)
    return templates.TemplateResponse("home.html", {"request": request, "time": localtime})

# Code for running app
if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST,
                port=int(PORT), reload=True, debug=True)
