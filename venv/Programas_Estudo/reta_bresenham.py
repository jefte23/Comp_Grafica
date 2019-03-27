from graphics import *

# function for line generation
def bresenham(x1, y1, x2, y2, win):

    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)

    y = y1
    for x in range(x1, x2 + 1):

        print("(", x, ",", y, ")\n")
        pt = Point(x, y)
        pt.draw(win)

        # Add slope to increment angle formed
        slope_error_new = slope_error_new + m_new

        # Slope error reached limit, time to
        # increment y and update slope error.
        if (slope_error_new >= 0):
            y = y + 1
            slope_error_new = slope_error_new - 2 * (x2 - x1)

        # driver function


def main():

    x1 = 120
    x2 = 450
    y1 = 100
    y2 = 300

    # x1 = int(input("informe X inicial: "))
    # x2 = int(input("informe X final: "))
    # y1 = int(input("informe Y inicial: "))
    # y2 = int(input("informe Y final: "))

    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(240, 240, 240))

    # Chava variavel de bresenham
    bresenham(x1, y1, x2, y2, win)

    win.getMouse()  # pause for click in window
    win.close()

main()