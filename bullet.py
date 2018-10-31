"""Bullet object in the game"""
from point import Point
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, pos, pos_delta, ttl):
        self.screen = screen
        self.pos: Point = pos
        self.pos_delta: Point = pos_delta
        self.ttl = float(ttl)

        '# Sprite initialization'
        pygame.sprite.Sprite.__ini t__(self)
        self.image = pygame.image.load('images/bullet.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()

    def blitme(self):
        rotated_image_rect = self.rect
        rotated_image_rect.center = (self.pos.x, self.pos.y)
        self.screen.blit(self.image, rotated_image_rect)
