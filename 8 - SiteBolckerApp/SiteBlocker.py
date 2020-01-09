# Gazstao (f) 2019-11-22 - Python - Udemy - Ardit Sulce
# para Mac e Linux: /etc/hosts
# para Windows C:\Windows\System32\drivers\etc

import time
from datetime import datetime as dt

start_hour = 9
end_hour = 19

hosts_temp = "hosts"
hosts_path = "/etc/hosts"
hosts = hosts_temp

redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

print("\n\nGazstao (f) 2019 - Python - Udemy - Ardit Sulce")
print("WEBSITE BLOCKER (TM)\n")

while True:

    if  start_hour < dt.now().hour < end_hour:
        print("Horário de expediente... ") 
        with open(hosts,'r+') as file:
            conteudo = file.read()
            print(conteudo)
            for website in website_list:
                if not website in conteudo:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Horário de diversão ... ")
        with open(hosts,'r+') as file:
            conteudo = file.readlines()
            for linha in conteudo:
                print(linha)
            file.seek(0)
            for linha in conteudo:
                if not any(website in linha for website in website_list):
                    file.write(linha)
    print("Agora: {}".format(dt.now()))                
    time.sleep(10)