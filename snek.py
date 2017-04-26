# coding: utf-8
from Tkinter import *
##################################
##          fonctions           ##
##################################


##################################
fen1 = Tk()
can = Canvas(fen1,bg="black",height=500,width=500)
can.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
fen1.mainloop()
fen1.destroy()
