import pygame as pyg
from expansion import *

def arting(xpl,ypl):
    
    pyg.draw.rect(window,(0,255,0),(xpl,ypl,75,75))
    pyg.draw.rect(window,(0, 255, 0),(kaktusx[0],ykaktus,50,75))
    

gameRun = True

window=pyg.display.set_mode((1920,1080))
pyg.display.set_caption("DragoZavr")
pyg.init()


exph=widghtex()
expw=highex()

ypl=exph-150-50
xpl=expw//2-100//2

ykaktus = ypl

isJump = False
jumpCount = 10
kaktusx = []
end = False
font = pyg.font.Font(None, 100)

while len(kaktusx)<1:
    kaktusx.append(1920)

    


while gameRun:
    window.fill((245,245,220))
    pyg.time.delay(22)

    if end:

        txt1="GAME OVER"
        text1 = font.render(txt1, 1, (255, 0, 0))
        place1 = text1.get_rect(center=(expw//2, exph//3))
        window.blit(text1, place1)
        mouse = pyg.mouse.get_pos()
        kaktusx[0]=1920
  
        button1 = pyg.Rect(expw//2-50,exph//2,100,50)
        pyg.draw.rect(window, (0,200,0), button1)
        pyg.display.flip()
        
        
        press1 = pyg.mouse.get_pressed(button1)
        if press1[0]==1 or press1[1]==1:
            end=False
            kaktusx[0]=1920

    if xpl<=kaktusx[0]+50 and xpl>=kaktusx[0] and ypl==ykaktus:
        end=True

    if not(end):
        kaktusx[0]-=10
    if kaktusx[0]<=-10:
        kaktusx[0]=1920


    arting(xpl, ypl)
    pyg.display.update()

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            gameRun=False
    
    keys = pyg.key.get_pressed()
    if not (isJump):
        if (keys[pyg.K_UP] or keys[pyg.K_w] or keys[pyg.K_SPACE] and not(end)):
            print("It is jump!")
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount<0:
                ypl += (jumpCount**2) //2
            else:
                ypl -= (jumpCount**2) //2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10