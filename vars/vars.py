import random
from vars.secrets import trainer_token, trainer_id, trainer_name

base_url = 'https://api.pokemonbattle.me:9104/'
trainer_token = trainer_token
trainer_id = trainer_id
trainer_name = trainer_name
pokemon_name = random.choice([
    'Severus',
    'Lucius',
    'Rudolfus',
    'Regulus',
    'Rabastan',
    'Bellatrix',
    'Antonin',
    'August',
    'Narcissa',
    'Selvin'
])
pokemon_photo = random.choice([
    'https://dolnikov.ru/pokemons/albums/092.png',
    'https://dolnikov.ru/pokemons/albums/093.png',
    'https://dolnikov.ru/pokemons/albums/094.png'
])
limit_text = 'Твой лимит боёв исчерпан. Текущее ограничение: 25 в день'