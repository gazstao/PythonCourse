import mysql.connector
import difflib

print("\n\nWelcome to the Python SQL Dictionary!")
print("by Gazstao 2019 - Ardit Soulce")

palavra = "love"
sql = "select * from Dictionary where Expression = '{}'".format(palavra)
con = mysql.connector.MySQLConnection()

def conSQL (_user = "ardit700_student", _password = "ardit700_student", _host = "108.167.140.122", _database = "ardit700_pm1database"):
    con = mysql.connector.connect(
    user = _user ,      #    user = "python",
    password = _password ,  #    password = "letsgoal",
    host = _host,       #    host = "localhost",
    database = _database #    database = "pythonDB"
    )
    if con.is_connected:
        print("Conectado em {} - Usuário: {}\n".format(con._host, con._user))
        return con
    else:
        print("Não conectado...\n")

con = conSQL()
if con.is_connected:
    cursor = con.cursor()
    query = cursor.execute(sql)
    results = cursor.fetchall()
    if (results):
        print("{}:".format(palavra.title()))
        x=1
        for item in results:
            print ("{}){}".format(x,item[1]))
            x+=1
    else:
        print("Sem resultados...")