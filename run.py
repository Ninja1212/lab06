"""Example game showing a circle moving on screen."""
import pygame

from game import Game
from player import Player
from opponent import Opponent
from food import FoodList
from keys import pressed_keys, directions
from sprite import Sprite
from sprite import SpriteList
from typing import List, Tuple
import random

# TODO: Refactor draw to act on list of Sprite and draw all Sprites
def draw(game: Game, sprite_list: SpriteList):
    """
    Draws the player and game on the screen.
    
    Note that because this function has only side-effects, it would take a
    simulation to test. We can do that, but for this class, it's a bit much.
    Therefore, we don't have any tests for this.
    """

    for f in sprite_list.sprite:
        pygame.draw.circle(
            game.screen,
            "blue",
            pygame.Vector2(f.x, f.y),
            f.size
        )
    pygame.display.flip()
    

def main():
    """
    Run the main game loop.
    
    Note: again, because this is a function that only has side effects, there's
    not really a clean way to test this. Main loops usually follow a command
    pattern like this where they coordinate functions from different files.
    """
    
    # Define the Game state
    game = Game(
        screen     = pygame.display.set_mode((1280, 720)),
        clock      = pygame.time.Clock(),
        background = "purple",
        fps        = 60,
        running    = True,
        deltaT     = 0,
        keymap     = {
                        "w": "UP",
                        "s": "DOWN",
                        "a": "LEFT",
                        "d": "RIGHT",
        },
    )

    # Define the player
    player = Player(
              x     = game.screen.get_width() / 2,
              y     = game.screen.get_height() / 2,
              size  = 40,
              speed = 300,
              color = "red"
    )
    
    # TODO: Initialize the Opponent
    
    # Initialze pygame
    pygame.init()

    sprite_list = SpriteList([])
    sprite_list.populate(50, (game.screen.get_width(), game.screen.get_height()))
    
    food_list = FoodList([])
    food_list.populate(100, (game.screen.get_width(), game.screen.get_height()))
    
    # Run forever in a loop until quit
    while game.running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                pygame.quit()

        # Move the game clock forward
        game.tick()

        # Get pressed keys and directions
        pressed = pressed_keys(pygame.key.get_pressed())
        dirs = directions(game.keymap, pressed)
        
        # Move the player
        player.move(game.deltaT, dirs)

        # TODO: move the Opponent

        if pygame.mouse.get_focused():
            player.move_to(pygame.mouse.get_pos())
        
        food_list.eat(player)
        # TODO: make the Opponent eat Food too

        food_list.move()

        # Draw the game
        draw(game, sprite_list)


# Run the main function
if __name__ == "__main__":
    main()