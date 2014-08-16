BuscaCep
========

O site dos Correios disponibiliza gratuitamente um ótimo serviço para busca online de CEPs.
Porém, essa é a única forma de acessá-lo: via página HTML.
Não existe, nem é exposta, nenhuma API que facilite a integração desse serviço com outras aplicações.

Para possibilitar esse tipo de integração, criei o buscacep que nada mais é que um componente python
que abstrai a complexidade de:

- Fazer a requisição HTTP (GET) passando os parâmetros necessários e;
- Processar a resposta - extraindo os dados de CEP do HTML retornado.

Internamente utilizo a biblioteca beautifulsoup4 para auxiliar no Web Scraping.