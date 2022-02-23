import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to maintain Aliens"""

    def __init__(self,ss_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        #Load the image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien at the top right corner of screen
        self.rect.y = self.settings.screen_width - self.rect.width
        self.rect.x = self.settings.screen_height - self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return true if alien is at edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0 or self.rect.bottom <= screen_rect.bottom:
            return True


    def update(self):
        """Move the alien up or down"""
        self.x -= (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x     
