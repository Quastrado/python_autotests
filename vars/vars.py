import random

base_url = 'https://pokemonbattle.me:9104/'
trainer_token = 'd77b841d8b0e7a3a065b5504a2305958'
trainer_id = 4454
trainer_name = 'Quastrado'
pokemon_name = random.choice([
    'Uno',
    'Dois',
    'Tres'
])
pokemon_photo = random.choice([
    'https://dolnikov.ru/pokemons/albums/092.png',
    'https://dolnikov.ru/pokemons/albums/093.png',
    'https://dolnikov.ru/pokemons/albums/094.png'
])
limit_text = 'Твой лимит боёв исчерпан. Текущее ограничение: 25 в день'