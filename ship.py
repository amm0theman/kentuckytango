"""#Point class representing ship controlled by player"""
from functools import singledispatch
from point import Point
from bullet import Bullet
from asteroid import Asteroid
import pygame
import math


class Ship(pygame.sprite.Sprite):
    def __init__(self, screen, pos: Point, pos_delta: Point, heading: float, acceleration: float):
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface = pygame.image.load('images/ship.png')
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()

        self.screen = screen
        self.pos: Point = pos
        self.pos_delta: Point = pos_delta
        self.heading: float = heading
        self.acceleration: float = acceleration

    def blitme(self):
        heading_in_degrees = (180 * self.heading) / math.pi
        rotated_image = pygame.transform.rotate(self.image, -heading_in_degrees)
        rotated_image_rect = rotated_image.get_rect()
        rotated_image_rect.center = (self.pos.x, self.pos.y)
        self.rect = rotated_image_rect
        self.screen.blit(rotated_image, rotated_image_rect)

    @singledispatch
    def intersect_event(self, arg):
        pass

    @intersect_event.register(Bullet)
    def _(self, arg: Bullet):
        pass

    @intersect_event.register(Asteroid)
    def _(self, arg: Asteroid):
        pass
