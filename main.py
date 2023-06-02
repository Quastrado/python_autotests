import requests
from vars.vars import base_url, trainer_id, trainer_token, pokemon_photo
from utils import cleaning


# Выселяем покемонов из покебола и убиваем чтоб ничего не падало

cleaning(base_url, trainer_id, trainer_token)

# Тут задания из домашки

create_pokemon_response = requests.post(f'{base_url}pokemons',
                    headers={
                        'Content-Type': 'application/json',
                        'trainer_token': trainer_token
                        },
                    json={
                        'name': 'some name',
                        'photo': 'https://dolnikov.ru/pokemons/albums/001.png'
                    })
print('Создание покемона. Ответ:\n' + create_pokemon_response.text)

pokemon_id = create_pokemon_response.json()['id']

upd_pokemon_name_response = requests.put(f'{base_url}pokemons',
                    headers={
                        'Content-Type': 'application/json',
                        'trainer_token': trainer_token
                        },
                    json={
                        'pokemon_id': pokemon_id,
                        'name': 'updated name',
                        'photo': pokemon_photo
                    })
print('Смена имени покемона. Ответ:\n' + upd_pokemon_name_response.text)

add_pokeball_response = requests.post(f'{base_url}trainers/add_pokeball',
                    headers={
                        'Content-Type': 'application/json',
                        'trainer_token': trainer_token
                    },
                    json={
                        'pokemon_id': pokemon_id
                    })

print('Отлов покемона. Ответ:\n' + add_pokeball_response.text)


