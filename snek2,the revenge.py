# coding: utf-8
#!/usr/bin/python
import time
from tkinter import *
from random import randrange


##################################
##            objets            ##
##################################

##g1 =[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
##g2 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g3 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g4 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g5 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g6 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g7 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g8 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g9 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
##g10 =[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
##gg=[g1,g2,g3,g4,g5,g6,g7,g8,g9,g10]
x,y=3,1
sens=2
taille=5
sec = 0
snake=[[1,1],[2,1],[3,1],[4,1],[5,1]]

##grille 10: [[],[],[],[],[],[],[],[],[],[]]
##grille 20: [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
g1 =[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
g2 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g3 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g4 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g5 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g6 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g7 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g8 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g9 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g10 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g11 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g12 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g13 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g14 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g15 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g16 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g17 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g18 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g19 =[[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]
g20 =[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
gg=[g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12,g13,g14,g15,g16,g17,g18,g19,g20]


##################################
##          fonctions           ##
##################################http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
def master():
    global gg
    for r in range(0,len(gg)):
        y0=r*25
        for un in range(0,len(gg[r])):
            if gg[r][un][0]==0:
                col="black"
            elif gg[r][un][0]==1:
                col="white"
            elif gg[r][un][0]==2:
                col="blue"
            can.create_rectangle(un*25, y0, un*25+25, y0+25, fill=col)

def pomme():
    global gg,taille,snake
    dess=0
    a=randrange(1,len(gg))
    b=randrange(1,len(gg))
    if gg[a][b][0]==0:
        for i in range(0,taille):
            if a==snake[i][0] and b==snake[i][1]:
                dess=1
        if dess==0:
            gg[a][b][0]=2
            can.create_rectangle(b*25, a*25, b*25+25, a*25+25, fill="red")
        else:
            pomme()
    else:
        pomme()
        
def snk():
    global gg,taille,sens,snake,x,y
    if sens==1:
        snake.append([snake[taille-1][0],snake[taille-1][1]-1])
    elif sens==2:
       snake.append([snake[taille-1][0],snake[taille-1][1]+1])
    elif sens==3:
        snake.append([snake[taille-1][0]-1,snake[taille-1][1]])
    elif sens==4:
        snake.append([snake[taille-1][0]+1,snake[taille-1][1]])
    can.create_rectangle(snake[taille][1]*25, snake[taille][0]*25, snake[taille][1]*25+25, snake[taille][0]*25+25, fill="green")
    can.create_rectangle(snake[0][1]*25, snake[0][0]*25, snake[0][1]*25+25, snake[0][0]*25+25, fill="black")
    if taille>4:
        for i in range(0,taille):
            if snake[taille][0]==snake[i][0] and snake[taille][1]==snake[i][1]:
                print("lost")
                fen1.quit()
    if gg[snake[taille][0]][snake[taille][1]][0]==1:
        print("lost")
        fen1.quit()
    if gg[snake[taille][0]][snake[taille][1]][0]==2:
        gg[snake[taille][0]][snake[taille][1]][0]=0
        taille+=1
        pomme()
    else:
        snake.pop(0)
    
def move(e):
    global x,y,sens
    if e.keycode==32:
        snk()
    if e.keycode==37 and gg[x][y-1][0]!=3:
        sens=1
        "left"
    elif e.keycode==38  and gg[x-1][y][0]!=3:
        sens=3
        "up"
    elif e.keycode==40  and gg[x+1][y][0]!=3:
        sens=4
        "down"
    elif e.keycode==39  and gg[x][y+1][0]!=3:
        sens=2
        "right"
    elif e.char=="z":
        master()

def tick():
    global sec
    sec += 1
    snk()
    can.after(200, tick)


##################################
##          programme           ##
##################################
fen1 = Tk()
can = Canvas(fen1,bg="black",height=500,width=500)
can.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='draw',command=pomme)
bou2.pack()
can.bind("<KeyPress>", move)
can.focus_set()
pomme()
master()
Button(fen1, fg='blue', text='Start', command=tick).pack()
fen1.mainloop()
fen1.destroy()