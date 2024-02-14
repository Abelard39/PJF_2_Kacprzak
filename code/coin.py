import pygame


class Coin:
    def __init__(self, name):
        self.name = name
        self.image = pygame.image.load("../res/art/collectibles/coin.png")

    def get_image(self):
        return self.image
