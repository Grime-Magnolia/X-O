import tkinter
class bke():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Boter kaas en eieren!')
        self.frame = tkinter.Frame(self.root)
        self.counterforbutton = 0
        self.buttonx = [0,1,2,0,1,2,0,1,2]
        self.buttony = [0,0,0,1,1,1,2,2,2]
        global beurt
        self.beurt = 0
        self.geweest = []
        self.procces = ['clear','clear','clear','clear','clear','clear','clear','clear','clear']
        self.won = 0
        self.checkerd1 = [2,0,0,1,2,0,3,6,6]
        self.checkerd2 = [4,4,3,4,5,1,4,7,7]
        self.checkerd3 = [6,8,6,7,8,2,5,8,8]
    def summon_window(self):
        self.frame.pack()
        def check():
            for a in range(0,8):
                if self.procces[self.checkerd1[a]] == self.procces[self.checkerd2[a]] == self.procces[self.checkerd3[a]] != 'clear':
                    print(f'{self.procces[self.checkerd3[a]]} won')
                    label = tkinter.Label(self.frame,text=f'{self.procces[self.checkerd3[a]]} won').grid(row=3,column=0)
                    self.won = 1
            if self.won != 1:
                self.root.after(100, check)
        self.root.after(100, check)
        self.root.mainloop()
        print(self.beurt)
        print(self.procces)
        for a in range(0,8):
            if self.procces[self.checkerd1[a]] == self.procces[self.checkerd2[a]] == self.procces[self.checkerd3[a]] != 'clear':
                print('won')
    def summon_button(self,a):
        def change():
            if self.geweest[a] == 0:
                if (self.beurt % 2) == 0:
                    button.config(text='O')
                    self.procces[a] = 'O'
                else:
                    button.config(text='X')
                    self.procces[a] = 'X'
                self.beurt = self.beurt + 1
                self.geweest[a] = 1
        button = tkinter.Button(self.frame,text='0',command= change)
        button.grid(row=self.buttonx[self.counterforbutton],column=self.buttony[self.counterforbutton],padx = 5, pady = 10)
        self.counterforbutton += 1
bke = bke()
for a in range(0,9):
    bke.geweest.append(0)
    bke.summon_button(a)
bke.summon_window()