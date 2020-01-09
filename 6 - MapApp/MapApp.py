# gazstao 2019-11-16 20h

import folium
from geopy.geocoders import ArcGIS
from datetime import datetime

endereco = "Vicente Spisla, 238, Curitiba"
alcance = 11
escala = 250
zoom = 15

coordenadas = ArcGIS()
local = coordenadas.geocode(endereco)

fg = folium.FeatureGroup(name="Aztech LABS")
fg.add_child(folium.Marker(location = [local.latitude,local.longitude], popup="AztechLABS CWB!", icon = folium.Icon(color="green")))
#fg.add_child(folium.RegularPolygonMarker(location = [local.latitude,local.longitude], popup="AztechLABS CWB!", icon = folium.Icon(color="green")))
#fg.add_child(folium.CircleMarker(location = [local.latitude,local.longitude], popup="AztechLABS CWB!", icon = folium.Icon(color="green")))
#fg.add_child(folium.Marker(location = [local.latitude,local.longitude], popup="AztechLABS CWB!", icon = folium.Icon(color="green")))

latstart = local.latitude-(alcance/escala)/2
lonstart = local.longitude-(alcance/escala)/2


for longitude in range(alcance):
    for latitude in range(alcance):
        lat = latstart+latitude/escala
        lon = lonstart+longitude/escala      
        if not ( local.latitude == lat and local.longitude == lon):
            fg.add_child(folium.Circle(location = [lat,lon],popup = "{} {}".format(lat,lon),radius=5))

#map = folium.Map(location = [local.latitude, local.longitude], zoom_start="16", tiles="Stamen Terrain", max_zoom=16)
map = folium.Map(location = [local.latitude, local.longitude], zoom_start=zoom)
map.add_child(fg)
map.save("/Users/gazstao/Documents/Curso Python/6 - MapApp/Mapa.html")

now = datetime.now()
print("\n\nGazstao 2019-11-16 MapApp from Udemy Python - agora: {}h{}m{}s".format(now.hour, now.minute, now.second))
print("@ {} , {}\n".format(local.latitude,local.longitude))