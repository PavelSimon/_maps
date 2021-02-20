#import requests
import time
from typing import Optional
import folium
import json
import uvicorn
from devtools import debug  # výpis premenný do promptu
from fastapi import FastAPI, Form, Request
# from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# import requests
import modules.netfunctions as netf
from config import HOST, PORT

moje_meno = netf.get_hostname()
moje_ip = netf.get_ip()
print('It is', moje_meno, 'My IP address:', moje_ip)

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="./templates")

netf.map_loads()

# Routes:


@app.get("/")
async def root(request: Request):
    """
    Ukáže zoznam zaevidovaných kryptomien
    """

    localtime = time.asctime(time.localtime(time.time()))
    print("/; Čas:", localtime)
    return templates.TemplateResponse("home.html", {"request": request, "time": localtime})


@app.get("/mapa")
async def mapa():
    url = (
        "http://download.freemap.sk/AdminLevel"
    )

    print(url)

    vis1 = json.loads(requests.get(f"{url}/okresy.json").text)
    # http://download.freemap.sk/AdminLevel/kraje.json

    m = folium.Map(location=[49.0, 19.5], zoom_start=7)
    #folium.GeoJson(vis1, name="geojson").add_to(m)
    m.save('static/map.html')
    return m._repr_html_()

# Code for running app
if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST,
                port=int(PORT), reload=True, debug=True)
