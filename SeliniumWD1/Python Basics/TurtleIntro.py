import turtle                # allows us to usr turtle librarys
import time

class TurtleAlex():

    def testAlex(self):
        window = turtle.Screen()     # creates a graphic window instance
        window.bgcolor("lightgreen") # set the window background color
        alex = turtle.Turtle()       # create a turtle named alex having a pen at its tip
        alex.color("blue")           # make tess blue
        alex.pensize(3)              # set the width of her pen

        alex.forward(150)            # tells alex to move forwards 150 units
        alex.left(90)                # turn 90 degree
        alex.forward(150)            # move forward 150 units
        alex.left(90)
        alex.forward(150)
        alex.left(90)
        alex.forward(150)
        print("Alex moved!!")
        time.sleep(2)

        alex.salary = 50000          # assigns a variable named salary in alex
        print("alex's salary: " + str(alex.salary))
        time.sleep(3)

ff = TurtleAlex()
ff.testAlex()