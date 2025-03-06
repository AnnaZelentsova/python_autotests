import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '155150bc8be065a8637b947e55ccc340'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : TOKEN}
POKEMON_ID = '252043'

body_create = {
    "name": "Карапуз",
    "photo_id": 563
}

body_new_name = {
    "pokemon_id": POKEMON_ID,
    "name": "Многорук",
    "photo_id": 563
}

body_add_pokeboll = {
    "pokemon_id": POKEMON_ID
}

response_create = requests.post (url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)

responce_new_name = requests.put (url= f'{URL}/pokemons', headers= HEADER, json= body_new_name )
print (responce_new_name.text)

responce_add_pokeball = requests.post (url= f'{URL}/trainers/add_pokeball', headers= HEADER, json= body_add_pokeboll)
print (responce_add_pokeball.text)

