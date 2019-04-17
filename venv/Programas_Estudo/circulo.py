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
	d = 3 - 2 * r;

	CirclePoints(xc, yc, x, y, cor, win);
	while (y >= x):
		x = x + 1

		if (d > 0):
			y = y - 1
			d = d + 4 * (x - y) + 10
		else:
			d = d + 4 * x + 6
			CirclePoints(xc, yc, x, y, cor, win)

def main():

	xc = 250
	yc = 250
	r = 100
	cor = color_rgb(153, 204, 50)

	# x1 = int(input("informe X inicial: "))
	# x2 = int(input("informe X final: "))
	# y1 = int(input("informe Y inicial: "))
	# y2 = int(input("informe Y final: "))

	win = GraphWin("Circulo_PontoMedio", 500, 500)
	# win.setBackground(color_rgb(240, 240, 240))

	CirculoPontoMedio(xc, yc, r, cor, win)

	win.getMouse()  # pause for click in window
	win.close()


main()