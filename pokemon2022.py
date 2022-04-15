import requests

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon?limit=20'

    response = requests.get(url)

    payload = response.json()
    results = payload.get('results', [])

    for pokemon in results:
        name = pokemon['name']
 
        print(name)
  