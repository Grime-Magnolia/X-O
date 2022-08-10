import tkinter
class bke():
    def __init__(self,X,O):
        self.root = tkinter.Tk()
        self.root.title('Boter kaas en eieren!')
        self.frame = tkinter.Frame(self.root)
        self.counterforbutton = 0
        self.buttonx = [0,1,2,0,1,2,0,1,2]
        self.buttony = [1,1,1,2,2,2,3,3,3]
        global beurt
        self.beurt = 0
        self.xwon = X
        self.owon = O
        self.procces = ['clear','clear','clear','clear','clear','clear','clear','clear','clear']
        self.won = 0
        self.checkerd1 = [2,0,0,1,2,0,3,6,6]
        self.checkerd2 = [4,4,3,4,5,1,4,7,7]
        self.checkerd3 = [6,8,6,7,8,2,5,8,8]
        self.geweest = []
        self.frame2 = tkinter.Frame(self.root)
    def summon_window(self):
        scoreO = tkinter.Label(self.frame2,text=f'O won {self.owon} times')
        scoreO.grid(row=0,column=0)
        justaminus = tkinter.Label(self.frame2,text=' - ').grid(row=0,column=1)
        scoreX = tkinter.Label(self.frame2,text=f'X won {self.xwon} times')
        scoreX.grid(row=0,column=2)
        self.frame2.pack(pady=20,padx=50)
        self.frame.pack(pady=20,padx=50)
        def check():
            def passy():
                self.root.quit()
            for a in range(0,8):
                if self.procces[self.checkerd1[a]] == self.procces[self.checkerd2[a]] == self.procces[self.checkerd3[a]] != 'clear':
                    label = tkinter.Label(self.frame,text=f'{self.procces[self.checkerd3[a]]} won').grid(row=3,column=0)
                    self.won = 1
                    if self.procces[self.checkerd3[a]] == 'O':
                        self.owon = self.owon + 1
                        scoreO.config(text=f'O won {self.owon} times')
                    else:
                        self.xwon = self.xwon + 1
                        scoreX.config(text=f'X won {self.xwon} times')
                    self.root.after(1000,passy)
            if self.won != 1:
                self.root.after(100, check)
        self.root.after(100, check)
        self.root.mainloop()
        for a in range(0,8):
            if self.procces[self.checkerd1[a]] == self.procces[self.checkerd2[a]] == self.procces[self.checkerd3[a]] != 'clear':
                self.root.destroy()
                self.root.quit()
    def summon_button(self,a):
        def change():
            if self.geweest[a] == 0:
                if (self.beurt % 2) == 0:
                    button.config(text='O')
                    button.config(bg='red')
                    self.procces[a] = 'O'
                else:
                    button.config(text='X')
                    self.procces[a] = 'X'
                    button.config(bg='green')
                self.beurt = self.beurt + 1
                self.geweest[a] = 1
        button = tkinter.Button(self.frame,text=' ',command= change)
        button.grid(row=self.buttonx[self.counterforbutton],column=self.buttony[self.counterforbutton],padx = 20, pady = 20)
        self.counterforbutton += 1
b = 0
def choice():
    choicer = tkinter.Tk
    def returny():
        choicer.root.destroy()
        global b
        b = 0
    def returnn():
        choicer.root.destroy()
        b = 1
    choicer.root = tkinter.Tk()
    label = tkinter.Label(text='again?').grid(row=0,column=1)
    buttonn = tkinter.Button(text='No',bg='red',command=returnn).grid(row=2,column=2)
    buttony = tkinter.Button(text='Yes',bg='green',command=returny).grid(row=2,column=0)
    choicer.root.mainloop()
    bke = 0
x,o = 0,0
while b != 1:
    Bke = bke(x,o)
    b = 1
    if b == 0:
        Bke.root = tkinter.Tk()
    for a in range(0,9):
        Bke.geweest.append(0)
        Bke.summon_button(a)
    Bke.summon_window()
    choice()
    print(b)
    x,o = Bke.xwon,Bke.owon
print(f'the final score is:\nO:{Bke.owon}\nX:{Bke.xwon}')
