from graphics import *

def ponto(x, y, cor, win):
    pt = Point(x, y)
    pt.setFill(cor)
    pt.draw(win)

def CirclePoints(xc, yc, x, y, cor, win):
    ponto(xc + x, yc + y, cor, win)
    ponto(xc - x, yc + y, cor, win)
    ponto(xc + x, yc - y, cor, win)
    ponto(xc - x, yc - y, cor, win)
    ponto(xc + y, yc + x, cor, win)
    ponto(xc - y, yc + x, cor, win)
    ponto(xc + y, yc - x, cor, win)
    ponto(xc - y, yc - x, cor, win)


def CirculoPontoMedio(xc, yc, r, cor, win):
    x = 0
    y = r
    d = 3 - 2 * r


    while (y >= x):

        CirclePoints(xc, yc, x, y, cor, win)

        if (d > 0):
            y = y - 1
            d += 4 * (x - y) + 10
        else:
            d += 4 * x + 6

        x = x + 1

def main():

	xc = 230
	yc = 170
	r = 200
	cor = color_rgb(153, 204, 50)

	win = GraphWin("Circulo_PontoMedio", 500, 500)
	# win.setBackground(color_rgb(240, 240, 240))

	CirculoPontoMedio(xc, yc, r, cor, win)

	win.getMouse()  # pause for click in window
	win.close()


main()