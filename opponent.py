"""A class for an Opponent."""
from dataclasses import dataclass
from sprite import Sprite
from typing_extensions import Self
from food import Food, FoodList
from character import Character

@dataclass
class Opponent(Character):
    """A competing player."""
    
    # TODO: Write an opponent class that extends Sprite.
    # Similarities with Player:
    #     Both classes are sprites & have the move method.
    # Differences with Player:
    #     The Opponent class doesn't have the attributes of speed & color.
    #     The Opponent class doesn't have the parameters of deltaT & dirs.
    #     The Opponent class doesn't have methods for move_to(for the cursor), eat, and resize.
    #     The Opponent's move method consists of a for loop, while the Player's move method consists of if statements.


    def move(self, food_list: FoodList) -> Self:
        closest: Food | None = None
        for f in food_list.food:
            if closest is None:
                closest = f
            if f.distance(self) < closest.distance(self):
                closest = f
        direction = self.direction(closest)
        self.x = self.x + (self.speed * direction[0])
        self.y = self.y + (self.speed * direction[1])
        return self
            
