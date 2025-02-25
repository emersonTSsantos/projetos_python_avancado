# IMDb Movie Scraper

Este projeto é um web scraper para coletar detalhes dos filmes mais populares no IMDb. Ele utiliza `requests`, `BeautifulSoup` e `concurrent.futures` para extrair informações de forma eficiente.

## Funcionalidades

- Coleta os 100 filmes mais populares do IMDb a partir da página de tendências.
- Para cada filme, extrai:
  - Título
  - Data de lançamento
  - Nota (avaliação)
  - Sinopse
- Os dados coletados são salvos em um arquivo `movies.csv`.
- Utiliza `ThreadPoolExecutor` para processamento paralelo, acelerando a coleta de dados.

## Tecnologias Utilizadas

- Python 3.x
- `requests` para requisições HTTP
- `BeautifulSoup` para parsing de HTML
- `csv` para salvar os dados extraídos
- `concurrent.futures` para processamento paralelo

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/imdb-movie-scraper.git
   cd imdb-movie-scraper

## Autor

Feito por Emerson Teixeira