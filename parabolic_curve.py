__author__ = 'Aly'

import sys
import turtle


def axes(t, screen_x):
    """
    Draws x axis and y axis
    """
    t.penup()
    t.home()


    t.pencolor('red')
    t.pendown()
    t.pensize(3)

    # Positive x axis
    t.forward(screen_x/2)
    t.right(90)
    t.penup()
    t.home()

    # Negative y axis
    t.pendown()
    t.right(90)
    t.forward(screen_x/2)
    t.penup()
    t.home()

    # Positive y axis
    t.pendown()
    t.right(90)
    t.back(screen_x/2)
    t.penup()
    t.home()

    # Negative x axis
    t.pendown()
    t.back(screen_x/2)
    t.penup()
    t.home()

    # Test line 1
    t.pencolor('black')
    t.setpos(screen_x/20, 0)
    t.pendown()
    t.setpos(0, screen_x/2)
    t.penup()

    # Test line 2
    t.setpos(0, screen_x/2 - 20)
    t.pendown()
    t.setpos(screen_x/10, 0)


    # # Test line 1
    # t.pencolor('black')
    # t.forward(10)
    # t.pendown()
    # t.left(93)
    # t.forward(200)
    # t.penup()
    #
    # # Test line 2
    # t.right(180)
    # t.forward(20)
    # t.left(5)
    # t.pendown()
    # t.forward(182)
    # t.penup()
    #
    # # Test line 3
    # t.setheading(0)
    # t.forward(20)
    # t.pendown()
    # t.left(107)
    # t.forward(160)
    # t.penup()
    #
    # t.setheading(270)
    # t.forward(20)
    # t.pendown()
    # t.left(26)
    # t.forward(148)



def lines(t, size, color):
    """
    Draw lines between the axes
    """
    t.pencolor(color)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)


def main():
    # Create screen and turtle.
    screen = turtle.Screen()
    screen.title('Parabolic curves with straight lines demo')
    screen_x, screen_y = screen.screensize()
    t = turtle.Turtle()

    # Uncomment to draw the graphics as quickly as possible.
    t.speed(0)

    # Draw the axes in the center of the screen
    axes(t, screen_x)

    # Draw a set of nested squares, varying the color.
    # The squares are 10%, 20%, etc. of half the size of the canvas.
    # colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    # t.pensize(3)
    # for i, color in enumerate(colors):
    #     square(t, (screen_y / 2) / 10 * (i+1), color)


    print('Hit enter/return key to exit')
    dummy = input()

if __name__ == '__main__':
    main()
