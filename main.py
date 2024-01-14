import turtle as t
import random

# import colorgram

#
# colors = (colorgram.extract("Hirst - painting.jpg",40))
#
# rgb_colors_list = []
#
# for i in range(0,len(colors)):
#     red = (colors[i].rgb.r)
#     green = (colors[i].rgb.g)
#     blue = (colors[i].rgb.b)
#
#     rgb_colors_list.append((red,green,blue))
#
#
# print(rgb_colors_list)

fetched_colors = [(207, 158, 96), (234, 213, 100), (41, 104, 144), (130, 168, 194), (149, 79, 57), (202, 137, 162), (149, 65, 82), (25, 40, 55), (205, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 119), (60, 115, 91), (26, 45, 37), (224, 170, 187), (62, 45, 34), (90, 155, 104), (43, 161, 183), (226, 175, 168), (237, 212, 7), (13, 97, 74), (42, 60, 99), (99, 126, 168), (180, 189, 211), (172, 204, 183), (62, 35, 44), (102, 43, 58), (108, 46, 38), (158, 205, 215), (77, 70, 37), (10, 85, 106)]

timmy = t.Turtle()
timmy.speed(0)

# For - First row:

def painting(size_of_dots, space_dots, number_of_rows, number_of_columns):

# Set centered initial position:

    timmy.penup()

    initial_x_position = ((number_of_rows / 2) * space_dots) * -1
    initial_y_position = ((number_of_columns / 2) * space_dots) * -1

    timmy.setpos(initial_x_position, initial_y_position)

    timmy.pendown()

    # Primer for j grafica cada fila y luego con el for i se grafica cada columna

    for i in range(0,number_of_columns):
        for j in range(0,number_of_rows+1):
            print(timmy.pos())
            x_position = (initial_x_position) + j * space_dots
            y_position = (initial_y_position) + i * space_dots
            timmy.color(random.choice(fetched_colors))
            timmy.dot(size_of_dots)
            timmy.penup()
            timmy.setpos(x_position,y_position)
            timmy.pendown()
            timmy.dot(size_of_dots)

screen = t.Screen()
screen.colormode(255)

painting(20, 50, 15, 15)



screen.exitonclick()





