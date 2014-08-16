# coding=utf-8
import re
import urllib2
from bs4 import BeautifulSoup

BUSCA_CEP_SERVICE_BASE_URL = "http://www.buscacep.correios.com.br/servicos/dnec/consultaEnderecoAction.do?relaxation={}&TipoCep=ALL&semelhante=S&cfm=1&Metodo=listaLogradouro&TipoConsulta=relaxation"


class Cep:
    """
    Estrutura de dado para armazenar CEPs
    """
    def __init__(self, numero, logradouro, bairro, localidade, uf):
        self.numero = numero
        self.logradouro = logradouro
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf

    def __repr__(self):
        import json
        return json.dumps(self.__dict__)


def busca(query):
    """
    Invoca o serviço buscacep do site dos correios, e extrai do HTML retornado a lista de ceps encontrados
    :param query: pode ser um numero de cep ou um logradouro
    :return: lista de Ceps encontrados
    """
    content = urllib2.urlopen(BUSCA_CEP_SERVICE_BASE_URL.format(query)).read()
    soup = BeautifulSoup(content)
    trs = soup.findAll('tr', onclick=re.compile('javascript:detalharCep.*'))
    cep_list = []
    for tr in trs:
        td = tr.find_all('td')
        cep_list.append(Cep(
            numero=td[4].string,
            logradouro=td[0].string,
            bairro=td[1].string,
            localidade=td[2].string,
            uf=td[3].string
        ))

    return cep_list