from graphics import *
from openpyxl import load_workbook


def ponto(x, y, cor, win):
    pt = Point(x, y)
    pt.setFill(cor)
    pt.draw(win)

#--------------------------------------------------------------
def linhasCentrais(x1, y1, x2, y2, cor, win):

    x,y = x1,y1
    length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
    dx = (x2-x1)/float(length)
    dy = (y2-y1)/float(length)

    for i in range(length):
        x += dx
        y += dy

        ponto(x, y, cor, win)

#--------------------------------------------------------------
def CirclePoints(xc, yc, x, y, cor, win):
	ponto(xc + x, yc + y, cor, win)
	ponto(xc - x, yc + y, cor, win)
	ponto(xc + x, yc - y, cor, win)
	ponto(xc - x, yc - y, cor, win)
	ponto(xc + y, yc + x, cor, win)
	ponto(xc - y, yc + x, cor, win)
	ponto(xc + y, yc - x, cor, win)
	ponto(xc - y, yc - x, cor, win)

def circulo(xc, yc, r, cor, win):

	x = 0
	y = r
	d = 3 - 2 * r

	CirclePoints(xc, yc, x, y, cor, win)
	while (y >= x):

		x = x + 1
		if (d > 0):
			y = y - 1
			d += 4 * (x - y) + 10
		else:
			d += 4 * x + 6

		CirclePoints(xc, yc, x, y, cor, win)


# --------------------------------------------------------------

def leituraDeArquivo():
    wb = load_workbook('planilha de radar.xlsx')  # abrindo o Workbook test.xlsx
    ws = wb['Planilha1']  # selecionando a planilha 'Plan1' dentro do Workbook test.xlsx
    for line in ws:  # iterando em todas as linhas da 'Plan1'
        print (line[0])  # print a primeira célula da linha
        print


# --------------------------------------------------------------
def main():

    #inicializa linhas centrais eixo x
    cor = color_rgb(131, 139, 139)
    win = GraphWin("Radar", 800, 600)
    linhasCentrais(400, 0, 400, 600, cor, win)
    linhasCentrais(0, 300, 800, 300, cor, win)

    #inicializa linhas centrais eixo x
    cor = color_rgb(0, 100, 0)
    circulo(400, 300, 290, cor, win)
    cor = color_rgb(0, 250, 0)
    circulo(400, 300, 100, cor, win)



    #aviao(x1, y1, x2, y2)

    leituraDeArquivo()


    # cliclar na tela para finalizar o programa
    win.getMouse()
    win.close()

main()