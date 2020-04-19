from bs4 import BeautifulSoup
import requests

r = requests.get("https://aztechtecnologia.com.br")
print(r.content)