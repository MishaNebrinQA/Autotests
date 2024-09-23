import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='c53fc8df52eb1a2001caeeab60aeac64'
HEADER = {'Content-Type' : 'application/json', "trainer_token" : TOKEN}


'''body_registration = {
"trainer_token": TOKEN,
"email": "misha.nebrin@gmail.com",
"password": "Qwe5726259!"
}

body_confirmation = {
    "trainer_token" : TOKEN
}'''

body_create = {
    "name": "Бульбазаврик",
    "photo_id": 1
}


'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation  = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']

body_change_name = {
    "pokemon_id": pokemon_id,
    "name": "Бульбазавриус",
    "photo_id": 1
}

body_add_pokeball = {
    "pokemon_id": pokemon_id
}

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)


response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)