import requests

from bs4 import BeautifulSoup
from string import punctuation
import re


webpage = "http://aztechtecnologia.com.br"

html = requests.get(webpage).content
soup = BeautifulSoup(html, 'html.parser')

# mostra o html formatadinho
html_bonito = soup.prettify()

# mostra texto limpo
clean_text = BeautifulSoup(html, "lxml").text

def preprocess_text(text):
    #text = text.decode('utf-8')
    text = text.lower()  # Lowercase text
    text = re.sub(f"[{re.escape(punctuation)}]", "", text)  # Remove punctuation
    text = " ".join(text.split())  # Remove extra spaces, tabs, and new lines
    return text

print(preprocess_text(clean_text))