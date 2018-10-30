"""#Shows the Game state for each object"""
from typing import List
from ship import Ship
from bullet import Bullet
from asteroid import Asteroid


class GameState:
    def __init__(self, my_ship, enemy_ship, bullets, asteroids):
        self.my_ship: Ship = my_ship
        self.enemy_ship: Ship = enemy_ship
        self.bullets: List[Bullet] = bullets
        self.asteroids: List[Asteroid] = asteroids
