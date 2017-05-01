# coding: utf-8
#!/usr/bin/python
import time
from tkinter import *
from random import randrange


##################################
##            objets            ##
##################################

g1 =[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
g2 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g3 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g4 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g5 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g6 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g7 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g8 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g9 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g10 =[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
gg=[g1,g2,g3,g4,g5,g6,g7,g8,g9,g10]
x,y=1,1
sens=2
taille=3
sec = 0


##grille 10: [[],[],[],[],[],[],[],[],[],[]]
##grille 20: [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
##g1 =[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
##g2 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g3 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g4 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g5 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g6 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g7 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g8 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g9 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g10 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g11 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g12 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g13 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g14 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g15 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g16 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g17 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g18 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g19 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g20 =[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
##gg=[g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12,g13,g14,g15,g16,g17,g18,g19,g20]


##################################
##          fonctions           ##
##################################http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
def master():
    global g1,g2,g3,g4,g5,g6,g7g,g8,g9,g10,gg
    for r in range(0,len(gg)):
        y0=r*25
        for un in range(0,len(gg[r])):
            if gg[r][un][0]==0:
                col="black"
            elif gg[r][un][0]==1:
                col="white"
            elif gg[r][un][0]==2:
                col="red"
            elif gg[r][un][0]==3:
                col="green"
                if gg[r][un][1]==1:
                    gg[r][un]=[0]
                else:
                    gg[r][un][1]-=1
            else:
                col="yellow"
            can.create_rectangle(un*25, y0, un*25+25, y0+25, fill=col)

def pomme():
    global g1,g2,g3,g4,g5,g6,g7g,g8,g9,g10,gg
    
    a=randrange(1,10)
    b=randrange(1,10)
    if gg[a][b][0]==0:
        gg[a][b][0]=2
    else:
        pomme()
        
def grid():
    for b in range(0,10):
        y0=b*50
        y1=b*50+25
        for i in range(0,10):
            can.create_rectangle(i*50, y0, i*50+25, y1, fill="white")
            can.create_rectangle(i*50+25, y0+25, i*50+50, y1+25, fill="white")
            
def deli():
    can.delete(ALL)
def drr():
    global x,y
    can.create_rectangle(x*25, y*25, x*25+25, y*25+25, fill="green")
def snake():
    global g1,g2,g3,g4,g5,g6,g7g,g8,g9,g10,gg,x,y,taille,sens
    if sens==3:
        if gg[x-1][y][0]==0:
            x-=1
            gg[x][y]=[3,taille]
        elif gg[x-1][y][0]==2:
            x-=1
            taille+=1
            gg[x][y]=[3,taille]
        else:
            fen1.quit()
            print("perdu")
            print("score : ",taille*10)
    if sens==4:
        if gg[x+1][y][0]==0:
            x+=1
            gg[x][y]=[3,taille]
        elif gg[x+1][y][0]==2:
            x+=1
            taille+=1
            gg[x][y]=[3,taille]
        else:
            fen1.quit()
            print("perdu")
            print("score : ",taille*10)
    if sens==1:
        if gg[1][y-1][0]==0:
            y-=1
            gg[x][y]=[3,taille]
        elif gg[x][y-1][0]==2:
            y-=1
            taille+=1
            gg[x][y]=[3,taille]
        else:
            fen1.quit()
            print("perdu")
            print("score : ",taille*10)
    if sens==2:
        if gg[x][y+1][0]==0:
            y+=1
            gg[x][y]=[3,taille]
        elif gg[x][y+1][0]==2:
            y+=1
            taille+=1
            gg[x][y]=[3,taille]
        else:
            fen1.quit()
            print("perdu")
            print("score : ",taille*10)


def move(e):
    global x,y,sens
    if e.keycode==32:
        snake()
        master()
    if e.keycode==37:
        sens=1
        "left"
    elif e.keycode==38:
        sens=3
        "up"
    elif e.keycode==40:
        sens=4
        "down"
    elif e.keycode==39:
        sens=2
        "right"

def tick():
    global sec
    sec += 1
    # Take advantage of the after method of the Label
    snake()
    master()
    can.after(500, tick)


##################################
##          programme           ##
##################################
fen1 = Tk()
can = Canvas(fen1,bg="black",height=500,width=500)
can.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='print',command=grid)
bou2.pack()
bou3 = Button(fen1,text='delete',command=deli)
bou3.pack()
bou4 = Button(fen1,text='draw',command=pomme)
bou4.pack()
can.bind("<KeyPress>", move)
can.focus_set()
master()
Button(fen1, fg='blue', text='Start', command=tick).pack()
fen1.mainloop()
fen1.destroy()
