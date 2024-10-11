"""A class for an Opponent."""
from dataclasses import dataclass
from sprite import Sprite
from typing_extensions import Self
from food import Food, FoodList

@dataclass
class Opponent(Sprite):
    """A competing player."""

    # TODO: Write an opponent class that extends Sprite.

    def move(self, food_list: FoodList) -> Self:
        closest: Food | None
        for f in food_list.food:
            if closest is None:
                closest = f
            if f.distance(self) < closest.distance(self):
                closest = f
        direction = self.direction(closest)
        self.x = self.x + (self.speed * direction[0])
        self.y = self.y + (self.speed * direction[1])
        return self
            
