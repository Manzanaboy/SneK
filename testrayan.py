from tkinter import *

def batons():
    global nombreBatons,jeu
    if jeu=="joue":
        return
    jeu="joue"
    can.delete(ALL)
    x=0
    nombreBatons=20
    while x<20:
        can.create_rectangle(20*x+5,5,(x+1)*20,105,fill="beige")
        can.create_rectangle(20*x+5,5,(x+1)*20,20,fill="red")
        x=x+1

def enlever1():
    global nombreBatons,player,a,jeu
    if jeu=="pause":
        return
    nombreBatons=nombreBatons-1
    can.delete(ALL)
    x=0
    a+=1
    if nombreBatons<=1 and a%2==0:
        print("joueur 2 a perdu")
        jeu="pause"
    elif nombreBatons<=1 and a%2!=0:
        print("joueur 1 a perdu")
        jeu="pause"
    while x<nombreBatons:
        can.create_rectangle(20*x+5,5,(x+1)*20,105,fill="beige")
        x=x+1
    if(a%2==0):
        player.configure(text="joueur 2")
    else:
        player.configure(text="joueur 1")

def enlever2():
    global nombreBatons,player,a
    nombreBatons=nombreBatons-2
    can.delete(ALL)
    x=0
    a+=1
    while x<nombreBatons:
        can.create_rectangle(20*x+5,5,(x+1)*20,105,fill="beige")
        x=x+1


def enlever3():
    global nombreBatons,player,a
    nombreBatons=nombreBatons-3
    can.delete(ALL)
    x=0
    a+=1
    while x<nombreBatons:
        can.create_rectangle(20*x+5,5,(x+1)*20,105,fill="beige")
        x=x+1

##### Programme principal : ############

nombreBatons=20
a=1
jeu="pause"
fen = Tk()
player = Label(fen,text = "joueur 1")
player.pack()
can = Canvas(fen, width =405, height =110, bg ='ivory')
can.pack(side =TOP)

b1 = Button(fen, text ='Commencer a jouer', command =batons)
b1.pack(side =LEFT, padx =3, pady =3)

b2 = Button(fen, text ='1', command =enlever1)
b2.pack(side =RIGHT, padx =3, pady =3)

b3 = Button(fen, text ='2', command =enlever2)
b3.pack(side =RIGHT, padx =3, pady =3)

b4 = Button(fen, text ='3', command =enlever3)
b4.pack(side =RIGHT, padx =3, pady =3)

Button(fen,text="Quitter",command=quit).pack()

fen.mainloop()
fen.destroy()
