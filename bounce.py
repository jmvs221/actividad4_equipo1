"""Bounce, a simple animation demo.

Exercises

1. Make the ball speed up and down.
2. Change how the ball bounces when it hits a wall.
3. Make the ball leave a trail.
4. Change the ball color based on position.
   Hint: colormode(255); color(0, 100, 200)

Modification: ball changes to a random color on each wall bounce.
"""

from random import choice, random
from turtle import (
    setup, hideturtle, tracer, up,
    clear, goto, dot, ontimer, done, color
)

from freegames import vector

# List of possible ball colors
COLORS = ['red', 'blue', 'green', 'cyan', 'orange', 'white', 'yellow']


def value():
    """Randomly generate value between (-5, -3) or (3, 5).

    Used to set the initial speed of the ball in each direction.
    The choice of 1 or -1 determines the starting direction.
    """
    return (3 + random() * 2) * choice([1, -1])


ball = vector(0, 0)

aim = vector(value(), value())

current_color = choice(COLORS)


def draw():
    """Move ball and draw game.

    This function runs repeatedly using ontimer.
    It moves the ball, checks for wall collisions,
    reverses direction on collision, picks a new random
    color on each bounce, and redraws the ball.
    """
    global current_color

    ball.move(aim)
    x = ball.x
    y = ball.y

    if x < -200 or x > 200:
        aim.x = -aim.x
        current_color = choice(COLORS)

    if y < -200 or y > 200:
        aim.y = -aim.y
        current_color = choice(COLORS)

    clear()
    color(current_color)
    goto(x, y)
    dot(10)

    ontimer(draw, 50)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()

# Start the animation loop
draw()
done()
