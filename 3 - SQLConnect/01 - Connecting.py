import mysql.connector

sql = "select * from Dictionary where Expression = 'rain'"

print("\n______________________________________\n\nMySQL Python Project Gazstao 2019  v:20191111\n")
con = mysql.connector.connect(
    user = "ardit700_student",      #    user = "python",
    password = "ardit700_student",  #    password = "letsgoal",
    host = "108.167.140.122",       #    host = "localhost",
    database = "ardit700_pm1database" #    database = "pythonDB"
    )
if con.is_connected:
    print("Conectado em {} - Usuário: {}\n".format(con._host, con._user))
else:
    print("Não conectado...\n")

cursor = con.cursor()
#query = cursor.execute("show tables")
print("Executando comando SQL:\n{}\n".format(sql))
query = cursor.execute(sql)
results = cursor.fetchall()

if results:
    for result in range(len(results)):
        #print (results[result])
        for item in results[result]:
            print("{}   ".format(item), end='')
        print("")

print("\nAté logo!\n")