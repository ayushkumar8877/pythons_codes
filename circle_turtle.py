import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow','magenta','brown','indigo','voilet']
t = turtle.Pen()
turtle.bgcolor('black') #background color change krne ke liye ye line likha gya hai.
for i in range(100):
    t.pencolor(colors[i%6])
    t.circle(5*i) # 7 aur 8 line me palimdrome word ka logic lagaya hai[IS SE REVERSE CHECK BHI HOTA HAI ].
    t.circle(-5*i)
    t.forward(i)
    t.left(i)
turtle.exitonclick()