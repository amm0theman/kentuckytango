"""takes care of movement for next frame of game play"""
from gameState import GameState
from ship import Ship
import math
from command import Command
from point import Point
from bullet import Bullet
import pygame


class MovementManager:
    def __init__(self, render_pace, window_x, window_y):
        self.renderPace = render_pace
        self.window_x = window_x
        self.window_y = window_y
        self.command_ship1: Command = Command()
        self.command_ship2: Command = Command()
        self.bullet_tracker1: int = 0
        self.bullet_tracker2: int = 0

    def calculate_ship_movement(self, ship: Ship):
        ship.pos += ship.pos_delta * self.renderPace
        ship.pos = self.calculate_wrap(ship.pos)
        return ship

    def calculate_rotation(self, game_state: GameState) -> GameState:
        if self.command_ship1.right:
            game_state.my_ship.heading -= .02
        elif self.command_ship1.left:
            game_state.my_ship.heading += .02
        if self.command_ship2.right:
            game_state.enemy_ship.heading -= .02
        elif self.command_ship2.left:
            game_state.enemy_ship.heading += .02
        return game_state

    @staticmethod
    def calculate_heading_vector(ship: Ship) -> Point:
        theta = ship.heading
        magnitude = ship.acceleration
        heading_vector = Point(magnitude * math.cos(theta), magnitude * math.sin(theta))
        return heading_vector

    def calculate_pos_delta(self, game_state: GameState) -> GameState:
        if self.command_ship1.accel:
            game_state.my_ship.pos_delta += self.calculate_heading_vector(game_state.my_ship)
        if self.command_ship2.accel:
            game_state.enemy_ship.pos_delta += self.calculate_heading_vector(game_state.enemy_ship)

        '# Calculate max speeds and friction'
        game_state.my_ship.pos_delta = self.calculate_friction(game_state.my_ship.pos_delta)
        game_state.enemy_ship.pos_delta = self.calculate_friction(game_state.enemy_ship.pos_delta)
        return game_state

    def calculate_movement(self, game_state: GameState) -> GameState:
        """Calculates movement for all game objects in the game state"""
        '# Calculate ships movements'
        game_state.my_ship = self.calculate_ship_movement(game_state.my_ship)
        game_state.enemy_ship = self.calculate_ship_movement(game_state.enemy_ship)

        '# Calculate movement for asteroids and for bullets'
        for i in game_state.asteroids:
            i.pos += i.pos_delta * self.renderPace
            i.pos = self.calculate_wrap(i.pos)
        for i in game_state.bullets:
            i.pos += i.pos_delta * self.renderPace
            i.pos = self.calculate_wrap(i.pos)

        return game_state

    def calculate_wrap(self, position: Point) -> Point:
        window_min = 0
        if position.x < window_min:
            position.x = self.window_x
        elif position.x > self.window_x:
            position.x = window_min
        if position.y < window_min:
            position.y = self.window_y
        elif position.y > self.window_y:
            position.y = window_min
        return position

    def calculate_friction(self, delta: Point) -> Point:
        top_speed = 200
        if self.command_ship1.accel is False:
            delta *= .993
        if math.fabs(delta.x) > top_speed:
            if delta.x > 0:
                delta.x = top_speed
            if delta.x < 0:
                delta.x = -1 * top_speed
        if math.fabs(delta.y) > top_speed:
            if delta.y > 0:
                delta.y = top_speed
            if delta.y < 0:
                delta.y = -1 * top_speed
        return delta

    def calculate_shoot(self, game_state: GameState, screen) -> GameState:
        if self.command_ship1.shoot and self.bullet_tracker1 < 10:
            self.bullet_tracker1 += 50
            theta = game_state.my_ship.heading
            magnitude = game_state.my_ship.acceleration
            heading_vector = Point(magnitude * math.cos(theta), magnitude * math.sin(theta))
            '# shoot a bullet with x time to live that gets updated every cycle'
            '# def __init__(self, screen, pos, pos_delta, ttl):'
            game_state.bullets.append(
                Bullet(screen,
                       Point(game_state.my_ship.pos.x, game_state.my_ship.pos.y) + (
                                   heading_vector * 25),
                       heading_vector * 200, 250))
        else:
            if self.bullet_tracker1 > 0:
                self.bullet_tracker1 -= 1

        if self.command_ship2.shoot and self.bullet_tracker2 < 10:
            self.bullet_tracker2 += 50
            theta = game_state.enemy_ship.heading
            magnitude = game_state.enemy_ship.acceleration
            heading_vector = Point(magnitude * math.cos(theta), magnitude * math.sin(theta))
            '# shoot a bullet with x time to live that gets updated every cycle'
            '# def __init__(self, screen, pos, pos_delta, ttl):'
            game_state.bullets.append(
                Bullet(screen,
                       Point(game_state.enemy_ship.pos.x, game_state.enemy_ship.pos.y) + (
                                   heading_vector * 25),
                       heading_vector * 200, 250))
        else:
            if self.bullet_tracker2 > 0:
                self.bullet_tracker2 -= 1
        return game_state
