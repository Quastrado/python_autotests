import pytest
import requests
from vars.vars import base_url, trainer_id, trainer_name

def test_get_trainers_status_code():
    response = requests.get(f'{base_url}trainers')
    assert response.status_code == 200

def test_get_my_trainer_name():
    response = requests.get(f'{base_url}trainers', params={
        'trainer_id': trainer_id
    })
    assert response.json()['trainer_name'] == trainer_name