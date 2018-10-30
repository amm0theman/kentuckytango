"""Represents player state with four booleans"""


class Command:
    def __init__(self):
        self.shoot: bool = False
        self.accel: bool = False
        self.right: bool = False
        self.left: bool = False
