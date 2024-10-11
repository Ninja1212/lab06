"""A super-class for anything that is trying to win."""
import math
from typing import Tuple 
from typing_extensions import Self
from dataclasses import dataclass
from sprite import Sprite

@dataclass
class Character(Sprite):
    """A class for competing entities."""
    # TODO: refactor Player and Opponent to extend Character