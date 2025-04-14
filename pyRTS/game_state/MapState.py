import pygame

"""
Long term, am thinking of defining a file format (or can just use json)
that defines all these paramters for each map. We can just load from map_name.
"""


class MapState:
    def __init__(self, map_name, map_size: pygame.math.Vector2):
        self.map_name = map_name
        self.map_size = map_size

    def load_map(self, map_name: str):
        raise NotImplementedError()
