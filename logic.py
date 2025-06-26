from random import randint
import requests
import random
from datetime import datetime, timedelta
from chance import chance

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
        self.pkmclass = self.pclass()
        Pokemon.pokemons[pokemon_trainer] = self
        self.last_feed_time = datetime.now()

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
        
    def pclass(self):
        if chance == 1 or 2 or 3:
            pkclass = 'Normal Pokemon'
            return pkclass
        if chance == 4:
            pkclass = 'Wizard'
            return pkclass
        if  pkclass == 5:
            pkclass = 'Fighter'
            return pkclass
        else:
            return 'error'
        
    
        
    # Метод класса для получения информации
    def info(self):
        pokemon_info = (

            f"Имя твоего покеомона: {self.name}\n"
            f"pokemon power: {self.power}\n"
            f"pokemon hp: {self.hp}\n"
            f"pokemon ability: {self.ab()}\n"
            f"pokemon type: {self.pcl()}"
        )
        return pokemon_info

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    #class's method for getting information about ability
    def ab(self):
        return self.ability
    
    def pcl(self):
        return self.pkmclass
    
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
        
    # class's method for feeding your pokemon
    def feed(self, feed_interval=20, hp_increase=10):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time + delta_time}"

class Wizard(Pokemon):
    def feed(self):
        return super().feed(feed_interval=10)

class Fighter(Pokemon): # 30-60 / 6-12
    def attack(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f'/nfighter used its power {super_power}'
    
    def feed(self):
        return super().feed(hp_increase=20)

if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))


