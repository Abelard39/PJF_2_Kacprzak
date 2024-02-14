import pygame


class Fruit:
    def __init__(self, name):
        self.name = name
        self.image = pygame.image.load("../res/art/collectibles/fruit.png")

    def get_image(self):
        return self.image
