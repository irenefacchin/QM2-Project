#Name: jeans_visualisation
#
#Description:
#This program draws t-shirts and jeans filled with colours according to their environmental impact 
#
#Date: December 2020
#
#First, import the GraphicsWindow elements from the ezraphics library to have access to the figures

from ezgraphics import GraphicsWindow

diff_co2 = 50
diff_water = 80

def main():

    # Create a graphics window (640 x 480 pixels):
    win = GraphicsWindow(640, 480)

#To draw the fast fashion pair of jeans

    # Draw the rectangle representing the CO2 emissions
    canvas = win.canvas()
    canvas.drawText(100,75,"Fast Fashion Jeans")
    canvas.setOutline("red")
    canvas.setFill("red")
    canvas.drawRect(100, 150, 40, 150)

    #Draw the middle part (half blue half red)
    canvas = win.canvas()
    canvas.setOutline("red")
    canvas.setFill("red")
    canvas.drawRect(140, 150, 40, 40)

    canvas = win.canvas()
    canvas.setOutline("blue")
    canvas.setFill("blue")
    canvas.drawRect(160, 150, 40, 40)
    
    # Draw the rectangle representing the water usage
    canvas = win.canvas()
    canvas.setOutline("blue")
    canvas.setFill("blue")
    canvas.drawRect(175, 150, 40, 150)

    

#To draw the sustainable pair of jeans

    # Draw the rectangle representing the CO2 emissions
    canvas = win.canvas()
    canvas.setOutline("black")
    canvas.drawText(300,75,"Sustainable Jeans")
    canvas.setOutline("green")
    canvas.setFill("white")
    canvas.drawRect(275, 150, 40, 150)

    canvas.setOutline("red")
    canvas.setFill("red")
    canvas.drawRect(275, 225, 40, 75)

    #Draw the middle part
    canvas = win.canvas()
    canvas.setOutline("green")
    canvas.setFill("white")
    canvas.drawRect(315, 150, 40, 40)

    #To remove the green line
    canvas.setOutline("white")
    canvas.drawLine(315,150, 315, 190)
    
    # Draw the rectangle representing the water usage
    canvas = win.canvas()
    canvas.setOutline("green")
    canvas.setFill("white")
    canvas.drawRect(355, 150, 40, 150)
    #To remove the green line
    canvas.setOutline("white")
    canvas.drawLine(355, 150, 355, 190)
    
    canvas.setOutline("blue")
    canvas.setFill("blue")
    canvas.drawRect(355, 270, 40, 30)

    #Draw the legend
    canvas = win.canvas()
    canvas.setOutline("red")
    canvas.setFill("red")
    canvas.drawRect(100, 350, 20, 20)
    canvas.drawText(125,355,"CO2 emissions")

    canvas = win.canvas()
    canvas.setOutline("blue")
    canvas.setFill("blue")
    canvas.drawRect(100, 325, 20, 20)
    canvas.drawText(125,330,"Water usage")

    #Draw the text
    canvas.setOutline("green")
    canvas.drawText(265, 175, "Saved CO2 emission and water")

    # Wait for the user to close the window
    win.wait()


if __name__ == "__main__":
    main()
