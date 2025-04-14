import pygame
from pygame.time import Clock
from pyRTS.game_objects.BaseObject import BaseObject
from pyRTS.game_state import GameState, MapState


def main():
    state = GameState()
    map = MapState(pygame.math.Vector2(10000, 10000))
    state.set_map(map)

    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    bg = pygame.Surface(window.get_size())
    bg.fill((23, 123, 157))
    print(window.get_size())
    game_group = pygame.sprite.Group()
    game_object = BaseObject(
        pygame.math.Vector2(50, 50),
        pygame.math.Vector2(1, 1),
        image=pygame.transform.scale_by(pygame.image.load("assets/test/test01.png"), 5),
    )
    game_group.add(game_object)
    window.blit(bg)
    game_clock = Clock()

    running = True

    while running:
        game_group.clear(window, bg)
        events: list[pygame.Event] = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
        game_group.draw(window)
        game_group.update(0)
        pygame.display.flip()
        game_clock.tick(30)


if __name__ == "__main__":
    pygame.init()
    main()
