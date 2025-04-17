import pygame
from pyRTS.game_state import GameState


class Camera:
    def __init__(
        self,
        size: pygame.math.Vector2,
        state: GameState,
        pos: pygame.math.Vector2 = pygame.math.Vector2(0, 0),
    ):
        self.size = size
        self.state = state
        self.pos = pos

    def render(self, )
