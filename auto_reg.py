import requests
from vars.vars import base_url

email = input('Введите почту: ')
password = input('Введите пароль: ')
trainer_token = input('Ввкдите токен: ')

requests.post(f'{base_url}trainers/reg', headers={
    'Content-Type': 'application/json'
    },
    json={
    'trainer_token': trainer_token,
    'email': email,
    'password': password
    })

requests.post(f'{base_url}trainers/confirm_email', headers={
    'Content-Type': 'application/json'
    },
    json={
    'trainer_token': trainer_token
    })