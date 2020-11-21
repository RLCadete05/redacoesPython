import re

import requests
from bs4 import BeautifulSoup

# verificar se a página está disponível
def get_pagina_existente(object):
    content = requests.get(object.strip())
    return False if content.status_code == 404 else content.content

def temas_e_links(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    # select = soup.find('select', attrs={'id': 'selectBoxBR'})
    options = soup.select('select[id=selectBoxBR]> option')
    for option in options[1:]:
        print(option['value'] + '->' + option.text)

class extrair_descricao(object):
    def get_descricao_tema(self, soup):
        soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
        secao_texto = soup.find('div', attrs={'id': 'secao_texto'})
        divs = secao_texto.find_all('div')
        print(divs[11].text)

'''
def get_essays(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    tables = soup.find('table', attrs={'id': 'redacoes_corrigidas'})
    links = tables.find_all('a')
    for link in links:
        print(link.get('href'))
'''

def extrair_titulo_e_tema(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    try:
        theme = soup.find_all('span', attrs={'itemprop': 'name'})[2].text
        print('\nTEMA: ', theme)
    except Exception as e:
        try:
            theme = soup.find('span', attrs={'class': 'definicao'})
            theme = theme.find('a').text.strip()
            print(theme)
        except Exception as e:
            print(e)
    title = soup.find('div', attrs={'class': 'br-grid-3 margem-conteudo'})
    title = title.find('h1').text.strip()
    print('\nTITULO: ', title)
    essay = soup.find('div', attrs={'class': 'conteudo-materia'})
    for content in essay.find_all('p')[1:]:
        print(content.text)

class ExtrairNota():
    def get_redacoes(url):
        soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
        tabela = soup.find('table', attrs={'id': 'redacoes_corrigidas'})
        coluna = tabela.find_all('td')[1]
        print(soup.find(id='redacoes_corrigidas').text)




URL_BASE = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes'
url_theme = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes/tema-abuso-de-autoridade-no-brasil.htm'
url_essay = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes/16257'
temas_e_links(URL_BASE)

#get_descricao_tema(url_theme)
#descricao = extrair_descricao(url_theme)

# get_redacoes(url_theme)

#extrair_titulo_e_tema(url_essay)
ExtrairNota(url_essay)