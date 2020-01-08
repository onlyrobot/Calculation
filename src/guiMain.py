'''
Date: 2020/1/8
Description: gui的主界面及分数显示界面
'''
import tkinter as tk
import guiQuestion as guiq
from tkmacosx import Button


class baseinterface():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('Calculation')
        self.root.geometry('600x400')

        initface(self.root)

class initface():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.initface = tk.Frame(self.master, width = 200, height = 200)
        self.initface.place(x = 240, y = 200)
        label = tk.Label(self.initface, text = '运算生成器', font = ("宋体", 20))
        label.place(x = 0, y =0)
        button = tk.Button(self.initface, text = '开始答题', fg = "red", highlightbackground = 'darkgreen', command = self.change, width = 10)
        button.place(x = 10, y = 100)

    def change(self,):
        self.initface.destroy()
        #endface(self.master)
        guiq.showquestion1(self.master)

class endface():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.endface = tk.Frame(self.master, width = 200, height = 200)
        self.endface.place(x = 240, y = 200)
        btnnext = tk.Button(self.endface, text = '结束答题', command = self.change, width = 10)
        btnnext.place(x = 10, y = 100)

    def change(self,):
        self.endface.destroy()
        showpoint(self.master)


class showpoint():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.showpoint = tk.Frame(self.master, width = 200, height = 200)
        self.showpoint.place(x = 240, y = 200)
        #point = guiq.getpoint()
        point = 50
        label = tk.Label(self.showpoint, text = ("your point is " + str(point)), font = ("宋体", 20), fg = "red")
        label.place(x = 0, y = 0)





if __name__ == '__main__':
    root = tk.Tk()
    baseinterface(root)
    root.mainloop()