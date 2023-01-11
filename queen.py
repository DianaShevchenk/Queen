import turtle as t
import queen_class
SIZE=30
t.speed(500)
queen8=queen_class.Queen(8)
res=queen8.get_result()

def square(x,y,z):
    t.penup()
    t.goto(x,y)
    t.pendown()

    if z%2==1:
        t.color('black','white')
    else:
        t.color('black','pink')

    t.begin_fill()

    for i in range(4):
        t.forward(SIZE)
        t.left(90)

    t.end_fill()
    
def set_color(f):
    if f%2==0:
        t.color('black','white')
    else:
        t.color('black','white')


def rectangle(x,y,w,h):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def polyline(p):
    t.penup()
    t.goto(x+p[0][0]*SIZE,y+p[0][1]*SIZE)
    t.pendown()
    t.begin_fill()
    for q in p:
        xq=x+q[0]*SIZE
        yq=y+q[1]*SIZE
        t.goto(xq,yq)
    t.end_fill()

def queen(x,y,z):  
    rectangle (x+SIZE*0.1,y+SIZE*0.1,SIZE*0.8,SIZE*0.1)
    rectangle (x+SIZE*0.15,y+SIZE*0.2,SIZE*0.7,SIZE*0.1)

    p=((0.15,0.3),(0.1,0.4),(0.9,0.4),(0.85,0.3))
    polyline(p)

    p=((0.1,0.4),(0.01,0.95),(0.4,0.4),
       (0.5,0.95),(0.6,0.4),
       (0.99,0.95),(0.9,0.4))
    polyline(p)



t.tracer(0)
t.hideturtle()
for j in range(8):
    for k in range(8):
        x=(j-4)*SIZE
        y=(k-4)*SIZE
        z=j*7+k
        square(x,y,z)
        if res[j][k]==1:
            queen(x,y,z)
t.update()
