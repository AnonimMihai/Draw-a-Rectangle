import turtle
import time


def perimeterCLI():
    global side1    # side 1 means the length of the rectangle
    global side2    # side 2 means the width of the rectangle
    q1 = ""
    while True:
        try:
            side1 = int(input("What is the length of the the rectangle?(px)\n"))
            side2 = int(input("What is the width of the the rectangle?(px)\n"))
        except:
            print("Sorry but you entered something wrong.\nExit code: 534")
            time.sleep(5)
            exit()
        if side1 < side2:
            print("The length should be bigger than the width."
                  "\nPlease try again.")
            continue
        elif side1 == side2:
            print("This will become a square.")
            while True:
                q2 = ""
                q2 = input("Are you sure you want to continue?\n").lower()
                if q2 == "yes":
                    continue
                elif q2 == "no":
                    print("OK.")
                    break
                else:
                    print("Sorry but you entered something wrong. You can only enter ""Yes"" or ""No""."
                          "\nPlease try again.")
                    break
        else:
            break
    print(f"The rectangle's perimeter is: {(side1*2) + (side2*2)} px.\n")
    while True:
        q1 = input("Do you want the rectangle to be vertical or horizontal?\n").lower()
        if q1 == "horizontal":
            drawRectangleHor()
            break
        elif q1 == "vertical":
            drawRectangleVer()
            break
        else:
            print("Sorry but you entered something wrong. You can only enter ""Vertical"" or ""Horizontal""."
                  "\nPlease try again.")
            continue

# Function that draw the rectangle if option was chosen as "Horizontal"
def drawRectangleHor():
    canvas = turtle.Turtle()
    canvas.penup()
    canvas.setposition(x=-360, y=0)
    canvas.pendown()
    canvas.forward(side1)
    canvas.left(90)
    canvas.forward(side2)
    canvas.left(90)
    canvas.forward(side1)
    canvas.left(90)
    canvas.forward(side2)
    turtle.done()


# Function that draw the rectangle if option was chosen as "Vertical"
def drawRectangleVer():
    canvas = turtle.Turtle()
    canvas.penup()
    canvas.setposition(x=-360, y=0)
    canvas.pendown()
    canvas.forward(side2)
    canvas.left(90)
    canvas.forward(side1)
    canvas.left(90)
    canvas.forward(side2)
    canvas.left(90)
    canvas.forward(side1)
    turtle.done()
