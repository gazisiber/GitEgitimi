import turtle
import math
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("#0a0e27")
screen.tracer(0)

# Modern color palette
colors = ["#FF006E", "#FB5607", "#FFBE0B", "#8338EC", "#3A86FF", "#06FFA5", "#FF4365"]
pastel_colors = ["#FFB3D9", "#FFD700", "#FFD966", "#D8BFD8", "#ADD8E6", "#98FB98", "#FFB6C1"]

# Draw animated background particles
def draw_background_particles():
    particle_drawer = turtle.Turtle()
    particle_drawer.hideturtle()
    particle_drawer.speed(0)
    
    for _ in range(80):
        x = random.randint(-500, 500)
        y = random.randint(-400, 400)
        size = random.randint(2, 8)
        color = random.choice(pastel_colors)
        
        particle_drawer.penup()
        particle_drawer.goto(x, y)
        particle_drawer.pencolor(color)
        particle_drawer.pensize(size)
        particle_drawer.dot(size)

# Draw a petal with modern design
def draw_petal(pen, x, y, size, angle, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(angle)
    pen.pendown()
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.pensize(2)
    
    pen.begin_fill()
    for _ in range(2):
        pen.forward(size)
        pen.right(90)
        pen.forward(size // 2)
        pen.right(90)
    pen.end_fill()

# Draw geometric flower with animation
def draw_geometric_flower(pen, rotation=0, color_offset=0):
    center_x, center_y = 0, 0
    num_petals = 12
    petal_size = 80
    
    # Draw outer petals (larger)
    for i in range(num_petals):
        angle = (360 / num_petals) * i + rotation
        x = center_x + 120 * math.cos(math.radians(angle))
        y = center_y + 120 * math.sin(math.radians(angle))
        color = colors[(i + color_offset) % len(colors)]
        
        pen.penup()
        pen.goto(x, y)
        pen.setheading(angle)
        pen.pendown()
        pen.pencolor(color)
        pen.fillcolor(color)
        pen.pensize(3)
        
        # Draw petal as rounded shape
        pen.begin_fill()
        for _ in range(2):
            pen.circle(petal_size // 2, 90)
            pen.right(90)
        pen.end_fill()
    
    # Draw middle circle with pattern
    for i in range(6):
        angle = (360 / 6) * i + rotation
        x = center_x + 50 * math.cos(math.radians(angle))
        y = center_y + 50 * math.sin(math.radians(angle))
        color = pastel_colors[(i + color_offset) % len(pastel_colors)]
        
        pen.penup()
        pen.goto(x, y)
        pen.pencolor(color)
        pen.fillcolor(color)
        pen.begin_fill()
        pen.circle(25)
        pen.end_fill()
    
    # Draw center core with gradient effect
    pen.penup()
    pen.goto(center_x, center_y)
    pen.pencolor("#FF006E")
    pen.fillcolor("#FF006E")
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()
    
    # Draw inner details
    pen.penup()
    pen.goto(center_x, center_y)
    pen.pencolor("#FFBE0B")
    pen.fillcolor("#FFBE0B")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()

# Main drawing with animation
draw_background_particles()

flower_pen = turtle.Turtle()
flower_pen.hideturtle()
flower_pen.speed(0)

star_pen = turtle.Turtle()
star_pen.hideturtle()
star_pen.speed(0)

# Animation loop
rotation_angle = 0
color_shift = 0

try:
    while True:
        # Clear the screen
        screen.clear()
        screen.bgcolor("#0a0e27")
        
        # Redraw background particles
        draw_background_particles()
        
        # Draw flower with rotation and color shift
        draw_geometric_flower(flower_pen, rotation_angle, color_shift)
        
        # Draw decorative stars
        for i in range(20):
            angle = (360 / 20) * i + rotation_angle
            x = 250 * math.cos(math.radians(angle))
            y = 250 * math.sin(math.radians(angle))
            
            star_pen.penup()
            star_pen.goto(x, y)
            star_pen.pencolor(colors[(i + color_shift) % len(colors)])
            star_pen.pensize(2)
            
            # Draw small star
            star_angle = rotation_angle
            star_pen.setheading(star_angle)
            for _ in range(5):
                star_pen.forward(15)
                star_pen.right(144)
        
        screen.update()
        
        # Update animation parameters
        rotation_angle = (rotation_angle + 3) % 360
        color_shift = (color_shift + 1) % len(colors)
        
        # Control animation speed
        time.sleep(0.05)
        
except KeyboardInterrupt:
    pass

turtle.done()