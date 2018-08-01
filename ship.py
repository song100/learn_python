import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the chip and setting the chip"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the image of the chip and achieve its frame rectangle
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # place every new ship in the center of the screen bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store decimal in center attribute
        self.center = float(self.rect.centerx)

        #  Moving sign
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ update the position of the ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update the rect according self.center
        self.rect.centerx = self.center

    def blitme(self):
        """draw the ship on the right position"""
        self.screen.blit(self.image, self.rect)
