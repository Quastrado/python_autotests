# Скрипт для автоматического проведения боёв в https://pokemonbattle.me/
# Автоматически выполняет:
# - создание покемона;
# - добавление покемона в покебол;
# - выбор покемона оппонента;
# - проведение битвы;
# - удаление покемона в случае победы

# Для использования скрипта должны быть пройдены следующие шаги:
# 1. Создай себе тренера в котике (полезные ссылки → создать тренера)
# 2. Зарегистрируйся на сайте покемонов: https://pokemonbattle.me/
# Для регистрации можно использовать любую почту или авторизацию через соц сети.
# 3. После регистрации нужно подтвердить аккаунт - это можно сделать по ссылке, которая придет на почту или через Postman

import requests
import sys
import time
from vars.vars import base_url, trainer_id, trainer_token, pokemon_name, pokemon_photo, limit_text
from utils import cleaning

# Узнаём у пользователя сколько битв он хочет провести
while True:
    print('В день можно провести не более 25 битв. Введите "0" (ноль) для выхода')
    counter = input('Желаемое количество битв: ')
    if counter.isdigit():
        if int(counter) >= 1 and int(counter) <= 25:
            counter = int(counter)
            break
        elif counter == '0':
            print('Правильно. Я тоже за мир')
            sys.exit()
# Выселяем покемонов из покебола и убиваем чтоб ничего не падало
cleaning(base_url, trainer_id, trainer_token)


for i in range(1, counter + 1):
    # Задержка в 2 секунды чтоб не мучать сильно апишку
    time.sleep(2)
    # Создаём покемона и получаем его id
    my_pokemon_id = requests.post(f'{base_url}pokemons',
                    headers={
                        'Content-Type': 'application/json',
                        'trainer_token': trainer_token
                        },
                    json={
                        'name': pokemon_name,
                        'photo': pokemon_photo
                    }).json()['id']
    # Добавляем покемона в покебол
    requests.post(f'{base_url}trainers/add_pokeball',
            headers={
                'Content-Type': 'application/json',
                'trainer_token': trainer_token
            },
            json={
                'pokemon_id': my_pokemon_id
            })
    # Получаем покемонов, находящихся в покеболе
    # Первого из них выбираем себе в противники
    pokemons_in_pokeball = requests.get(f'{base_url}pokemons', params={
        'in_pokeball': 1
        }).json()
    
    another_trainer_id = pokemons_in_pokeball[0]['trainer_id']
    defending_pokemon_id = pokemons_in_pokeball[0]['id']
    # Сравниваем id тренера выбранного покемона
    # Если совпадает с id нашего тренера, выбираем следующего
    j = 0
    while another_trainer_id == str(trainer_id):
        j = j + 1
        another_trainer_id = pokemons_in_pokeball[j]['trainer_id']
        defending_pokemon_id = pokemons_in_pokeball[j]['id']
    # Проводим битву
    battle_response = requests.post(f'{base_url}battle',
        headers={
            'Content-Type': 'application/json',
            'trainer_token': trainer_token
        },
        json={
            'attacking_pokemon': my_pokemon_id,
            'defending_pokemon': defending_pokemon_id
        })
    # Смотрим результат
    # В случае поражения переходим на следующую итерацию
    try:
        if battle_response.json()['result'] == 'Твой покемон проиграл':
            print(f'Итерация {i}, итог: Поражение')
            continue
    except KeyError:
        print(limit_text)
        cleaning(base_url, trainer_id, trainer_token)
        sys.exit()
    
    # В случае победы удаляем покемона и начинаем следующую итерацию
    print(f'Итерация {i}, итог: Победа')

    cleaning(base_url, trainer_id, trainer_token)
    
    