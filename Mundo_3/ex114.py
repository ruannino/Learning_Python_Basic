# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
# print(site.read()) lê os dados do site
import urllib.error
import urllib.request

try:
    urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site pudim não está acessível no momento!\033[m')
else:
    print('\033[32mConsegui acessar o site pudim!\033[m')
