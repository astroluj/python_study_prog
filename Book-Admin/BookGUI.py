__author__ = 'astroluj'
#-*- coding: utf-8 -*-

'''
==@ [국민대학교]도서관리20093326_이의재
'''
import Books
import Sqlite3_admin
import tkinter as tk
import tkinter.ttk as ttk

class Example(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def callback(self, entry, event):
        # Operator Case
        if event == 'search':
            result = Books.search_info(table = 'Books',
                                       name, author, price = entry.get().split(','))
            entry.delete(len(entry.get())
            entry.insert(0, result)
                                
        elif event =='insert':
            result = Books.insert_info(table = 'Books',
                                       name, author, price = entry.get().split(','))
            entry.delete(len(entry.get()))
            entry.insert(0, 'Success' if result
                         else 'Failed')
        elif event == 'modify':
            result = Books.update_info(table = 'Books',
                                       name, author, price = entry.get().split(','))
            entry.delete(len(entry.get()))
            entry.insert(0, 'Success' if result
                         else 'Failed')
        else: # delete
            result = Books.update_info(table = 'Books',
                                       name, author, price = entry.get().split(','))
            entry.delete(len(entry.get()))
            entry.insert(0, 'Success' if result
                         else 'Failed')

        
    def initUI(self):

        # form set
        self.parent.title("[국민대]도서관리")
        self.style = ttk.Style()
        self.style.theme_use("default")

        # row x col
        for i in range(3):
            self.columnconfigure(i, pad=2)
        for i in range(4):
            self.rowconfigure(i, pad=2)

        # pad set
        entry = ttk.Entry(self)
        
        # Label
        text = ['Name', 'Author', 'Price']
        # event register
        for col, i in enumerate(text, start = 1):
            txt = ttk.Label(self,
                           text = i))
            btn.grid(row = 0,
                     column = col)
        # insert
        entry.grid(row=1, column=3, sticky=tk.W + tk.E)
        entry.insert(0,1, '') # name input
        entry.insert(0,2, '') # author input
        entry.insert(0,3, '') # price input

        text = ['search', 'insert', 'modify', 'update']
        # event register
        for col, i in enumerate(text, start = 1):
            btn = ttk.Button(self,
                            text = i,
                            command = (lambda text = i: self.callback(entry, text)))
            btn.grid(row = 2,
                     column = col)
        # show data
        entry.grid(row=3, columnspans=3, sticky=tk.W + tk.E)
        entry.insert(3, '')
        
        # package
        self.pack()

def main():

    root = tk.Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()


