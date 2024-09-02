# import colorgram

# colors = colorgram.extract('damien-hirst-severed-spots.jpg', 88)

# rgb_colors=[]

# for c in colors:
#     r=c.rgb.r
#     g=c.rgb.g
#     b=c.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)

#colour extraction code above


color_list=[(250, 228, 17), (199, 12, 35), (213, 13, 9), (232, 228, 5), (198, 68, 20), (32, 90, 188), (43, 212, 72), (234, 149, 41), (33, 30, 153), (240, 246, 251), (16, 22, 55), (66, 9, 49), (244, 39, 148), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (230, 164, 8), (15, 154, 22), (245, 59, 16), (98, 75, 9), (248, 11, 9), (223, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 213), (85, 76, 209), (85, 225, 235), (251, 8, 16), (241, 167, 157), (177, 180, 224), (31, 244, 165), (7, 81, 113), (15, 52, 248)]

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.setx(-150)
tim.sety(150)
for _ in range(10):
    for _ in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.fd(50)
        tim.pendown()
    tim.penup()
    tim.setx(-150)
    tim.sety(tim.ycor()-50)
    

t.mainloop()