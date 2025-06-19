from random import randint
import requests
import random

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
       
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.ability = self.get_ability()
        self.hp = random.randint(200, 400)
        self.power = random.randint(30, 60)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "error"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_ability(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['abilities'][0]['ability']['name'])
        else:
            return "error"
        
    # Метод класса для получения информации
    def info(self):
        pokemon_info = (

            f"Имя твоего покеомона: {self.name}/n"
            f"pokemon power: {self.power}/n"
            f"pokemon: {self.hp}"
        )
        return pokemon_info

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def ab(self):
        return self.ability
    
    # class's method for attack
    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1, 5)
            if chance  == 2:
                return f'pokemon-wizard used magic shield'
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f'fight between @{self.pokemon_trainer} and @{enemy.pokemon_trainer}'
        else:
            enemy.hp = 0
            return f'@{self.pokemon_trainer} won against @{enemy.pokemon_trainer}'

class Wizard(Pokemon):
    pass

class Fighter(Pokemon): # 30-60 / 6-12
    def attack(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f'/nfighter used its power {super_power}'

if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))


