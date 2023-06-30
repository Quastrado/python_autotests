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

import sys
import time
from vars.vars import base_url, trainer_id, trainer_token, limit_text
from methods import *
from utils import *

# Узнаём у пользователя сколько битв он хочет провести
while True:
    print('В день можно провести не более 25 битв. Введите "0" (ноль) для выхода')
    counter = input('Желаемое количество битв: ')
    if counter.isdigit() and int(counter) in range(1, 26):
        counter = int(counter)
        break
    elif counter == '0':
        print('Правильно. Я тоже за мир')
        sys.exit()


for i in range(1, counter + 1):
    # Задержка в 2 секунды чтоб не мучать сильно апишку
    time.sleep(2)
    # Получаем список своих покемонов
    my_pokemons = get_my_pokemons(base_url, trainer_id)
    # Если 5 покемонов тренера с атакой 7, уведомить об этом
    weakest = get_weakest(my_pokemons)
    if weakest['attack'] == 7 and len(my_pokemons) == 5:
        print('Твоим покемонам некуда расти')
        sys.exit()
    # Находим своих покемонов в покеболе
    my_pokemons_in_pokeball = get_my_pokemons_in_pokeball(base_url, trainer_id) 
    # Если покемонов у тренера меньше 5, создаём нового и ловим
    if len(my_pokemons) < 5:
        new_pokemon = create_pokemon(base_url, trainer_token)
        new_pokemon_id = new_pokemon['id']
    # Если в покеболе меньше 3 покемонов, ловим нового
        if len(my_pokemons_in_pokeball) < 3:
            add_pokeball(base_url, trainer_token, new_pokemon_id)
    # Выбираем из своих покемонов покемона с самой высокой атакой
    my_pokemon = get_strongest(my_pokemons_in_pokeball)
    my_pokemon_id = my_pokemon['id']
    # Получаем список покемонов в покеболе (первая выдача)
    in_pokeball = find_pokemons_in_pokeball(base_url)
    # Фильтруем список покемонов в покеболе
    # Там не должно быть нашего покемона
    opponents = get_opponents(in_pokeball, trainer_id)
    # Из списка противников выбираем с самой низкой атакой
    opponent = get_weakest(opponents)
    opponent_id = opponent['id']
    # Проводим битву
    battle = fight_a_battle(
        base_url,
        trainer_token,
        my_pokemon_id,
        opponent_id
        )
    # Смотрим результат
    try:
        if battle['result'] == 'Твой покемон проиграл':
            print(f'Итерация {i}, итог: Поражение')
            continue
    except KeyError:
    # Если в теле ответа нет ключа 'result', 
    # выводим сообщение о превышении лимита боёв
    # в день и выходим из программы
        print(limit_text)
        sys.exit()
    
    print(f'Итерация {i}, итог: Победа')
    time.sleep(1)
    # Если атака покемона увеличивается до 7,
    # убираем его из покебола чтоб обезопасить
    my_pokemons_in_pokeball = get_my_pokemons_in_pokeball(base_url, trainer_id)
    strongest = get_strongest(my_pokemons_in_pokeball)
    strongest_id = strongest['id']
    if int(float(strongest['attack'])) == 7:
        delete_from_pokeball(
            base_url,
            trainer_token,
            strongest_id
            )
    