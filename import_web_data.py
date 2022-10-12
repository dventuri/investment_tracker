#https://reulison.com.br/web-scraping-python/

#importe a biblioteca usada para consultar uma URL
import urllib.request

#importe as funções BeautifulSoup para analisar os dados retornados do site
from bs4 import BeautifulSoup

#especifique o URL
wiki = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/19348/ITUB/corporate-actions?language=pt-br"

#Consulte o site e retorne o html para a variável 'page'
page = urllib.request.urlopen(wiki)

#Parse o html na variável 'page' e armazene-o no formato BeautifulSoup
soup = BeautifulSoup(page, 'html5lib')

