import requests


def cleaning(base_url, trainer_id, trainer_token):
    '''
    Метод для очистки покебола и удаления покемнонов
    Применялся в старой реализации
    Будет удалён или переписан
    '''
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

def get_strongest(my_pokemons):
    '''
    Отыскать покемона с самой высокой атакой
    '''
    first = my_pokemons[0]
    if len(my_pokemons) > 1:
        for i in range(1, len(my_pokemons)):
            second = my_pokemons[i]
            if int(float(second['attack'])) > int(float(first['attack'])):
                first = second
    return first


def get_weakest(opponents):
    '''
    Отыскать покемона с самой слабой атакой
    '''
    first = opponents[0]
    if len(opponents) > 1:
        for i in range(1, len(opponents)):
            second = opponents[i]
            if int(float(second['attack'])) < int(float(first['attack'])):
                first = second
    return first


def get_opponents(pokemons, trainer_id):
    '''
    Сформировать список чужих покемонов в покеболе
    '''
    return [pokemon for pokemon in pokemons if pokemon['trainer_id'] != str(trainer_id)]


def choose_an_opponent(trainer_id, in_pokeball):
    '''
    Подобрать противника для битвы
    id тренера не должен совпадать с нашим
    '''
    opponent = {
        'trainer_id' : in_pokeball[0]['trainer_id'],
        'pokemon_id': in_pokeball[0]['id']
    }
    i = 0
    while opponent['trainer_id'] == str(trainer_id):
        i = i + 1
        opponent['trainer_id'] = in_pokeball[i]['trainer_id']
        opponent['pokemon_id'] = in_pokeball[i]['id']
    return opponent
