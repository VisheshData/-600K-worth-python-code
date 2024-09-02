# 600k-dollars-worth-code


## 🎨 Recreate a $600,000 Damien Hirst Spot Painting with Code
Ever thought you could recreate a masterpiece worth $600,000 with just a few lines of code? Well, now you can! This Python program recreates Damien Hirst's iconic spot painting using nothing but the turtle module, a list of colors, and a little bit of coding magic.

## 🖌️ How It Works
This project extracts the color palette from one of Damien Hirst's famous spot paintings and then uses turtle graphics to place those colors on a canvas in a grid pattern, much like the original artwork. Who knew art could be this easy (and cheap)?

## 📦 Installation
Before running the code, make sure you have the necessary Python packages installed:

```bash

pip install colorgram.py
```
Also, ensure you have Python's turtle module ready to go.

## 💻 Usage
Start by extracting colors from the spot painting image using colorgram:

```python

import colorgram

colors = colorgram.extract('damien-hirst-severed-spots.jpg', 88)

rgb_colors = []

for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)  # Uncomment to see the extracted colors
```
Once you have your color palette, use the following code to generate the spot painting:

```python

import turtle as t
import random

# Use this color list based on the extracted colors
color_list = [(250, 228, 17), (199, 12, 35), (213, 13, 9), (232, 228, 5), (198, 68, 20),
              (32, 90, 188), (43, 212, 72), (234, 149, 41), (33, 30, 153), (240, 246, 251),
              (16, 22, 55), (66, 9, 49), (244, 39, 148), (65, 202, 229), (14, 205, 222),
              (63, 21, 10), (224, 19, 111), (230, 164, 8), (15, 154, 22), (245, 59, 16),
              (98, 75, 9), (248, 11, 9), (223, 140, 203), (68, 240, 161), (10, 97, 62),
              (5, 38, 33), (68, 219, 155), (238, 157, 213), (85, 76, 209), (85, 225, 235),
              (251, 8, 16), (241, 167, 157), (177, 180, 224), (31, 244, 165), (7, 81, 113),
              (15, 52, 248)]

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
    tim.sety(tim.ycor() - 50)

t.mainloop()
```
## 🖼️ Output
After running the code, you'll see a grid of colorful dots that look remarkably like a Damien Hirst spot painting. Congratulations! You've just created your very own $600,000 artwork.

## 🤔 Why?
Because who wouldn’t want to say they've recreated a Damien Hirst painting in their free time? Plus, it’s a fun way to practice Python coding with turtle graphics.

##📜 License
This project is licensed under the MIT License. Feel free to use, modify, and share this code as you like. Just don't try to sell it as an original Hirst—he might not appreciate that. 😉
