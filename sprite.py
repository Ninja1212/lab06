"""A super-class for anything onscreen that moves."""
import math
from typing import Tuple 
from typing_extensions import Self
from dataclasses import dataclass

@dataclass
class Sprite:
    """A class for anything that is drawn on screen."""
    x: int
    y: int
    size: int
    
    # TODO: Refactor Character and Food to extend Sprite.

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
