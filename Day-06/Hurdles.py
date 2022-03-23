
"""
CHALLENGES MADE IN REEBORG'S WORLD

*** Hurdles race 1 ***
Reeborg has entered a hurdles race. Make him run the course, following the path shown.

What you need to know
The functions move() and turn_left().
"""
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# for step in range(6):
#     jump()

"""
*** Hurdles race 2 ***
Reeborg has entered a hurdle race, but he does not know in advance how long the race is. Make him run the course, following a path similar to the one shown, but stopping at the only flag that will be shown after the race has started.
What you need to know
The functions move() and turn_left().
The condition at_goal() and its negation.
How to use a while loop.
Your program should also be valid for world Hurdles 1.
"""
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#     jump()

"""
*** Hurdles race 3 ***
Reeborg has entered a hurdle race. Make him run the course, following the path shown.

The position and number of hurdles changes each time this world is reloaded.
What you need to know
The functions move() and turn_left().
The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
How to use a while loop and an if statement.
Your program should also be valid for worlds Hurdles 1 and Hurdles 2.
"""
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

"""  
*** Hurdles race 4 ***
Reeborg has entered a hurdle race. Make him run the course, following the path shown.

The position, the height and the number of hurdles changes each time this world
is reloaded.

What you need to know
You should be able to write programs that are valid for worlds Around 4 and
Hurdles 3, and ot combine them for this last hurdles race.

Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3

"""
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()