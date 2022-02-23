import pygame
from pygame.sprite import Sprite
 
class Raindrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, rd_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # Load the raindrop image and set its rect attribute.
        #   Raindrop image from: https://commons.wikimedia.org/wiki/File:Antu_raindrop.svg
        #   License: https://creativecommons.org/licenses/by-sa/3.0/deed.en
        #   Modified size, and cropped.
        self.image = pygame.image.load('Practice/Ch13/13_4/images/raindrop.png')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrop down the screen."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y

    def check_bottom(self):
        """Return true if raindrops are at bottom of the screen"""
        #screen_rect = self.screen.get_rect()
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False