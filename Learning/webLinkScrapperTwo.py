from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime

print('\n\n\nGazstao WebParser Test v2.0 2022.09.11-21h03\n\n')

horaExecucao = datetime.now().strftime("%Y.%m.%d-%H.%M")

def gravaNoticias(url):
    request = urllib.request.Request(url)
    request.add_header('Accept-Encoding', 'utf-8')
    resp = urllib.request.urlopen(request)
    soup = BeautifulSoup(resp, 'html.parser', from_encoding=resp.info().get_param('charset'))

    file = open("./Learning/Data/newsArchive.txt","a")
    file.write("\n\nNoticias em {} em {}\n\n".format(url, horaExecucao))

    for link in soup.find_all('a', href=True):
        try:
            texto = BeautifulSoup(link['href'], 'html.parser')
            print(texto.get_text())
            file.write('{}\n'.format(texto.get_text()))
        except:
            print('Erro ao converter {}'.format(url))

    file.close()

gravaNoticias('https://g1.globo.com')
gravaNoticias('https://www.msn.com')
gravaNoticias('https://www.terra.com.br')
gravaNoticias('https://jovempan.com.br/jpnews')
gravaNoticias('https://www.bbc.co.uk')