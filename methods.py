import requests
from vars.vars import pokemon_photo, pokemon_name


def get_my_pokemons(base_url, trainer_id):
    '''
    Получить покемонов тренера
    '''
    return requests.get(f'{base_url}pokemons', params={'trainer_id': trainer_id}).json()


def get_my_pokemons_in_pokeball(base_url, trainer_id):
    '''
    Получить покемонов тренера в покеболе
    '''
    return requests.get(f'{base_url}pokemons', 
                        params={
                            'trainer_id': trainer_id,
                            'in_pokeball': 1
                            }
                            ).json()


def create_pokemon(base_url, trainer_token):
    '''
    Создать покемона
    '''
    create_pokemon = requests.post(f'{base_url}pokemons',
                        headers={
                            'Content-Type': 'application/json',
                            'trainer_token': trainer_token
                            },
                        json={
                            'name': pokemon_name,
                            'photo': pokemon_photo
                        })
    return create_pokemon.json()


def add_pokeball(base_url, trainer_token, my_pokemon_id):
    '''
    Поймать покемона в покебол
    '''
    requests.post(f'{base_url}trainers/add_pokeball',
            headers={
                'Content-Type': 'application/json',
                'trainer_token': trainer_token
            },
            json={
                'pokemon_id': my_pokemon_id
            })
    return True


def delete_from_pokeball(base_url, trainer_token, my_pokemon_id):
    '''
    Удалить покемона из покебола
    '''
    requests.post(f'{base_url}trainers/delete_pokeball',
            headers={
                'Content-Type': 'application/json',
                'trainer_token': trainer_token
            },
            json={
                'pokemon_id': my_pokemon_id
            })
    return True
    

def find_pokemons_in_pokeball(base_url):
    '''
    Найти покемонов в покеболе
    '''
    return requests.get(f'{base_url}pokemons', params={
        'in_pokeball': 1
        }).json()


def fight_a_battle(base_url, trainer_token, my_pokemon_id, defending_pokemon_id):
    '''
    Провести битву
    '''
    return requests.post(f'{base_url}battle',
        headers={
            'Content-Type': 'application/json',
            'trainer_token': trainer_token
        },
        json={
            'attacking_pokemon': my_pokemon_id,
            'defending_pokemon': defending_pokemon_id
        }).json()