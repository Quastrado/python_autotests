import requests

def cleaning(base_url, trainer_id, trainer_token):
    my_pokemons = requests.get(f'{base_url}pokemons', params={'trainer_id': trainer_id})
    if len(my_pokemons.json()) > 0:
        for pokemon in my_pokemons.json():
            id = pokemon['id']
            requests.post(f'{base_url}trainers/delete_pokeball', headers={'Content-Type': 'application/json'}, json={
                'pokemon_id': id
            })
            requests.post(f'{base_url}pokemons/kill', 
                        headers={
                            'Content-Type': 'application/json',
                            'trainer_token': trainer_token
                            },
                        json={
                            'pokemon_id': id
            })