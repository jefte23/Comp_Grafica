def dda(x0, y0, x1, y1):
    
    dx = x1 - x0
    dy = y1 - y0
    steps = 0
    
    if (round(dx) > round(dy)):
        steps = round(dx)
    else:
        steps = round(dy)
    
    #print(steps)
    Xinc = dx / steps
    Yinc = dy / steps
    
    X = x0
    Y = y0
    
    for x in range(steps): 
        print("(",round(X, 2) ,",",round(Y, 2) ,")\n")
        X = X + Xinc
        Y = Y + Yinc
    
if __name__=='__main__': 
    x1 = 6
    y1 = 9
    x2 = 11
    y2 = 12
    dda(x1, y1, x2, y2) 
    
#############################

def bresanham_v2(x1, y1, x2, y2):
    xf = 0
    dx = x2 - x1
    dy = y2 - y1
    p = 2 * (dy - dx)
    p2 = 2 * dy
    xy2 = 2 * (dy - dx)
    
    if (x1 > x2):
        x = x2
        y = y2
        xf = x1
    else:
        x = x1
        y = y1
        xf = x2
     
    print("(",x ,",",y ,")\n") 

    while(x < xf):
        x = x +1
        if (p < 0):
            p += p2
        else:
            y = y + 1
            p += xy2
           
        print("(",x ,",",y ,")\n") 

if __name__=='__main__': 
    x1 = 3
    y1 = 2
    x2 = 15
    y2 = 5
    bresanham_v2(x1, y1, x2, y2)

