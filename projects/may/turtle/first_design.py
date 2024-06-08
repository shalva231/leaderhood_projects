import turtle


def draw_attractive_design1():
    pen = turtle.Turtle()
    pen.speed(20000)
    pen.color("lime")
    pen.width(0.5)
    turtle.bgcolor("black")

    pen2 = turtle.Turtle()
    pen2.speed(20000)
    pen2.color("lime")
    pen2.width(0.5)

    pen3 = turtle.Turtle()
    pen3.speed(20000)
    pen3.color("lime")
    pen3.left(180)
    pen3.width(0.5)

    pen4 = turtle.Turtle()
    pen4.speed(20000)
    pen4.color("lime") 
    pen4.left(180)
    pen4.width(0.5)


    start_size = 0

    for j in range(200):
        for s in range(4):
            pen2.forward(start_size)
            pen2.right(90)

            pen.forward(start_size)
            pen.right(90)

            pen3.forward(start_size)
            pen3.right(90)

            pen4.forward(start_size)
            pen4.right(90)



        pen2.right(5)
        pen.left(5)
        pen4.right(5)
        pen3.left(5)

        start_size +=1



# Call the function to draw the attractive design with black background
draw_attractive_design1()

turtle.done()