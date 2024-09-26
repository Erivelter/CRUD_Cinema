import requests

def buscar_todos_filmes(generos, max_paginas=5):
    api_key = "95037e14"
    url = "http://www.omdbapi.com/"
    todos_filmes = []

    for genero in generos:
        for pagina in range(1, max_paginas + 1):
            params = {
                'apikey': api_key,
                's': genero,
                'type': 'movie',
                'r': 'json',
                'page': pagina
            }
            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                dados = response.json()
                filmes = dados.get('Search', [])
                todos_filmes.extend(filmes)

                if not filmes:  # Se não houver mais filmes, sai do loop
                    break
            else:
                print("Erro na requisição:", response.status_code)

    return todos_filmes

# Exemplo de uso
generos_para_buscar = ["Action", "Comedy", "Drama"]
todos_filmes = buscar_todos_filmes(generos_para_buscar)

# Exibe os resultados
for filme in todos_filmes:
    print(f"Titulo: {filme['Title']}, Ano: {filme['Year']}, ID: {filme['imdbID']}, Poster: {filme['Poster']}")
