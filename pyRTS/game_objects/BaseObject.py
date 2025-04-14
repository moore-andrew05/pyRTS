import pygame

'''
Base Object that all game objects inherit from.

TODO:
    - Not sure how best to do the draw method. Should it accept a surface?
    - Position based on center of object?
'''


class BaseObject:

    def __init__(self, x: float, y: float
