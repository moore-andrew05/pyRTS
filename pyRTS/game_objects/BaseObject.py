import pygame

"""
Base Object that all game objects inherit from.

TODO:
    - Not sure how best to do the draw method. Should it accept a surface?
    - Position based on center of object?
"""


class BaseObject(pygame.sprite.Sprite):
    def __init__(
        self,
        pos: pygame.math.Vector2,
        velocity: pygame.math.Vector2 = pygame.math.Vector2(0, 0),
        image: pygame.Surface | None = None,
    ):
        super().__init__()
        self.pos = pos
        self.velocity = velocity
        if image:
            self.image = image
        else:
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, dt: float):
        self.pos += self.velocity
        self.rect.center += self.velocity
