"""A super-class for anything onscreen that moves."""
import math
from typing_extensions import Self
from dataclasses import dataclass
from typing import List, Tuple
import random

@dataclass
class Sprite:
    """A class for anything that is drawn on screen."""
    # TODO: Refactor Character and Food to extend Sprite.
    
    x: int
    y: int
    size: int
    
    def direction(self, other: Self) -> Tuple[float, float]:
        # Step 1: Subtract the x and y coordinates of the two sprites to get the vector
        vector: Tuple[float, float] = (other.x - self.x, other.y - self.y)
        
        # Step 2: Compute the magnitude of the vector (ensure it's an int, so we can use floor later)
        magnitude: float = math.sqrt(vector[0]**2 + vector[1]**2)
        
        # Step 3: Normalize the vector (avoid division by zero)
        if magnitude == 0:
            return (0, 0)  # Return a zero vector if magnitude is zero
        
        # Step 4: Normalize and use floor to ensure the result is integer
        normalized_vector: Tuple[float, float] = (
            vector[0] / magnitude, 
            vector[1] / magnitude
        )
        
        return normalized_vector
    
@dataclass
class SpriteList:
    """A containing class for Sprite."""
    sprite: List[Sprite]


    def populate(self, amount: int, bounds: Tuple[int, int]) -> List[Sprite]:
        """
        Purpose: Populates the game world with a specified amount of sprites, placing them 
        randomly within the given bounds (width and height). This initializes a list of 
        sprites.
        
        Examples:
            sprite_list = SpriteList([])
            populate(sprite_list, 5, (500, 500)) -> List of 5 sprite objects within the 500x500 bounds
        """
        for i in range(amount):
            self.sprite.append(
                Sprite(
                    x=random.randint(0, bounds[0]), 
                    y=random.randint(0, bounds[1]),
                    size=10
                )
            )
        return self.sprite
