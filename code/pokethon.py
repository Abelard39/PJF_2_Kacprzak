import pygame
from pygame import Surface


class Pokethon:
    name: str
    image: Surface

    def __init__(self, pokemon_name, pokemon_image, next_evolution):
        self.name = pokemon_name
        self.image = pygame.image.load("../res/art/pokethons/" + pokemon_image + ".png")
        self.next_evolution = next_evolution

    def evolve(self):
        self.name = self.next_evolution.name
        self.image = self.next_evolution.image

    def get_image(self):
        return self.image
