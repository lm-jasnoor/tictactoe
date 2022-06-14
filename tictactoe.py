from tkinter import *
from tkinter.messagebox import *


class demo:
#-------------------------------------reseting--------------------------------
    def reset(self):
        self.play=0

        self.bt1['text']=''
        self.bt1['state']='normal'
        self.bt1.configure(bg='systembuttonface')

        self.bt2['text'] = ''
        self.bt2['state'] = 'normal'
        self.bt2.configure(bg='systembuttonface')

        self.bt3['text'] = ''
        self.bt3['state'] = 'normal'
        self.bt3.configure(bg='systembuttonface')

        self.bt4['text'] = ''
        self.bt4['state'] = 'normal'
        self.bt4.configure(bg='systembuttonface')

        self.bt5['text'] = ''
        self.bt5['state'] = 'normal'
        self.bt5.configure(bg='systembuttonface')

        self.bt6['text'] = ''
        self.bt6['state'] = 'normal'
        self.bt6.configure(bg='systembuttonface')

        self.bt7['text'] = ''
        self.bt7['state'] = 'normal'
        self.bt7.configure(bg='systembuttonface')

        self.bt8['text'] = ''
        self.bt8['state'] = 'normal'
        self.bt8.configure(bg='systembuttonface')

        self.bt9['text'] = ''
        self.bt9['state'] = 'normal'
        self.bt9.configure(bg='systembuttonface')

#----------------------COLOR CHANGE-------------------------------------------------------
    def win1(self):
        self.bt1.configure(bg='yellow')
        self.bt2.configure(bg='yellow')
        self.bt3.configure(bg='yellow')
    def win2(self):
        self.bt4.configure(bg='yellow')
        self.bt5.configure(bg='yellow')
        self.bt6.configure(bg='yellow')
    def win3(self):
        self.bt7.configure(bg='yellow')
        self.bt8.configure(bg='yellow')
        self.bt9.configure(bg='yellow')
    def win4(self):
        self.bt1.configure(bg='yellow')
        self.bt4.configure(bg='yellow')
        self.bt7.configure(bg='yellow')
    def win5(self):
        self.bt2.configure(bg='yellow')
        self.bt5.configure(bg='yellow')
        self.bt8.configure(bg='yellow')
    def win6(self):
        self.bt3.configure(bg='yellow')
        self.bt6.configure(bg='yellow')
        self.bt9.configure(bg='yellow')
    def win7(self):
        self.bt1.configure(bg='yellow')
        self.bt5.configure(bg='yellow')
        self.bt9.configure(bg='yellow')
    def win8(self):
        self.bt7.configure(bg='yellow')
        self.bt5.configure(bg='yellow')
        self.bt3.configure(bg='yellow')





#----------------------WIN LOSS-------------------------------------------------------
    def checkwin(self):
        if self.bt1['text']=='X' and self.bt2['text']=='X' and self.bt3['text']=='X':
            self.win1()
            showinfo('TIC TAC TOE','X wins')
            self.reset()




        elif self.bt4['text']=='X' and self.bt5['text']=='X' and self.bt6['text']=='X':
            self.win2()
            showinfo('TIC TAC TOE','X wins')
            self.reset()

        elif self.bt7['text']=='X' and self.bt8['text']=='X' and self.bt9['text']=='X':
            self.win3()
            showinfo('TIC TAC TOE','X wins')
            self.reset()

        elif self.bt1['text']=='X' and self.bt4['text']=='X' and self.bt7['text']=='X':
            self.win4()
            showinfo('TIC TAC TOE','X wins')
            self.reset()

        elif self.bt2['text']=='X' and self.bt5['text']=='X' and self.bt8['text']=='X':
            self.win5()
            showinfo('TIC TAC TOE','X wins')
            self.reset()

        elif self.bt3['text']=='X' and self.bt6['text']=='X' and self.bt9['text']=='X':
            self.win6()
            showinfo('TIC TAC TOE','X wins')
            self.reset()

        elif self.bt1['text']=='X' and self.bt5['text']=='X' and self.bt9['text']=='X':
            self.win7()
            showinfo('TIC TAC TOE','X wins')
            self.reset()

        elif self.bt3['text']=='X' and self.bt5['text']=='X' and self.bt7['text']=='X':
            self.win8()
            showinfo('TIC TAC TOE','X wins')
            self.reset()

        elif self.bt1['text'] == 'O' and self.bt2['text'] == 'O' and self.bt3['text'] == 'O':
            self.win1()
            showinfo('TIC TAC TOE', 'O wins')
            self.reset()

        elif self.bt4['text'] == 'O' and self.bt5['text']== 'O' and self.bt6['text'] == 'O':
            self.win2()
            showinfo('TIC TAC TOE', 'O wins')
            self.reset()

        elif self.bt7['text'] == 'O' and self.bt8['text'] == 'O' and self.bt9['text'] == 'O':
            self.win3()
            showinfo('TIC TAC TOE', 'O wins')
            self.reset()

        elif self.bt1['text'] == 'O' and self.bt4['text']== 'O' and self.bt7['text'] == 'O':
            self.win4()
            showinfo('TIC TAC TOE', 'O wins')
            self.reset()

        elif self.bt2['text'] == 'O' and self.bt5['text'] == 'O' and self.bt8['text'] == 'O':
            self.win5()
            showinfo('TIC TAC TOE', 'O wins')
            self.reset()

        elif self.bt3['text'] == 'O' and self.bt6['text'] == 'O' and self.bt9['text'] == 'O':
            self.win6()
            showinfo('TIC TAC TOE', 'O wins')
            self.reset()

        elif self.bt1['text'] == 'O' and self.bt5['text'] == 'O' and self.bt9['text'] == 'O':
            self.win7()
            showinfo('TIC TAC TOE', 'O wins')
            self.reset()

        elif self.bt3['text'] == 'O' and self.bt5['text'] == 'O' and self.bt7['text'] == 'O':
            self.win8()
            showinfo('TIC TAC TOE', 'O wins')
            self.reset()





#----------------------STATE CHANGE-------------------------------------------------------

    def fire1(self):
        if self.play%2==0:
            self.bt1['text']='X'
        else:
            self.bt1['text']='O'
        self.play=self.play+1
        self.bt1['state']='disabled'
        self.checkwin()
    def fire2(self):
        if self.play%2==0:
            self.bt2['text']='X'
        else:
            self.bt2['text']='O'
        self.play=self.play+1
        self.bt2['state']='disabled'
        self.checkwin()

    def fire3(self):
        if self.play%2==0:
            self.bt3['text']='X'
        else:
            self.bt3['text']='O'
        self.play=self.play+1
        self.bt3['state']='disabled'
        self.checkwin()

    def fire4(self):
        if self.play%2==0:
            self.bt4['text']='X'
        else:
            self.bt4['text']='O'
        self.play=self.play+1
        self.bt4['state']='disabled'
        self.checkwin()

    def fire5(self):
        if self.play%2==0:
            self.bt5['text']='X'
        else:
            self.bt5['text']='O'
        self.play=self.play+1
        self.bt5['state']='disabled'
        self.checkwin()

    def fire6(self):
        if self.play%2==0:
            self.bt6['text']='X'
        else:
            self.bt6['text']='O'
        self.play=self.play+1
        self.bt6['state']='disabled'
        self.checkwin()

    def fire7(self):
        if self.play%2==0:
            self.bt7['text']='X'
        else:
            self.bt7['text']='O'
        self.play=self.play+1
        self.bt7['state']='disabled'
        self.checkwin()

    def fire8(self):
        if self.play%2==0:
            self.bt8['text']='X'
        else:
            self.bt8['text']='O'
        self.play=self.play+1
        self.bt8['state']='disabled'
        self.checkwin()

    def fire9(self):
        if self.play%2==0:
            self.bt9['text']='X'
        else:
            self.bt9['text']='O'
        self.play=self.play+1
        self.bt9['state']='disabled'
        self.checkwin()


#----------------------INITIALIZE-------------------------------------------------------
    def __init__(self):
        self.play=0
        self.root=Tk()
        self.root.geometry('280x300')

        self.bt1=  Button(self.root,text='',width=10,height=5,command=self.fire1)
        self.bt2 = Button(self.root, text='', width=10, height=5, command=self.fire2)
        self.bt3 = Button(self.root, text='', width=10, height=5, command=self.fire3)
        self.bt4 = Button(self.root, text='', width=10, height=5, command=self.fire4)
        self.bt5 = Button(self.root, text='', width=10, height=5, command=self.fire5)
        self.bt6 = Button(self.root, text='', width=10, height=5, command=self.fire6)
        self.bt7 = Button(self.root, text='', width=10, height=5, command=self.fire7)
        self.bt8 = Button(self.root, text='', width=10, height=5, command=self.fire8)
        self.bt9 = Button(self.root, text='', width=10, height=5, command=self.fire9)
        self.bt10= Button(self.root, text='restart game', command=self.reset)
        self.bt11= Button(self.root, text='exit game',command=self.root.destroy)

        self.bt1.grid(row=0,column=0)
        self.bt2.grid(row=0, column=1)
        self.bt3.grid(row=0, column=2)
        self.bt4.grid(row=1, column=0)
        self.bt5.grid(row=1, column=1)
        self.bt6.grid(row=1, column=2)
        self.bt7.grid(row=2, column=0)
        self.bt8.grid(row=2, column=1)
        self.bt9.grid(row=2, column=2)
        self.bt10.grid(row=3,column=0)
        self.bt11.grid(row=3,column=2)

        self.root.mainloop()

x=demo()