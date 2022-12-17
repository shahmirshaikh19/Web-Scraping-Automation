import time
import turtle

class ForLoop():
    def BasicLoop(self):

        print("this will execute first!")

        for n in range(3):
            print("Loop is running!!")
            print("Loop is still running!!")
            print("it's the " + str(n) +" itration")

        print("Now the loop is finished!!")

    def TurtleLoop(self):

        window = turtle.Screen()
        window.bgcolor("lightgreen")  # set the window background color
        alex = turtle.Turtle()  # create a turtle named alex having a pen at its tip
        alex.color("blue")  # make tess blue
        alex.pensize(3)

        distance = 50
        angle = 100
        for _ in range(20):
            alex.forward(distance)
            alex.right(angle)
            distance = distance + 10
            angle = angle - 2

        time.sleep(3)

ff = ForLoop()
ff.BasicLoop()
ff.TurtleLoop()