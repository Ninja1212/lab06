"""Test suite for game."""
import pygame
from cs110 import expect, summarize
import game
import player
import keys
import food
import opponent
import sprite

#------------------------------------------------------------------------------#
# Setup: Run these before all tests.
#------------------------------------------------------------------------------#
test_game = game.Game(
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
                        "d": "RIGHT"
        },
    )

test_player_1 = player.Player(x=100, y=100, size=10, speed=10, color="red")
test_player_2 = player.Player(x=100, y=100, size=10, speed=10, color="red")
test_player_3 = player.Player(x=100, y=100, size=10, speed=10, color="red")
test_player_4 = player.Player(x=100, y=100, size=10, speed=10, color="red")

test_player_UP = player.Player(x=100, y=  0, size=10, speed=10, color="red")
test_player_DN = player.Player(x=100, y=200, size=10, speed=10, color="red")
test_player_LT = player.Player(x=200, y=100, size=10, speed=10, color="red")
test_player_RT = player.Player(x=  0, y=100, size=10, speed=10, color="red")

"""
Opponent Tests(not working):
test_opponent_1 = opponent.Opponent(x=100, y=100, size=10, speed=10, color="blue")
test_opponent_2 = opponent.Opponent(x=100, y=200, size=10, speed=10, color="blue")
test_opponent_3 = opponent.Opponent(x=200, y=100, size=10, speed=10, color="blue")
test_opponent_4 = opponent.Opponent(x=100, y=100, size=10, speed=10, color="blue")
"""
#------------------------------------------------------------------------------#
# Test player.move (& opponent.move)
#------------------------------------------------------------------------------#
expect(test_player_1.move(10, ["UP"]),    test_player_UP)
expect(test_player_2.move(10, ["DOWN"]),  test_player_DN)
expect(test_player_3.move(10, ["RIGHT"]), test_player_LT)
expect(test_player_4.move(10, ["LEFT"]),  test_player_RT)

"""
Opponent Tests(not working/need help):
expect(test_opponent_1.move(10, ["UP"]),    test_opponent_UP)
expect(test_opponent_2.move(10, ["DOWN"]),  test_opponent_DN)
expect(test_opponent_3.move(10, ["RIGHT"]), test_opponent_LT)
expect(test_opponent_4.move(10, ["LEFT"]),  test_opponent_RT)
"""
#------------------------------------------------------------------------------#
# Test player.directions
#------------------------------------------------------------------------------#
expect(keys.directions(test_game.keymap, ["w"]),      ["UP"])
expect(keys.directions(test_game.keymap, ["s"]),      ["DOWN"])
expect(keys.directions(test_game.keymap, ["a"]),      ["LEFT"])
expect(keys.directions(test_game.keymap, ["d"]),      ["RIGHT"])
expect(keys.directions(test_game.keymap, ["w", "a"]), ["UP", "LEFT"])
expect(keys.directions(test_game.keymap, ["w", "d"]), ["UP", "RIGHT"])
expect(keys.directions(test_game.keymap, ["s", "a"]), ["DOWN", "LEFT"])
expect(keys.directions(test_game.keymap, ["s", "d"]), ["DOWN", "RIGHT"])


#------------------------------------------------------------------------------#
# Test keys.pressed_keys
#------------------------------------------------------------------------------#
expect(keys.pressed_keys((False,) * 8   + (True,) * 2), ['backspace', 'tab'])
expect(keys.pressed_keys((False,) * 97  + (True,) * 3), ['a', 'b', 'c'])
expect(keys.pressed_keys((False,) * 100 + (True,) * 1), ['d'])


#------------------------------------------------------------------------------#
# Test game.tick
#------------------------------------------------------------------------------#
expect(test_game.tick(), test_game)


#------------------------------------------------------------------------------#
# Test player.move_to
#------------------------------------------------------------------------------#
test_player_move_mouse_1 = player.Player(x=150, y=200, size=10, speed=10, color="red")
test_player_move_mouse_2 = player.Player(x=0, y=0, size=10, speed=10, color="red")

test_player_mouse_1 = player.Player(x=150, y=100, size=10, speed=10, color="red")
test_player_mouse_2 = player.Player(x=100, y=100, size=10, speed=10, color="red")

# Move player to (150, 200) and (0, 0)
expect(test_player_mouse_1.move_to((150, 200)), test_player_move_mouse_1)
expect(test_player_mouse_2.move_to((0, 0)), test_player_move_mouse_2)


#------------------------------------------------------------------------------#
# Test player.eat
#------------------------------------------------------------------------------#
test_player_eat = player.Player(x=100, y=100, size=10, speed=10, color="red", count=0)

# Eat food and increment count
test_player_eat.eat()
expect(test_player_eat.count, 1)

# Eat again and increment count
test_player_eat.eat()
expect(test_player_eat.count, 2)


#------------------------------------------------------------------------------#
# Test player.resize
#------------------------------------------------------------------------------#
test_player_resize = player.Player(x=100, y=100, size=10, speed=10, color="red", count=5)
test_player_resize.resize()

# After resizing, size should be 10 + count (i.e., 15)
expect(test_player_resize.size, 15)

# Simulate eating food and resizing
test_player_resize.eat()
test_player_resize.resize()
expect(test_player_resize.size, 16)


#------------------------------------------------------------------------------#
# Test Food.move
#------------------------------------------------------------------------------#
test_food_move_1 = food.Food(x=100, y=100, size=10)
test_food_move_2 = food.Food(x=100, y=100, size=10)

# Move the food by (5, -5) and (-10, 10)
expect(test_food_move_1.move(5, -5), food.Food(x=105, y=95, size=10))
expect(test_food_move_2.move(-10, 10), food.Food(x=90, y=110, size=10))


#------------------------------------------------------------------------------#
# Test Food.distance
#------------------------------------------------------------------------------#
test_food_distance = food.Food(x=0, y=0, size=10)
test_player_dist = player.Player(x=0, y=10, size=10, speed=10, color="red")

# Calculate the distance between food and player
expect(test_food_distance.distance(test_player_dist), 10.0)

test_player_dist_2 = player.Player(x=3, y=4, size=10, speed=10, color="red")
# Calculate the distance between food and player (Pythagoras: 3^2 + 4^2 = 5^2)
expect(test_food_distance.distance(test_player_dist_2), 5.0)


#------------------------------------------------------------------------------#
# Test Food.hit
#------------------------------------------------------------------------------#
test_food_hit = food.Food(x=0, y=0, size=1)
test_player_hit_1 = player.Player(x=0, y=10, size=10, speed=10, color="red")
test_player_hit_2 = player.Player(x=0, y=11, size=10, speed=10, color="red")

# Player 1 should hit the food
expect(test_food_hit.hit(test_player_hit_1), True)

# Player 2 should not hit the food
expect(test_food_hit.hit(test_player_hit_2), False)

#------------------------------------------------------------------------------#
# Test FoodList.populate
#------------------------------------------------------------------------------#
test_sprite_list = sprite.SpriteList([])

# Populate with 5 food items within bounds (500, 500)
populated_sprite_list = test_sprite_list.populate(5, (500, 500))

# Expect 5 items in the list
expect(len(populated_sprite_list), 5)

# Check that all food items are within bounds
for sprite_item in populated_sprite_list:
    expect(0 <= sprite_item.x <= 500, True)
    expect(0 <= sprite_item.y <= 500, True)
    expect(sprite_item.size, 10)


#------------------------------------------------------------------------------#
# Test FoodList.eat
#------------------------------------------------------------------------------#
test_food_list_eat = food.FoodList([food.Food(x=0, y=0, size=10)])
test_player_eat = player.Player(x=0, y=0, size=10, speed=10, color="red")

# Player eats the food, expect the list to be empty and player count to increase
test_food_list_eat.eat(test_player_eat)
expect(len(test_food_list_eat.food), 0)
expect(test_player_eat.count, 1)
expect(test_player_eat.size, 11)  # Size should increase after eating


#------------------------------------------------------------------------------#
# Test FoodList.move
#------------------------------------------------------------------------------#
test_food_list_move = food.FoodList([food.Food(x=100, y=100, size=10), food.Food(x=100, y=100, size=10)])

# Move the food items in the list
test_food_list_move.move()

# Expect the food items to have moved slightly
for food_item in test_food_list_move.food:
    expect(99 <= food_item.x <= 101, True)
    expect(99 <= food_item.y <= 101, True)


#------------------------------------------------------------------------------#
# Summarize the tests
#------------------------------------------------------------------------------#
summarize()