import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.ongsbrasil.com.br/default.asp?Pag=1&Destino=Instituicoes")
c = r.content
# print c

soup = BeautifulSoup(c, "html.parser")
print (soup.prettify())
