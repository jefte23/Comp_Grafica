from graphics import *

def ROUND(a):
	return int(a + 0.5)

def drawDDA(x1,y1,x2,y2, win):
    x,y = x1,y1
    length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
    dx = (x2-x1)/float(length)
    dy = (y2-y1)/float(length)
    print ('x = %s, y = %s' % (((ROUND(x),ROUND(y)))))

    for i in range(length):
        x += dx
        y += dy

        pt = Point(x, y)
        pt.draw(win)
        print ('x = %s, y = %s' % (((ROUND(x),ROUND(y)))))


def main():

    x1 = 400
    x2 = 400
    y1 = 0
    y2 = 600

    # x1 = int(input("informe X inicial: "))
    # x2 = int(input("informe X final: "))
    # y1 = int(input("informe Y inicial: "))
    # y2 = int(input("informe Y final: "))

    win = GraphWin("My Window", 800, 600)
    #win.setBackground(color_rgb(240, 240, 240))

    # Chava variavel de bresenham
    drawDDA(x1, y1, x2, y2, win)

    win.getMouse()  # pause for click in window
    win.close()


main()