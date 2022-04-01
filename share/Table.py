from tkinter import *
 
class Table:
     
    def __init__(self,root, total_rows, total_columns, lst):
        self.total_rows =total_rows
        self.total_columns =total_columns
        self.lst = lst
         
        # code for creating table
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                 
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, self.lst[i][j])