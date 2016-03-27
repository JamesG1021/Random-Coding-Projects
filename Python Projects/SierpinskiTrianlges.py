import turtle
from math import pi, cos, sin, radians

def drawTriangle(points,color,t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0],points[0][1])
    t.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,t):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],t)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, t)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, t)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, t)

def sierpinski2(points,degree,t):
    colormap = ['cyan','cyan','cyan','cyan','cyan']
    drawTriangle(points,colormap[degree],t)
    if degree > 0:
        sierpinski2([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, t)
        sierpinski2([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, t)
        sierpinski2([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, t)

def grow_tree(t, x1, y1, branch_radius, angle, depth):
    t.color('brown')
    t.pensize(depth)  # depth is what controls the iterations of the branch
    if depth < 1:
        t.color("green")
    bend_angle = pi/4
    branch_ratio = .6
    x2 = x1 + cos(angle) * branch_radius
    y2 = y1 + sin(angle) * branch_radius
    t.ht()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)
    if depth: # depth must be greater than 0 to branch
        grow_tree(t, x2, y2, branch_radius * branch_ratio, angle + bend_angle, depth - 1)# branch to the left
        grow_tree(t, x2, y2, branch_radius * branch_ratio, angle - bend_angle, depth - 1)  # branch to the right

def grow_tree2(t, x1, y1, branch_radius, angle, depth):
    t.color('brown')
    t.pensize(depth)  # depth is what controls the iterations of the branch
    if depth < 1:
        t.color("green")
    bend_angle = pi/4
    branch_ratio = .6
    x2 = x1 + cos(angle) * branch_radius
    y2 = y1 + sin(angle) * branch_radius
    t.ht()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)
    if depth: # depth must be greater than 0 to branch
        grow_tree(t, x2, y2, branch_radius * branch_ratio, angle + bend_angle, depth - 1)# branch to the left
        grow_tree(t, x2, y2, branch_radius * branch_ratio, angle - bend_angle, depth - 1)  # branc

def main():
   t = turtle.Turtle()
   wn = turtle.Screen()
   wn.bgcolor('cyan')
   depth = 8
   depth2 = 4
   wn.title("Binary Tree, depth = "+str(depth))
   trunk_height = 100
   trunk_height1 = -45
   myPoints = [[-300,100],[-200,250],[-100,100],[100,0]]
   sierpinski(myPoints,4,t)
   myPoints = [[-200,-50],[-100,100],[0,-50],[100,0]]
   sierpinski2(myPoints,4,t)
   myPoints = [[0,-50],[200,-50],[100,-200],[100,0]]
   sierpinski(myPoints,4,t)
   grow_tree(t,100,-50,trunk_height,pi/2,depth)
   grow_tree2(t,100,-50,trunk_height1,pi/2,depth2)
   t.penup()
   t.ht()
   t.goto(-100,200)
   t.color('black')
   t.write("'blue','red','green',white',yellow'", font=("Arial", 15, "normal"))
   wn.exitonclick()

main()
