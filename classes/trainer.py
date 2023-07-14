import requests

class Trainer():
    
    def __init__(self, trainer_data) -> None:
        self.trainer_token = trainer_data['trainer_token']
        self.trainer_id = trainer_data['trainer_id']
        self.trainer_name = trainer_data['trainer_name']
        self.pokemon_name = trainer_data['pokemon_name']
        self.pokemon_photo = trainer_data['pokemon_photo']

    
    def get_trainer_pokemons(self, base_url):
        '''
        Получить покемонов тренера
        '''
        return requests.get(f'{base_url}pokemons', params={'trainer_id': self.trainer_id}).json()
    

    def get_trainers_pokemons_in_pokeball(self, base_url):
        '''
        Получить покемонов тренера в покеболе
        '''
        return requests.get(f'{base_url}pokemons', 
                            params={
                                'trainer_id': self.trainer_id,
                                'in_pokeball': 1
                                }
                                ).json()
    

    def get_trainers_pokemons_not_in_pokeball(self, base_url):
        '''
        Получить покемонов тренера вне покебола
        '''
        return requests.get(f'{base_url}pokemons', 
                            params={
                                'trainer_id': self.trainer_id,
                                'in_pokeball': 0
                                }
                                ).json()
    

    def get_pokemons_in_pokeball(base_url):
        '''
        Получить всех покемонов в покеболе
        '''
        return requests.get(f'{base_url}pokemons',
                            params={
                                'in_pokeball': 1
                            }
                            ).json()
    

    def get_trainer_info(base_url, trainer_id):
        '''
        Получить информацию о тренере
        '''
        return requests.get(f'{base_url}trainers', 
                            params={
                                'trainer_id': trainer_id
                                }
                                ).json()
    

    def create_pokemon(self, base_url):
        '''
        Создать покемона
        '''
        create_pokemon = requests.post(f'{base_url}pokemons',
                            headers={
                                'Content-Type': 'application/json',
                                'trainer_token': self.trainer_token
                                },
                            json={
                                'name': self.pokemon_name,
                                'photo': self.pokemon_photo
                            })
        return create_pokemon.json()
    

    def add_pokeball(self, base_url, pokemon_id):
        '''
        Поймать покемона в покебол
        '''
        requests.post(f'{base_url}trainers/add_pokeball',
                headers={
                    'Content-Type': 'application/json',
                    'trainer_token': self.trainer_token
                },
                json={
                    'pokemon_id': pokemon_id
                })
    

    def delete_from_pokeball(base_url, trainer_token, my_pokemon_id):
        '''
        Удалить покемона из покебола
        '''
        requests.put(f'{base_url}trainers/delete_pokeball',
                headers={
                    'Content-Type': 'application/json',
                    'trainer_token': trainer_token
                },
                json={
                    'pokemon_id': my_pokemon_id
                })
        

    def fight_a_battle(self, base_url, my_pokemon_id, opponent_pokemon_id):
        '''
        Провести битву
        '''
        return requests.post(f'{base_url}battle',
            headers={
                'Content-Type': 'application/json',
                'trainer_token': self.trainer_token
            },
            json={
                'attacking_pokemon': my_pokemon_id,
                'defending_pokemon': opponent_pokemon_id
            }).json()