import socket
import folium
import json

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def get_hostname():
    hostname = socket.gethostname()
    return hostname

def map_loads():  
    with open('static\\okresy-edit.json', encoding='utf-8') as myfile:
        data = myfile.read()
    vis2 = json.loads(data)
    # url = (
    #     "http://download.freemap.sk/AdminLevel"
    # )

    # print(url)

    # #vis1 = json.loads(requests.get(f"{url}/okresy.json").text)
    # #vis2 = json.loads(requests.get(f"{url}/okresy-005.json").text)
    # #http://download.freemap.sk/AdminLevel/kraje.json

    m = folium.Map(location=[49.0, 19.5],
                    zoom_start=8, width='100%', height='85%')
    #folium.GeoJson(vis1, name="geojson").add_to(m)
    folium.GeoJson(vis2, name="geojson").add_to(m)
    m.save('templates/map.html')
    return