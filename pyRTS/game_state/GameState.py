import MapState

"""
Master Class to store all game state
"""


class GameState:
    def __init__(self):
        self.map = None

    def set_map(self, map_state: MapState):
        self.map = map_state
