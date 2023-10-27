# make a nn webscraper that can figure out what to search for

import random
import turtle
from pynput.keyboard import Key, Listener
# default constructor
class Character: # l3arn how to do instance/ private variables 
    def __init__(self, type, level): # also learn toString()
        self.type = type
        self.level = level
        self.health = level * random.randint(20,30)
        self.damage = level * random.randint(10,15)
        self.attack_chance = random.randint(0,5)
    
    def attack(self, character):
        attack_success = random.randint(0,30-self.attack_chance)
        if attack_success <= 15:
            character.health -= self.damage - attack_success

alive = False
frankie = Character('wizard', 5)
johnny = Character('lizard', 5)
while alive:
    frankie.attack(johnny)
    johnny.attack(frankie)
    print(f"frankie health: {frankie.health}")
    print(f"johnny health: {johnny.health}")
    if frankie.health <= 0 or johnny.health <= 0:
        alive = False

class NN:
    def __init__(self, parent1, parent2, food_position):
        self.parent1 = parent1
        self.parent2 = parent2
        self.choice = random.randint(0,4)
count = 0 
keys = []

# apple pos = [6,5]
# tail_poses = [ [3,2] [2,4] ]
# 

def on_press(key):
    print(key)
    keys.append(key)

def write_file():
    with open("log.txt", "a") as f:
        for key in keys:
            f.write(str(key))

def on_release(key):
    if key == Key.esc:
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
        
        


            
