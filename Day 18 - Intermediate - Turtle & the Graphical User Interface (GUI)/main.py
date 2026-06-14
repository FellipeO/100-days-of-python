# import colorgram
# extracted_colors = colorgram.extract("image.jpg",30)
# def extract_color (num, e_colors):
#     return tuple([e_colors[num].rgb.r, e_colors[num].rgb.g, e_colors[num].rgb.b])
# for i in range(len(extracted_colors)):
#     color_list.append(extract_color(i, extracted_colors))
# print(color_list)
import random
import turtle

color_list = [(232, 251, 242), (198, 12, 32), (250, 237, 18), (39, 76, 189), (39, 217, 68), (238, 227, 5),
              (229, 159, 46), (28, 40, 157), (214, 75, 13), (16, 154, 16), (198, 15, 11), (243, 34, 165),
              (229, 17, 121), (69, 10, 30), (61, 15, 8), (224, 141, 209), (10, 97, 61), (221, 161, 8),
              (49, 213, 231), (18, 19, 44), (11, 227, 239), (237, 156, 219), (83, 74, 212), (74, 213, 166),
              (81, 234, 201), (57, 233, 241), (4, 68, 42)]

def draw_circle ():
    """Draw and fill a circle"""
    with nat.fill():
        nat.circle(20)

nat = turtle.Turtle()
nat.hideturtle()
nat.speed("fastest")
screen = turtle.Screen()
screen.colormode(255)

for y in range (-350, 350, 70):
    nat.teleport(-350, y)
    for _ in range (10):
        nat.color(random.choice(color_list))
        draw_circle()
        nat.penup()
        nat.forward(70)
        nat.pendown()




screen.exitonclick()