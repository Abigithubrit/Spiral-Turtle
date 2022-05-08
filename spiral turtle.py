import turtle
tr=turtle.Turtle()
tr.shape('arrow')
tr.speed(50)
tr.pensize(2)
tr.getscreen().bgcolor('black')
tr.color('green')
tr.forward(40)
def newGraph():
    for i in range(25):
        tr.backward(i+6)
        tr.right(i)
        tr.forward(i)
    tr.right(-40)
    for i in range(25):
        tr.forward(i+6)
        tr.left(i)
        tr.backward(i)
for i in range(9):
    if i==2:
        tr.color('green')
    if i==4:
        tr.color('red')
    if i==6:
            tr.color('blue')
    if i==8:
         tr.color('pink')
    newGraph()           
        
