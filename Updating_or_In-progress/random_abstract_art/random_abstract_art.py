import math
import random
import colorgram

import turtle as turtle_module
turtle_module.colormode(255)
franklin = turtle_module.Turtle()

franklin.shape("turtle")
franklin.speed("fastest")
image_colors = colorgram.extract('image.jpg', 100)
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in image_colors]

turtle_module.Screen().bgcolor("black")
print(turtle_module.screensize(10000, 10000))

# print(set(rgb_colors))
# franklin.color("green")
# colors = ["red", "blue", "green", "yellow", "purple", "orange", "grey", "pink", "black"]


def dashing_line(dash_length, num_of_dashes, direction=0, pen_width=None):
    franklin.setheading(direction)
    if pen_width is None:
        pass
    else:
        franklin.width(pen_width)
    for _ in range(num_of_dashes):
        franklin.color(random.choice(rgb_colors))
        random.choice(rgb_colors)
        franklin.forward(dash_length)
        franklin.penup()
        franklin.forward(dash_length)
        franklin.pendown()


# dashing_line(10, 5)


def make_symmetrical_equilateral_polygon(num_of_equal_edges, perimeter_size, pen_width=None):
    if pen_width is None:
        pass
    else:
        franklin.width(pen_width)
    franklin.color(random.choice(rgb_colors))
    length = perimeter_size/num_of_equal_edges
    if num_of_equal_edges > 2:
        for edge in range(num_of_equal_edges):
            franklin.forward(length)
            franklin.left(360/num_of_equal_edges)
    else:
        print("A polygon must have at least 3 sides. Please pass in a higher number.")

# make_symmetrical_equilateral_polygon(7, 200, 5)


def polygon_image_frame(frame_diagonal, num_of_equal_edges, perimeter_size, num_of_frames=1, pen_width=None):
    if pen_width is None:
        pass
    else:
        franklin.width(pen_width)     
    make_symmetrical_equilateral_polygon(num_of_equal_edges, perimeter_size)
    for _ in range(num_of_frames):
        interior_angle = 180 - (360/num_of_equal_edges)
        escape_angle_for_outside_border = (360 - interior_angle)/2
        franklin.right(escape_angle_for_outside_border)
        franklin.penup()
        franklin.forward(frame_diagonal)
        franklin.pendown()
        franklin.left(escape_angle_for_outside_border)
        hypotenuse = frame_diagonal
        opposite_angle = escape_angle_for_outside_border - 90
        opp_length = hypotenuse*math.sin(math.radians(opposite_angle))
        extra_length = num_of_equal_edges*2*opp_length
        perimeter_size = perimeter_size + extra_length
        make_symmetrical_equilateral_polygon(num_of_equal_edges, perimeter_size)

# polygon_image_frame(10, 7, 100, 3, 5)


def random_walk(num_of_turns, pen_width=None):
    franklin.width(pen_width)
    franklin.speed(100)
    directions = [90, 180, 270, 360]
    for _ in range(num_of_turns):
        franklin.setheading(random.choice(directions))
        franklin.color(random.choice(rgb_colors))
        franklin.forward(25)

# random_walk(100, 10)


def draw_spirograph(gap_space, circle_size):
    franklin.speed(100)
    if 360 % gap_space != 0:
        print("Please enter a number divisible of 360.")
        return
    circle_count = int(360 / gap_space)
    for _ in range(circle_count):
        franklin.color(random.choice(rgb_colors))
        franklin.circle(circle_size)
        franklin.setheading(franklin.heading() + gap_space)

# draw_spirograph(1,10)


def dot_portrait(dot_size, number_of_dots, dots_per_row, screen_setting=None):
    if number_of_dots % dots_per_row != 0:
        print("Please enter 2 divisible numbers for the portrait's completion.")
        return
    franklin.penup()
    if screen_setting is None:
        pass
    else:
        franklin.setheading(206)
        franklin.forward(705)
        franklin.setheading(0)
    for dot_count in range(1, number_of_dots + 1):
        franklin.dot(dot_size, random.choice(rgb_colors))
        franklin.forward(50)
        if dot_count % dots_per_row == 0:
            franklin.setheading(90)
            franklin.forward(50)
            franklin.setheading(180)
            franklin.forward(dots_per_row * 50)
            franklin.setheading(0)


# dot_portrait(20, 100, 10, "corner")



# 2, 3, 3, 4, 5
# art = [random_walk, dot_portrait, make_symmetrical_equilateral_polygon, dashing_line, polygon_image_frame]

# random_walk(num_of_turns, pen_width=None)
# dot_portrait(dot_size, number_of_dots, dots_per_row, screen_setting=None)
# make_symmetrical_equilateral_polygon(num_of_equal_edges, perimeter_size, pen_width=None)
# dashing_line(dash_length, num_of_dashes, direction=0, pen_width=None)
# polygon_image_frame(frame_diagonal, num_of_equal_edges, perimeter_size, num_of_frames=1, pen_width=None)


# random_walk(50, 5-10)
# dot_portrait(10-20, 50-100, 5-10, screen_setting=None)
# make_symmetrical_equilateral_polygon(3-10, 200-300, 10)
# dashing_line(5-10, 3-7, random.choice(range(361)), 5-10)
# polygon_image_frame(10, 3-10, 100, 2-5, 5)


pen_width = 10


dashing_line(random.choice(range(15, 20)), random.choice(range(10, 15)), random.choice([0, 90, 180, 270]), pen_width)

no_of_dots = 1
dots_in_row = 3
while no_of_dots % dots_in_row != 0:
    no_of_dots = random.choice(range(50, 101))
    dots_in_row = random.choice(range(5, 10))
dot_portrait(random.choice(range(5, 21)), no_of_dots, dots_in_row)

random_walk(50, pen_width) # only black ink

make_symmetrical_equilateral_polygon(random.choice(range(3, 10)), random.choice(range(200, 300)), pen_width) # only black ink

dashing_line(random.choice(range(15, 20)), random.choice(range(10, 15)), random.choice([0, 90, 180, 270]), pen_width)

polygon_image_frame(15, random.choice(range(3, 10)), 100, random.choice(range(2, 5)), pen_width)

random_walk(50, pen_width)

gap = 33
while 360 % gap != 0:
    gap = random.choice(range(0, 361))
franklin.width(5)
draw_spirograph(gap, 30)


def random_abstract(art_pieces):
    # 2, 3, 3, 3, 5
    art = [random_walk, dashing_line, dot_portrait, make_symmetrical_equilateral_polygon, polygon_image_frame]
    for piece in range(art_pieces):
        art_choice = random.choice([0, 1, 2, 3, 4])
        if art_choice in [0, 1]:
            parameter = (30, 10)
        elif art_choice in [2, 3]:
            parameter = (9, 100, 10)
        elif art_choice == 4:
            parameter = (20, 7, 500, 3, 5)
        print(parameter)
        x = art[art_choice]
        print(x)


# random_abstract(2)


franklin.hideturtle()
screen = turtle_module.Screen()
screen.exitonclick()











