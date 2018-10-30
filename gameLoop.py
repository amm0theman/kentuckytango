import pygame
from gameState import GameState
from point import Point
from ship import Ship
from asteroid import Asteroid
from bullet import Bullet
from movementManager import MovementManager
from collisionManager import CollisionManager
from random import randint
import math


class GameLoop:
    def __init__(self):
        '# Initialize game window and settings etc.'
        self.screen = pygame.display.set_mode(
            (1000, 1000))

        pygame.display.set_caption("Asteroids")
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.debug_text_surface = self.myfont.render('Hello', False, (255, 255, 255))

        self.render_pace: float = 1 / 60
        self.game_active = True
        asteroid_list = []
        bullet_list = []

        ship = Ship(self.screen, Point(400, 500), Point(0, 0), -math.pi / 2, 1)
        enemy_ship = Ship(self.screen, Point(600, 500), Point(0, 0), -math.pi / 2, 1)
        self.game_state = GameState(ship, enemy_ship, bullet_list, asteroid_list)

        for count in range(0, 8):
            asteroids = Asteroid(self.screen, Point(randint(0, 900), randint(0, 900)),
                                 Point(randint(-20, 20), randint(-20, 20)), randint(120, 170))
            list.append(asteroid_list, asteroids)

        for count in range(0, 10):
            bullets = Bullet(self.screen, Point(randint(200, 300), randint(400, 500)), Point(5, 5), 50)
            list.append(bullet_list, bullets)

        self.movement_manager = MovementManager(self.render_pace, 1000, 1000)
        self.collision_manager = CollisionManager()

    def handle_events(self):
        for event in pygame.event.get():
            '# When x button pushed quit game'
            if event.type == pygame.KEYDOWN:
                '#process ship one key down presses'
                if event.key == pygame.K_w:
                    self.movement_manager.command_ship1.accel = True
                elif event.key == pygame.K_a:
                    self.movement_manager.command_ship1.right = True
                elif event.key == pygame.K_d:
                    self.movement_manager.command_ship1.left = True
                elif event.key == pygame.K_SPACE:
                    self.movement_manager.command_ship1.shoot = True
                elif event.key == pygame.K_8:
                    '#process ship two key down presses'
                    self.movement_manager.command_ship2.accel = True
                elif event.key == pygame.K_4:
                    self.movement_manager.command_ship2.left = True
                elif event.key == pygame.K_6:
                    self.movement_manager.command_ship2.right = True
                elif event.key == pygame.K_0:
                    self.movement_manager.command_ship2.shoot = True
            elif event.type == pygame.KEYUP:
                '#process ship one key up presses'
                if event.key == pygame.K_w:
                    self.movement_manager.command_ship1.accel = False
                elif event.key == pygame.K_a:
                    self.movement_manager.command_ship1.right = False
                elif event.key == pygame.K_d:
                    self.movement_manager.command_ship1.left = False
                elif event.key == pygame.K_SPACE:
                    self.movement_manager.command_ship1.shoot = False
                elif event.key == pygame.K_8:
                    '#process ship two key up presses'
                    self.movement_manager.command_ship2.accel = False
                elif event.key == pygame.K_4:
                    self.movement_manager.command_ship2.left = False
                elif event.key == pygame.K_6:
                    self.movement_manager.command_ship2.right = False
                elif event.key == pygame.K_0:
                    self.movement_manager.command_ship2.shoot = False
            elif event.type == pygame.QUIT:
                self.game_active = False
                pygame.quit()

    def update_game(self):
        self.game_state = self.movement_manager.calculate_rotation(self.game_state)
        self.game_state = self.movement_manager.calculate_pos_delta(self.game_state)
        self.game_state = self.movement_manager.calculate_movement(self.game_state)
        self.game_state = self.movement_manager.calculate_shoot(self.game_state, self.screen)
        self.game_state = self.collision_manager.if_intersect(self.game_state)

        for i in self.game_state.bullets:
            i.ttl -= 1

        for i in self.game_state.bullets:
            if i.ttl <= 0:
                self.game_state.bullets.remove(i)

    def render_game(self):
        '#render new asteroids at new locations every call'
        "#render new ship locations and heading directions"
        '#render bullets as they are created and travel until they die'

        self.game_state.my_ship.blitme()
        self.game_state.enemy_ship.blitme()

        for i in self.game_state.asteroids:
            i.blitme()
        for i in self.game_state.bullets:
            i.blitme()

        self.debug_text_surface = self.myfont.render(str(self.game_state.my_ship.pos_delta.x), False, (255, 255, 255))
        self.screen.blit(self.debug_text_surface, (0, 0))

        pygame.display.flip()
        self.screen.fill(000000)

    """Main game loop"""

    def run_game(self):
        pygame.init()

        while self.game_active:
            self.handle_events()
            self.update_game()
            self.render_game()
