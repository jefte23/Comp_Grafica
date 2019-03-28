from graphics import *

# Function to put pixels a
# at subsequence points

def drawCircle(xc, yc, x, y, win):

	pt = Point(xc + x, yc + y)
	pt = Point(xc - x, yc + y)
	pt = Point(xc + x, yc - y)
	pt = Point(xc - x, yc - y)
	pt = Point(xc + y, yc + x)
	pt = Point(xc - y, yc + x)
	pt = Point(xc + y, yc - x)
	pt = Point(xc - y, yc - x)
	pt.draw(win)


# Function for circle - generation
# using Bresenham 's algorithm

def circleBres(xc, yc, r):
	x = 0
	y = r
	d = 3 - 2 * r;

	#drawCircle(xc, yc, x, y);
	while (y >= x):
		++x

		if (d > 0):
			--y
			d = d + 4 * (x - y) + 10
		else:
			d = d + 4 * x + 6
			drawCircle(xc, yc, x, y)
			#delay(50)

def main():
	xc = 50
	yc = 50
	r2 = 30

	win = GraphWin("My Window", 500, 500)
	win.setBackground(color_rgb(240, 240, 240))

	circleBres(xc, yc, r2, win)

	win.getMouse()  # pause for click in window
	win.close()

main()