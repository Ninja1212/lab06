CPSC 110 Lab 5 Due: Fri Oct. 11, 2024, 9:00am

General Lab Instructions:
1. All assignments will be submitted through Canvas. If you submit multiple times, the most recent submission will be graded.

2. You will typically explain your code from the last lab to the instructor at the beginning of the next lab to receive your full marks and feedback.

3. If you work with other people, list all of your names on the assignment. Each assignment will specify how many others you can work with.

4. Please review the collage’s plagiarism policies. As a general rule, copy/paste should never be used for any code. Ever. You may discuss topics with other students and reference online materials, but the final assignment must be written by the student. If you reference materials/people besides the textbook/instructor then cite this in a file contributions.txt. Full citations are not necessary, a bullet point list of the materials/people that you references is suitable.

5. Code will be graded for functionality as well as quality. This means code that should be easy to read with descriptive variable names and appropriate comments.

6. You should aim to stick to the concepts we have already covered in class. For example, do not use ”if statements” on assignment 1 since it was not covered in lecture 1. If you have studied programming elsewhere then it is tempting to jump ahead, but full marks will only be given to assignments that are focused on this course’s content.

7. Code that cannot run successively in Python 3 will receive a zero. Make sure you are using the correct python version and allow yourself enough time for thorough testing.

8. At the start of each assignment will be a list of the required files for submission. All files should be com- pressed in one zip folder named <studentnumber>_<yourname >_LAB < number >_CPSC110.zip. For example: 21870110_LUKESKYWALKER_LAB01_CPSC110.zip

Lab 05 intructions:
- Total points: 30
- Due: Fri Oct. 11, 2024, 9:00am
- Required files:
  - food.py
  - game.py
  - run.py
  - keys.py
  - player.py
  - tests.py
  - .gitignore
  - README.md

# Lab 05: How to Design Worlds

Download the full code at [https://github.com/CC-CPSC-110/lab05](https://github.com/CC-CPSC-110/lab05) by using your GitHub Desktop app.

Today we are building our first interactive game. 

All tasks are marked with `TODO`. They are the minimum places where you will have to make changes. However, you can and should make more changes than the `TODO` marks if the problem requires it.

Start by running `run.py` and observing the already-created behaviour of the system. It's best to trace through a file and see if you can figure out which functions call which other functions. Use the debugger or simply `ctrl-click` or `cmd-click` on function definitions to find where they go.

You should see a ball that you can move around the screen by pressing the `WASD` keys. 

## Run tests and keep organized

Take a look at `tests.py` and run it. You'll see that the tests have been organized into a long list and there are many of them. This is typical of a complex software system.

You'll also notice that you **do not need to run** `run.py` to get the tests to work. Instead, we are **simulating** each function call. Since we know the input and output types precisely, we are able to test the functions on their own.

Particularly when you start your group project, the need for tests will become quickly apparent. You want a guarantee that functions will work as intended, or development will quickly go in circles. We've been getting into the habit of test-driven development, but when large systems get to be complex, it is very, very important to have tests.

The file system is carefully organized. Do your work where the TODOs indicate to keep organization simple.

## Problem 1: Move a `Food`

Find the `TODO` mark in `food.py` where it tells you to write the method for moving a `Food`. 

Using the full HtDF recipe, completing the method with fully-defined tests. You can use the solution from lecture, or come up with your own system for moving.

## Problem 2: Populate and draw `Food`

Find the `TODO` mark in `food.py` where it tells you to write the method for populating a `FoodList`. Also note the `TODO` in `run.py` where it asks you to draw your `Food`.

Using the full HtDF recipe, completing the method with fully-defined tests. You can use the solution from lecture, or come up with your own system for populating the FoodList.

## Problem 3: Move `Player` with mouse

Find the `TODO` mark in `player.py` where it tells you to write the method for moving a `Player` to a mouse position. Also note the `TODO` in `run.py`.

Using the full HtDF recipe, completing the method with fully-defined tests. You can use the solution from lecture, or come up with your own system for moving the `Player` to the mouse.

Problem 4: Check whether `Player` is touching `Food`

Find the `TODO` mark in `player.py` where it tells you to write the method for checking whether a `Player` is touching `Food`. Also note the `TODO` in `run.py`.

Using the full HtDF recipe, completing the method with fully-defined tests. Hint: you can use a version of the `distance` method we've been implementing for `Apartment`, but you'll have to make a change based on `size` for both the `Player` and the `Food`.

## Problem 5: Update `FoodList` and `count` in `Player`

When the `Player` consumes a `Food`, its `count` needs to change and the `FoodList` needs to be updated to remove that `Food`. You'll need to figure out how to update both states.

There are a few ways to complete this task. Top marks will be given to solutions that are clear, testable, and well-documented.

Using the full HtDF recipe, completing the method with fully-defined tests.

## Problem 6: Change `Player` size based on `Food` count

Find the `TODO` mark in `player.py` where it tells you to write the method for changing `Player` size based on `Food` count. Also note the `TODO` in `run.py`.

Using the full HtDF recipe, completing the method with fully-defined tests.

## Problem 7: Playtest and Improve

Congrats! You now have a very simple game. Play it a few times. Does it work the way you want or expect it to?

Choose one thing you'd like to improve. Use the HtDF recipe for anything you improve. You cannot remove any functionalities, only add them.
