# coding: utf-8
#!/usr/bin/python
import time
from tkinter import *
from tkinter.messagebox import *
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
sens=2
sens2=0
taille=3
taille2=3
sec = 0
snake=[[1,1],[2,1],[3,1]]
snake2=[[18,18],[17,18],[16,18]]
game="off"
lan="off"
pl=1



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
##################################
def master():
    global gg
    for r in range(0,len(gg)):
        y0=r*25
        for un in range(0,len(gg[r])):
            if gg[r][un][0]==0:
                col="black"
            elif gg[r][un][0]==1:
                col="white"
            can.create_rectangle(un*25, y0, un*25+25, y0+25, fill=col)

def pomme():
    global gg,taille,snake,pl,taille2,snake2
    dess=0
    a=randrange(1,len(gg)-1)
    b=randrange(1,len(gg)-1)
    if gg[a][b][0]==0:
        for i in range(0,taille):
            if a==snake[i][0] and b==snake[i][1]:
                dess=1
            if pl==2:
                for b in range(0,taille2):
                    if a==snake2[b][0] and b==snake2[b][1]:
                        dess=1
        if dess==0:
            gg[a][b][0]=2
            can.create_rectangle(b*25, a*25, b*25+25, a*25+25, fill="red")
        else:
            pomme()
    else:
        pomme()
        
def snk():
    global gg,taille,sens,snake,game,taille2,snake2
    if gg[snake[taille-1][0]][snake[taille-1][1]][0]==1:
        tab.config(text="press <space> to continue")
        game="off"
        return
    if sens==1:
        snake.append([snake[taille-1][0],snake[taille-1][1]-1])
    elif sens==2:
       snake.append([snake[taille-1][0],snake[taille-1][1]+1])
    elif sens==3:
        snake.append([snake[taille-1][0]-1,snake[taille-1][1]])
    elif sens==4:
        snake.append([snake[taille-1][0]+1,snake[taille-1][1]])
    if pl==2:
        meme=0
        for a in range(0,taille2):
            if snake[0][1]==snake2[a][1] and snake[0][0]==snake2[a][0]:
                meme=1
        if meme!=1:
            can.create_rectangle(snake[0][1]*25, snake[0][0]*25, snake[0][1]*25+25, snake[0][0]*25+25, fill="black")
        else:
            can.create_rectangle(snake[0][1]*25, snake[0][0]*25, snake[0][1]*25+25, snake[0][0]*25+25, fill="blue")
    elif pl==1:
        can.create_rectangle(snake[0][1]*25, snake[0][0]*25, snake[0][1]*25+25, snake[0][0]*25+25, fill="black")
    can.create_rectangle(snake[taille][1]*25, snake[taille][0]*25, snake[taille][1]*25+25, snake[taille][0]*25+25, fill="green")
    if taille>4:
        for i in range(0,taille):
            if snake[taille][0]==snake[i][0] and snake[taille][1]==snake[i][1]:
                tab.config(text="press <space> to continue")
                game="off"
                return
    if gg[snake[taille][0]][snake[taille][1]][0]==2:
        gg[snake[taille][0]][snake[taille][1]][0]=0
        pomme()
        taille+=1
        if pl==2:
            tab.config(text="score vert:"+str(taille*10-30))
        else:
            tab.config(text="score :"+str(taille*10-30))
    else:
        snake.pop(0)
    
#####
def snk2():
    global gg,taille2,sens2,snake2,game,snake,taille
    if gg[snake2[taille2-1][0]][snake2[taille2-1][1]][0]==1:
        tab.config(text="press <space> to continue")
        game="off"
        return
    if sens2==1:
        snake2.append([snake2[taille2-1][0],snake2[taille2-1][1]-1])
    elif sens2==2:
       snake2.append([snake2[taille2-1][0],snake2[taille2-1][1]+1])
    elif sens2==3:
        snake2.append([snake2[taille2-1][0]-1,snake2[taille2-1][1]])
    elif sens2==4:
        snake2.append([snake2[taille2-1][0]+1,snake2[taille2-1][1]])
    meme=0
    for a in range(0,taille):
        if snake[0][1]==snake2[a][1] and snake[0][0]==snake2[a][0]:
            meme=1
    if meme!=1:
        can.create_rectangle(snake2[0][1]*25, snake2[0][0]*25, snake2[0][1]*25+25, snake2[0][0]*25+25, fill="black")
    can.create_rectangle(snake2[taille2][1]*25, snake2[taille2][0]*25, snake2[taille2][1]*25+25, snake2[taille2][0]*25+25, fill="blue")
    if taille2>4:
        for i in range(0,taille2):
            if snake2[taille2][0]==snake2[i][0] and snake2[taille2][1]==snake2[i][1]:
                tab.config(text="press <space> to continue")
                game="off"
                return
    if gg[snake2[taille2][0]][snake2[taille2][1]][0]==2:
        gg[snake2[taille2][0]][snake2[taille2][1]][0]=0
        pomme()
        taille2+=1
        tab2.config(text="score bleu:"+str(taille2*10-30))
    else:
        snake2.pop(0)

def move(e):
    global x,y,sens,game,snake,gg,sec,taille,sens2,snake2,taille2
    if e.keycode==32:
        if game=="off":
            game="on"
            snake=[[1,1],[2,1],[3,1]]
            for i in range(1,len(gg)-1):
                for b in range(1,len(gg[i])-1):
                    gg[i][b][0]=0
            snake2=[[18,18],[17,18],[16,18]]
            sec=0
            taille=3
            taille2=3
            master()
            pomme()
            sens=2
            sens2=1
            tick()
    if e.keycode==37 and snake[taille-1][1]!=snake[taille-2][1]+1:
        sens=1
        "left"
    elif e.keycode==38  and snake[taille-1][0]!=snake[taille-2][0]+1:
        sens=3
        "up"
    elif e.keycode==40  and snake[taille-1][0]!=snake[taille-2][0]-1:
        sens=4
        "down"
    elif e.keycode==39  and snake[taille-1][1]!=snake[taille-2][1]-1:
        sens=2
        "right"
    elif e.char=="a" and snake2[taille2-1][1]!=snake2[taille2-2][1]+1:
        sens2=1
    elif e.char=="w" and snake2[taille2-1][0]!=snake2[taille2-2][0]+1:
        sens2=3
    elif e.char=="s" and snake2[taille2-1][0]!=snake2[taille2-2][0]-1:
        sens2=4
    elif e.char=="d" and snake2[taille2-1][1]!=snake2[taille2-2][1]-1:
        sens2=2

def tick():
    global sec,game,pl,taille,taille2
    sec += 1
    snk()
    if pl==2:
        snk2()
        if game=="off":
            print("score vert :",taille*10-30)
            print("score bleu :",taille2*10-30)
    elif pl==1 and game=="off":
        print("score :",taille*10-30)
    if game=="on":
        can.after(200, tick)
    





def callback():
    global game,lan
    if lan=="on":
        game="off"
        if askyesno("Quitte", "Êtes-vous sûr de vouloir faire ça?"):
            fen1.quit()
        else:
            showinfo("Continue", "Vous n'avez pas froid aux yeux!")
        game="on"
        tick()
    else:
        fen1.quit()



    
def cree():
	global game,lan
	lan="on"
	can.pack(side=LEFT)
	can.bind("<KeyPress>", move)
	can.focus_set()
	bouton.destroy()
	bou3.destroy()
	game="on"
	master()
	pomme()
	tick()


def de():
    global pl,lan
    lan="on"
    pl=2
    can.pack(side=LEFT)
    can.bind("<KeyPress>", move)
    can.focus_set()
    bouton.destroy()
    bou3.destroy()
    game="on"
    master()
    pomme()
    tick()
    
##################################
##          programme           ##
##################################
fen1 = Tk()
can = Canvas(fen1,bg="black",height=500,width=500)
bouton=Button(fen1, text="New Game", command=cree)
bouton.pack()
bou3 = Button(fen1,text="2 Players", command=de)
bou3.pack()
bou1 = Button(fen1,text='Quitter',command=callback).pack()
tab=Label(fen1)
tab2=Label(fen1)
tab.pack()
tab2.pack()
fen1.mainloop()
fen1.destroy()
