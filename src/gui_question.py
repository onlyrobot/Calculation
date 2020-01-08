'''
Date: 2020/1/8
Description: gui的问题界面
'''
import tkinter as tk
import linecache as lc
import  gui_main as guim

def getpoint(point):
    return point


class showquestion1():
    def __init__(self, master):

        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width = 200, height = 200)
        self.showquestion.place(x = 240, y = 200)
        question = lc.getline('question.txt', 1)

        label = tk.Label(self.showquestion, text = question, font = ("宋体", 20))
        label.place(x = 0, y =0)
        button = tk.Button(self.showquestion, text = '下一题', fg = "red", highlightbackground = 'darkgreen', command = self.nextquestion, width = 10)
        button.place(x = 10, y = 100)

    def nextquestion(self,):
        self.showquestion.destroy()
        showquestion2(self.master)

class showquestion2():
    def __init__(self, master):

        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width = 200, height = 200)
        self.showquestion.place(x = 240, y = 200)
        question = lc.getline('question.txt', 2)

        label = tk.Label(self.showquestion, text = question, font = ("宋体", 20))
        label.place(x = 0, y =0)
        button = tk.Button(self.showquestion, text = '下一题', fg = "red", highlightbackground = 'darkgreen', command = self.nextquestion, width = 10)
        button.place(x = 10, y = 100)

    def nextquestion(self,):
        self.showquestion.destroy()
        showquestion3(self.master)


class showquestion3():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width=200, height=200)
        self.showquestion.place(x=240, y=200)
        question = lc.getline('question.txt', 3)

        label = tk.Label(self.showquestion, text=question, font=("宋体", 20))
        label.place(x=0, y=0)
        button = tk.Button(self.showquestion, text='下一题', fg="red", highlightbackground='darkgreen',
                           command=self.nextquestion, width=10)
        button.place(x=10, y=100)

    def nextquestion(self, ):
        self.showquestion.destroy()
        showquestion4(self.master)


class showquestion4():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width=200, height=200)
        self.showquestion.place(x=240, y=200)
        question = lc.getline('question.txt', 4)

        label = tk.Label(self.showquestion, text=question, font=("宋体", 20))
        label.place(x=0, y=0)
        button = tk.Button(self.showquestion, text='下一题', fg="red", highlightbackground='darkgreen',
                           command=self.nextquestion, width=10)
        button.place(x=10, y=100)

    def nextquestion(self, ):
        self.showquestion.destroy()
        showquestion5(self.master)


class showquestion5():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width=200, height=200)
        self.showquestion.place(x=240, y=200)
        question = lc.getline('question.txt', 5)

        label = tk.Label(self.showquestion, text=question, font=("宋体", 20))
        label.place(x=0, y=0)
        button = tk.Button(self.showquestion, text='下一题', fg="red", highlightbackground='darkgreen',
                           command=self.nextquestion, width=10)
        button.place(x=10, y=100)

    def nextquestion(self, ):
        self.showquestion.destroy()
        showquestion6(self.master)


class showquestion6():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width=200, height=200)
        self.showquestion.place(x=240, y=200)
        question = lc.getline('question.txt', 6)

        label = tk.Label(self.showquestion, text=question, font=("宋体", 20))
        label.place(x=0, y=0)
        button = tk.Button(self.showquestion, text='下一题', fg="red", highlightbackground='darkgreen',
                           command=self.nextquestion, width=10)
        button.place(x=10, y=100)

    def nextquestion(self, ):
        self.showquestion.destroy()
        showquestion7(self.master)


class showquestion7():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width=200, height=200)
        self.showquestion.place(x=240, y=200)
        question = lc.getline('question.txt', 7)

        label = tk.Label(self.showquestion, text=question, font=("宋体", 20))
        label.place(x=0, y=0)
        button = tk.Button(self.showquestion, text='下一题', fg="red", highlightbackground='darkgreen',
                           command=self.nextquestion, width=10)
        button.place(x=10, y=100)

    def nextquestion(self, ):
        self.showquestion.destroy()
        showquestion8(self.master)


class showquestion8():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width=200, height=200)
        self.showquestion.place(x=240, y=200)
        question = lc.getline('question.txt', 8)

        label = tk.Label(self.showquestion, text=question, font=("宋体", 20))
        label.place(x=0, y=0)
        button = tk.Button(self.showquestion, text='下一题', fg="red", highlightbackground='darkgreen',
                           command=self.nextquestion, width=10)
        button.place(x=10, y=100)

    def nextquestion(self, ):
        self.showquestion.destroy()
        showquestion9(self.master)


class showquestion9():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width=200, height=200)
        self.showquestion.place(x=240, y=200)
        question = lc.getline('question.txt', 9)

        label = tk.Label(self.showquestion, text=question, font=("宋体", 20))
        label.place(x=0, y=0)
        button = tk.Button(self.showquestion, text='下一题', fg="red", highlightbackground='darkgreen',
                           command=self.nextquestion, width=10)
        button.place(x=10, y=100)

    def nextquestion(self, ):
        self.showquestion.destroy()
        showquestion10(self.master)


class showquestion10():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width=200, height=200)
        self.showquestion.place(x=240, y=200)
        question = lc.getline('question.txt', 10)

        label = tk.Label(self.showquestion, text=question, font=("宋体", 20))
        label.place(x=0, y=0)
        button = tk.Button(self.showquestion, text='下一题', fg="red", highlightbackground='darkgreen',
                           command=self.nextquestion, width=10)
        button.place(x=10, y=100)

    def nextquestion(self, ):
        self.showquestion.destroy()
        guim.endface(self.master)