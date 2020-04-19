import requests
from bs4 import BeautifulSoup

r = requests.get("")

r = requests.get("a href=\"http://www.ongsbrasil.com.br\default.asp?Pag=1&amp;Destino=Instituicoes&amp;Estado=AP\"")
c = r.content

soup = BeautifulSoup(c, "html.parser")
print (soup.prettify())

