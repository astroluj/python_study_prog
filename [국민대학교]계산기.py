__author__ = 'raven' and 'astroluj'
#-*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk

class Example(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def callback(self, entry, event):
        # Operator Case
        if event == 'Cls':
            entry.delete(0, tk.END)
        elif event =='Back':
            entry.delete(len(entry.get()) - 1)
        elif event == '=':
            ans = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, ans)
        elif event == 'Close':
            self.parent.destroy()
        else:
            entry.insert(tk.END, event)

        
    def initUI(self):

        # form set
        self.parent.title("[국민대]Calculator")
        self.style = ttk.Style()
        self.style.theme_use("default")

        # row x col
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        # pad set
        entry = ttk.Entry(self)
        entry.grid(row=0, columnspan=4, sticky=tk.W + tk.E)
        entry.insert(0, '')

        text = [['Cls', 'Back', ' ', 'Close'],
                ['7', '8', '9', '/'],
                ['4', '5', '6', '*'],
                ['1', '2', '3', '-'],
                ['0', '.', '=', '+']]
        # event register
        for row, i in enumerate(text, start = 1):
            for col, j in enumerate(i, start = 1):
                btn = ttk.Button(self,
                               text = j,
                               command = (lambda text = j: self.callback(entry, text)))
                btn.grid(row = row,
                         column = col)

        # package
        self.pack()

def main():

    root = tk.Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()

