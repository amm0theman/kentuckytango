"""Asteroid object in the game"""
from point import Point
import pygame


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen, pos: Point, pos_delta: Point, size):
        self.screen = screen
        self.pos: Point = pos
        self.pos_delta: Point = pos_delta
        self.size = size

        '# Sprite initialization'
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/asteroid.png')
        self.image = pygame.transform.scale(self.image, (self.size, self.size - 25))
        self.rect = self.image.get_rect()

    def blitme(self):
        rotated_image_rect = self.rect
        rotated_image_rect.center = (self.pos.x, self.pos.y)
        self.screen.blit(self.image, rotated_image_rect)
