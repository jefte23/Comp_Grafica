from graphics import *


def ponto(x, y, cor, win):
    pt = Point(x, y)
    pt.setFill(cor)
    pt.draw(win)

def ROUND(a):
	return int(a + 0.5)

#def aviao(x1, y1, x2, y2, cor, win):


def main():
    #Localização do avião
    x1 = 120
    y1 = 100

    #destino do avião
    x2 = 450
    y2 = 300

    #cor = color_rgb(153, 204, 50)

    #win = GraphWin("aviao", 500, 500)

    #aviao(x1, y1, x2, y2, cor, win)

    aviao(x1, y1, x2, y2)

    #win.getMouse()  # pause for click in window
    #win.close()

main()