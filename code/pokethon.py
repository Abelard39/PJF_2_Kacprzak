import pygame
from pygame import Surface


class Pokethon:
    pokemon_name: str
    pokemon_image: Surface
    pokemon_hp: int

    def __init__(self, pokemon_name, pokemon_image, next_evolution):
        self.pokemon_name = pokemon_name
        self.pokemon_image = pygame.image.load("../res/art/pokethons/" + pokemon_image + ".png")
        self.next_evolution = next_evolution

    def evolve(self):
        self.pokemon_name = self.next_evolution.pokemon_name
        self.pokemon_image = self.next_evolution.pokemon_image
        self.pokemon_hp = self.next_evolution.pokemon_hp

    def get_pokemon_image(self):
        return self.pokemon_image
