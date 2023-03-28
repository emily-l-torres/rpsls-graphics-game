#Emily Torres
#"Rock-Paper-Scissors-Lizard-Spock" Graphics Game!

import random
from graphics import *
import math, time

def rpsls():

    play = True
        
    win = GraphWin("Rock-Paper-Scissors-Lizard-Spock", 400, 300) 
    win.setBackground("sky blue")
    message = Text(Point(200,25), "Welcome to Rock-Paper-Scissors-Lizard-Spock!")
    message.setSize(15)
    message.draw(win)

    message2 = Text(Point(200,50), "Inspired by The Big Bang Theory")
    message2.setSize(15)
    message2.draw(win)

    message3 = Text(Point(200,75), "Give it your best shot!")
    message3.setSize(10)
    message3.draw(win)  #displays three messages at the top of the window

    b1 = RoundButton(win, 50, 200, 50, "red", "Rock")
    b2 = RoundButton(win, 125, 200, 50, "yellow", "Paper")
    b3 = RoundButton(win, 200, 200, 50, "green", "Scissors")
    b4 = RoundButton(win, 275, 200, 50, "blue", "Lizard")
    b5 = RoundButton(win, 350, 200, 50, "purple", "Spock")
    b6 = SquareButton(win, 375, 275, 40, "orange", "Quit") #displays buttons in the center/lower right of the window

    l = ["rock", "paper", "scissors", "lizard", "spock"] #list used in selecting a random move

    while True:

        p = win.getMouse()
        choice = random.choice(l) #selects a random move and correlates with player's object choice
        message2.undraw()
        message3.undraw() #undraws the messages displayed before gameplay

        if b1.overlaps(p) == True:
            b1.press()
            message.setText("You threw rock, I threw {}!".format(choice)) #displays the move selected by player
                                                                        #and random move selected by computer

            if choice == "paper": #possible outcome for random
                message2.setText("Paper covers Rock") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You lose, I win!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "lizard": #possible outcome for random
                message2.setText("Rock crushes Lizard") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You win, I lose!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "spock": #possible outcome for random
                message2.setText("Spock vaporizes Rock") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You lose, I win!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "scissors": #possible outcome for random
                message2.setText("And as it always has, Rock crushes Scissors") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You win, I lose!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "rock": #possible outcome for random
                message.setText("We both threw rock, so nobody wins!") #displays if computer and player choose the same object

        elif b2.overlaps(p) == True:
            b2.press()
            message.setText("You threw paper, I threw {}!".format(choice))

            if choice == "lizard": #possible outcome for random
                message2.setText("Lizard eats Paper") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You lose, I win!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "spock": #possible outcome for random
                message2.setText("Paper disproves Spock") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You win, I lose!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "rock": #possible outcome for random
                message2.setText("Paper covers Rock") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You win, I lose!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "scissors": #possible outcome for random
                message2.setText("Scissors cuts Paper") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You lose, I win!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "paper": #possible outcome for random
                message.setText("We both threw paper, so nobody wins!") #displays if computer and player choose the same object
            
        elif b3.overlaps(p) == True:
            b3.press()
            message.setText("You threw scissors, I threw {}!".format(choice))

            if choice == "lizard": #possible outcome for random
                message2.setText("Scissors decapitates Lizard") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You win, I lose!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "spock": #possible outcome for random
                message2.setText("Spock smashes Scissors") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You lose, I win!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "rock": #possible outcome for random
                message2.setText("And as it always has, Rock crushes Scissors") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You lose, I win!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "paper": #possible outcome for random
                message2.setText("Scissors cuts Paper") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You win, I lose!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "scissors": #possible outcome for random
                message.setText("We both threw scissors, so nobody wins!") #displays if computer and player choose the same object
            
        elif b4.overlaps(p) == True:
            b4.press()
            message.setText("You threw lizard, I threw {}!".format(choice))

            if choice == "scissors": #possible outcome for random
                message2.setText("Scissors decapitates Lizard") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You lose, I win!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "spock": #possible outcome for random
                message2.setText("Lizard poisons Spock") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You win, I lose!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "rock": #possible outcome for random
                message2.setText("Rock crushes Lizard") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You lose, I win!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "paper": #possible outcome for random
                message2.setText("Lizard eats Paper") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You win, I lose!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "lizard": #possible outcome for random
                message.setText("We both threw lizard, so nobody wins!") #displays if computer and player choose the same object
            
        elif b5.overlaps(p) == True:
            b5.press()
            message.setText("You threw spock, I threw {}!".format(choice))

            if choice == "scissors": #possible outcome for random
                message2.setText("Spock smashes Scissors") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You win, I lose!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "lizard": #possible outcome for random
                message2.setText("Lizard poisons Spock") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You lose, I win!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "rock": #possible outcome for random
                message2.setText("Spock vaporizes Rock") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You win, I lose!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "paper": #possible outcome for random
                message2.setText("Paper disproves Spock") # displays description of rule for the two selected objects
                message2.setSize(15)
                message2.draw(win)
                message3.setText("You lose, I win!") # displays if computer or player wins/loses
                message3.setSize(15)
                message3.draw(win)
            elif choice == "spock": #possible outcome for random
                message.setText("We both threw spock, so nobody wins!") #displays if computer and player choose the same object
            
        elif b6.overlaps(p) == True:
            b6.press()
            win.close()
            return #closes game
        
        else:
            message.setText("Click a button to throw your move!") #displays when player clicks anywhere within the window that's not a button

#---------------------------------------------------------------------

class Button:

    # constructor
    def __init__(self, win, shape, color, label):
        # draw the button
        shape.setFill(color)
        shape.draw(win)
        centerPoint = shape.getCenter()
        text = Text(centerPoint, label)
        text.draw(win)
        # information Button objects need to remember:
        self.shape = shape
        self.color = color

    def press(self):
        self.shape.setFill("gray")
        time.sleep(0.2)
        self.shape.setFill(self.color)

#---------------------------------------------------------------------

class RoundButton(Button):

    # constructor
    def __init__(self, win, centerX, centerY, diameter, color, label):
        # create the Circle object
        centerPoint = Point(centerX, centerY)
        radius = diameter / 2
        circle = Circle(centerPoint, radius)
        # call the superclass constructor to draw the button
        super().__init__(win, circle, color, label)
        # information RoundButton objects need to remember:
        self.x = centerX
        self.y = centerY
        self.radius = radius

    def overlaps(self, point):
        pointX = point.getX()
        pointY = point.getY()
        distance = math.sqrt((pointX - self.x)**2 + (pointY - self.y)**2)
        if distance <= self.radius:
            return True
        else:
            return False

#---------------------------------------------------------------------

class SquareButton(Button):

    # constructor
    def __init__(self, win, centerX, centerY, size, color, label):
        # create the Rectangle object
        leftX = centerX - size/2
        rightX = centerX + size/2
        topY = centerY - size/2
        bottomY = centerY + size/2
        rect = Rectangle(Point(leftX,bottomY), Point(rightX,topY))
        # call the superclass constructor to draw the button
        super().__init__(win, rect, color, label)
        # information SquareButton objects need to remember:
        self.x1 = leftX
        self.x2 = rightX
        self.y1 = topY
        self.y2 = bottomY

    def overlaps(self, point):
        pointX = point.getX()
        pointY = point.getY()
        if (pointX >= self.x1 and pointX <= self.x2 and
            pointY >= self.y1 and pointY <= self.y2):
            return True
        else:
            return False

#---------------------------------------------------------------------
