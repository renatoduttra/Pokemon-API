import requests



def pegar_pokemon():
    print ('Habilidades do {pokemon}')
    for i in poke['abilities']:
        print(i['abilities']['name'])

def main():
    global pokemon
    pokemon =  str(input('Pokemon : '))
    api = 'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(api)
    poke = res.jason()

    if __name__ == '__main__':
        main()