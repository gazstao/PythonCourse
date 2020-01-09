# gazstao 2019-11-16 22h30

import mysql.connector
import folium
from geopy.geocoders import ArcGIS
from datetime import datetime
import webbrowser

enderecos = [ 
        ["Vicente Spisla, 238, Curitiba","AztechLABS","black"],
        ["Av Iguaçu, 1236, Curitiba","Sugisawa","blue"],
        [ "Arthur Bernardes, 1385, Curitiba","Trabalho Lindsey" , "orange"],
        [ "Augusto Stelfeld, 1727, Curitiba","Cermen","blue"],
        ["Sao Jose Calazans, 100, Curitiba","Consuelo", "green"],
        ["Dep Mario de Barros, 1130, Curitiba","Luzinho","green"],
        ["Rua Carlos de Campos, 1100, Curitiba","Tyta","green"],
        ["Theodoro Makiloka, 2179, Curitiba","DuLeo", "darkblue"] ,
        ["Estrada Nova de Colombo, 5504, Curitiba", "<a href=\"https://spacuritiba.org.br/\">Sociedade Protetora dos Animais</a>", "green"]
        ]

arquivo = "/Users/gazstao/Documents/Curso Python/6 - MapApp/GztMapa.html"
alcance = 11
escala = 250
zoom = 12
lat = 0.0
lon = 0.0
cor = "white"

coordenadas = ArcGIS()
fg = folium.FeatureGroup(name="Aztech LABS")

now = datetime.now()
print("\nGazstao 2019-11-16 GztMapApp (f) -  {}h {}m {}s\n\nProcurando localizacao dos pontos...\n".format(now.hour, now.minute, now.second))

def conSQL (_user = "python", _password = "letsgoal", _host = "localhost", _database = "pythonDB"):
    con = mysql.connector.connect(
    user = _user ,      #    user = "python",
    password = _password ,  #    password = "letsgoal",
    host = _host,       #    host = "localhost",
    database = _database) #    database = "pythonDB" )
    if con.is_connected:
        print("Conectado em {} - Usuário: {}\n".format(con._host, con._user))
        return con
    else:
        print("Não conectado...\n")


con = conSQL()

for endereco in enderecos:
    print ("Endereco: {} - {} - ".format(endereco[0], endereco[1]), end="")
    cor = endereco[2]
    if con.is_connected:
        sql = "select * from local where endereco = '{}'".format(endereco[0])
        cursor = con.cursor()
        query = cursor.execute(sql)
        results = cursor.fetchall()

        # ver se resultado está na lista
        if (results):
            for item in results:
               print("Já esta no banco de dados: {} \nRecuperando latitude e longitude. {},{}\n".format(item[0],item[2],item[3]))
               lat = item[2]
               lon = item[3]
               cor = item[4]
        # se não, inserir
        else:
            local = coordenadas.geocode(endereco[0])
            lat = local.latitude
            lon = local.longitude
            sql = "insert into local values ('{}','{}',{},{}, '{}')".format(endereco[1], endereco[0], lat, lon, cor)
            print("{}".format(sql))
            cursor = con.cursor()
            query = cursor.execute(sql)
            con.commit()
            
        # adiciona marcadores no mapa
        fg.add_child(folium.Marker(location = [lat,lon], popup = endereco[1], icon = folium.Icon(color=cor)))

con.close()
#map = folium.Map(location = [local.latitude, local.longitude], zoom_start="16", tiles="Stamen Terrain", max_zoom=16)
map = folium.Map(location = [-25.36974502969017, -49.236823257833734], zoom_start=zoom)
map.add_child(fg)
map.save(arquivo)

print("\nCriado arquivo {} at -25.36974502969017, -49.236823257833734\n".format(arquivo))
webbrowser.open(arquivo)