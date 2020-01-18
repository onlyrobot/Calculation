'''
Date: 2020/1/8
Description: gui的问题界面
'''
import tkinter as tk
import linecache as lc
import  gui_main as guim
import random as ran

point = 0
question_num = []
def getpoint():
    global point
    return point




class showquestion1():
    def __init__(self, master):

        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width = 600, height = 400)
        self.showquestion.place(x = 0, y = 0)
        #随机读出题目
        n = guim.getquestion_num()
        num = ran.randint(1, n)
        global question_num
        question_num.append(num)
        question = lc.getline('../res/questions.txt', num)

        ans_list = []
        flag = 0
        question_list = []
        for data in question:
            if data == '\n':
                break
            if flag == 1:
                ans_list.append(data)
            if data == '=':
                flag = 1
            if flag == 0:
                question_list.append(data)

        self.ans_str = "".join(ans_list)
        question_list.append("=")
        question_str = "".join(question_list)
        question_len = len(question_str)


        label = tk.Label(self.showquestion, text = question_str, font = ("宋体", 20))
        label.place(x = 200, y =200)
        button = tk.Button(self.showquestion, text = '下一题', fg = "red", highlightbackground = 'darkgreen', command = self.nextquestion, width = 10)
        button.place(x = 250, y = 300)
        self.showquestion.entry = tk.Entry()
        self.showquestion.entry.place(x = 200 + question_len * 15, y = 200)

    def nextquestion(self, ):
        input = self.showquestion.entry.get()
        print(input)
        if input == self.ans_str:
            global point
            point += 10
            print(point)
        self.showquestion.destroy()
        showquestion2(self.master)
        #guim.endface(self.master)

class showquestion2():
    def __init__(self, master):

        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width = 600, height = 400)
        self.showquestion.place(x = 0, y = 0)
        #找出之前未读取过的题目
        global question_num
        n = guim.getquestion_num()
        while True:
            num = ran.randint(1, n)
            flag = 1
            for i in question_num:
                if num == question_num:
                    flag = 0
            if flag == 1:
                question_num.append(num)
                break

        num = question_num[-1]
        question = lc.getline('../res/questions.txt', num)

        ans_list = []
        flag = 0
        question_list = []
        for data in question:
            if data == '\n':
                break
            if flag == 1:
                ans_list.append(data)
            if data == '=':
                flag = 1
            if flag == 0:
                question_list.append(data)

        self.ans_str = "".join(ans_list)
        question_list.append("=")
        question_str = "".join(question_list)
        question_len = len(question_str)


        label = tk.Label(self.showquestion, text = question_str, font = ("宋体", 20))
        label.place(x = 200, y =200)
        button = tk.Button(self.showquestion, text = '下一题', fg = "red", highlightbackground = 'darkgreen', command = self.nextquestion, width = 10)
        button.place(x = 250, y = 300)
        self.showquestion.entry = tk.Entry()
        self.showquestion.entry.place(x = 200 + question_len * 15, y = 200)

    def nextquestion(self, ):
        input = self.showquestion.entry.get()
        print(input)
        if input == self.ans_str:
            global point
            point = point + 10
            print(point)
        self.showquestion.destroy()
        showquestion3(self.master)


class showquestion3():
    def __init__(self, master):

        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width = 600, height = 400)
        self.showquestion.place(x = 0, y = 0)
        # 找出之前未读取过的题目
        global question_num
        n = guim.getquestion_num()
        while True:
            num = ran.randint(1, n)
            flag = 1
            for i in question_num:
                if num == question_num:
                    flag = 0
            if flag == 1:
                question_num.append(num)
                break

        num = question_num[-1]
        question = lc.getline('../res/questions.txt', num)

        ans_list = []
        flag = 0
        question_list = []
        for data in question:
            if data == '\n':
                break
            if flag == 1:
                ans_list.append(data)
            if data == '=':
                flag = 1
            if flag == 0:
                question_list.append(data)

        self.ans_str = "".join(ans_list)
        question_list.append("=")
        question_str = "".join(question_list)
        question_len = len(question_str)


        label = tk.Label(self.showquestion, text = question_str, font = ("宋体", 20))
        label.place(x = 200, y =200)
        button = tk.Button(self.showquestion, text = '下一题', fg = "red", highlightbackground = 'darkgreen', command = self.nextquestion, width = 10)
        button.place(x = 250, y = 300)
        self.showquestion.entry = tk.Entry()
        self.showquestion.entry.place(x = 200 + question_len * 15, y = 200)

    def nextquestion(self, ):
        input = self.showquestion.entry.get()
        print(input)
        if input == self.ans_str:
            global point
            point = point + 10
            print(point)
        self.showquestion.destroy()
        showquestion4(self.master)


class showquestion4():
    def __init__(self, master):

        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width = 600, height = 400)
        self.showquestion.place(x = 0, y = 0)
        # 找出之前未读取过的题目
        global question_num
        n = guim.getquestion_num()
        while True:
            num = ran.randint(1, n)
            flag = 1
            for i in question_num:
                if num == question_num:
                    flag = 0
            if flag == 1:
                question_num.append(num)
                break

        num = question_num[-1]
        question = lc.getline('../res/questions.txt', num)

        ans_list = []
        flag = 0
        question_list = []
        for data in question:
            if data == '\n':
                break
            if flag == 1:
                ans_list.append(data)
            if data == '=':
                flag = 1
            if flag == 0:
                question_list.append(data)

        self.ans_str = "".join(ans_list)
        question_list.append("=")
        question_str = "".join(question_list)
        question_len = len(question_str)


        label = tk.Label(self.showquestion, text = question_str, font = ("宋体", 20))
        label.place(x = 200, y =200)
        button = tk.Button(self.showquestion, text = '下一题', fg = "red", highlightbackground = 'darkgreen', command = self.nextquestion, width = 10)
        button.place(x = 250, y = 300)
        self.showquestion.entry = tk.Entry()
        self.showquestion.entry.place(x = 200 + question_len * 15, y = 200)

    def nextquestion(self, ):
        input = self.showquestion.entry.get()
        print(input)
        if input == self.ans_str:
            global point
            point = point + 10
            print(point)
        self.showquestion.destroy()
        showquestion5(self.master)


class showquestion5():
    def __init__(self, master):

        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width = 600, height = 400)
        self.showquestion.place(x = 0, y = 0)
        # 找出之前未读取过的题目
        global question_num
        n = guim.getquestion_num()
        while True:
            num = ran.randint(1, n)
            flag = 1
            for i in question_num:
                if num == question_num:
                    flag = 0
            if flag == 1:
                question_num.append(num)
                break

        num = question_num[-1]
        question = lc.getline('../res/questions.txt', num)

        ans_list = []
        flag = 0
        question_list = []
        for data in question:
            if data == '\n':
                break
            if flag == 1:
                ans_list.append(data)
            if data == '=':
                flag = 1
            if flag == 0:
                question_list.append(data)

        self.ans_str = "".join(ans_list)
        question_list.append("=")
        question_str = "".join(question_list)
        question_len = len(question_str)


        label = tk.Label(self.showquestion, text = question_str, font = ("宋体", 20))
        label.place(x = 200, y =200)
        button = tk.Button(self.showquestion, text = '下一题', fg = "red", highlightbackground = 'darkgreen', command = self.nextquestion, width = 10)
        button.place(x = 250, y = 300)
        self.showquestion.entry = tk.Entry()
        self.showquestion.entry.place(x = 200 + question_len * 15, y = 200)

    def nextquestion(self, ):
        input = self.showquestion.entry.get()
        print(input)
        if input == self.ans_str:
            global point
            point = point + 10
            print(point)
        self.showquestion.destroy()
        showquestion6(self.master)


class showquestion6():
    def __init__(self, master):

        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width = 600, height = 400)
        self.showquestion.place(x = 0, y = 0)
        # 找出之前未读取过的题目
        global question_num
        n = guim.getquestion_num()
        while True:
            num = ran.randint(1, n)
            flag = 1
            for i in question_num:
                if num == question_num:
                    flag = 0
            if flag == 1:
                question_num.append(num)
                break

        num = question_num[-1]
        question = lc.getline('../res/questions.txt', num)

        ans_list = []
        flag = 0
        question_list = []
        for data in question:
            if data == '\n':
                break
            if flag == 1:
                ans_list.append(data)
            if data == '=':
                flag = 1
            if flag == 0:
                question_list.append(data)

        self.ans_str = "".join(ans_list)
        question_list.append("=")
        question_str = "".join(question_list)
        question_len = len(question_str)


        label = tk.Label(self.showquestion, text = question_str, font = ("宋体", 20))
        label.place(x = 200, y =200)
        button = tk.Button(self.showquestion, text = '下一题', fg = "red", highlightbackground = 'darkgreen', command = self.nextquestion, width = 10)
        button.place(x = 250, y = 300)
        self.showquestion.entry = tk.Entry()
        self.showquestion.entry.place(x = 200 + question_len * 15, y = 200)

    def nextquestion(self, ):
        input = self.showquestion.entry.get()
        print(input)
        if input == self.ans_str:
            global point
            point = point + 10
            print(point)
        self.showquestion.destroy()
        showquestion7(self.master)


class showquestion7():
    def __init__(self, master):

        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width = 600, height = 400)
        self.showquestion.place(x = 0, y = 0)
        # 找出之前未读取过的题目
        global question_num
        n = guim.getquestion_num()
        while True:
            num = ran.randint(1, n)
            flag = 1
            for i in question_num:
                if num == question_num:
                    flag = 0
            if flag == 1:
                question_num.append(num)
                break

        num = question_num[-1]
        question = lc.getline('../res/questions.txt', num)

        ans_list = []
        flag = 0
        question_list = []
        for data in question:
            if data == '\n':
                break
            if flag == 1:
                ans_list.append(data)
            if data == '=':
                flag = 1
            if flag == 0:
                question_list.append(data)

        self.ans_str = "".join(ans_list)
        question_list.append("=")
        question_str = "".join(question_list)
        question_len = len(question_str)


        label = tk.Label(self.showquestion, text = question_str, font = ("宋体", 20))
        label.place(x = 200, y =200)
        button = tk.Button(self.showquestion, text = '下一题', fg = "red", highlightbackground = 'darkgreen', command = self.nextquestion, width = 10)
        button.place(x = 250, y = 300)
        self.showquestion.entry = tk.Entry()
        self.showquestion.entry.place(x = 200 + question_len * 15, y = 200)

    def nextquestion(self, ):
        input = self.showquestion.entry.get()
        print(input)
        if input == self.ans_str:
            global point
            point = point + 10
            print(point)
        self.showquestion.destroy()
        showquestion8(self.master)


class showquestion8():
    def __init__(self, master):

        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width = 600, height = 400)
        self.showquestion.place(x = 0, y = 0)
        # 找出之前未读取过的题目
        global question_num
        n = guim.getquestion_num()
        while True:
            num = ran.randint(1, n)
            flag = 1
            for i in question_num:
                if num == question_num:
                    flag = 0
            if flag == 1:
                question_num.append(num)
                break

        num = question_num[-1]
        question = lc.getline('../res/questions.txt', num)

        ans_list = []
        flag = 0
        question_list = []
        for data in question:
            if data == '\n':
                break
            if flag == 1:
                ans_list.append(data)
            if data == '=':
                flag = 1
            if flag == 0:
                question_list.append(data)

        self.ans_str = "".join(ans_list)
        question_list.append("=")
        question_str = "".join(question_list)
        question_len = len(question_str)


        label = tk.Label(self.showquestion, text = question_str, font = ("宋体", 20))
        label.place(x = 200, y =200)
        button = tk.Button(self.showquestion, text = '下一题', fg = "red", highlightbackground = 'darkgreen', command = self.nextquestion, width = 10)
        button.place(x = 250, y = 300)
        self.showquestion.entry = tk.Entry()
        self.showquestion.entry.place(x = 200 + question_len * 15, y = 200)

    def nextquestion(self, ):
        input = self.showquestion.entry.get()
        print(input)
        if input == self.ans_str:
            global point
            point = point + 10
            print(point)
        self.showquestion.destroy()
        showquestion9(self.master)


class showquestion9():
    def __init__(self, master):

        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width = 600, height = 400)
        self.showquestion.place(x = 0, y = 0)
        # 找出之前未读取过的题目
        global question_num
        n = guim.getquestion_num()
        while True:
            num = ran.randint(1, n)
            flag = 1
            for i in question_num:
                if num == question_num:
                    flag = 0
            if flag == 1:
                question_num.append(num)
                break

        num = question_num[-1]
        question = lc.getline('../res/questions.txt', num)

        ans_list = []
        flag = 0
        question_list = []
        for data in question:
            if data == '\n':
                break
            if flag == 1:
                ans_list.append(data)
            if data == '=':
                flag = 1
            if flag == 0:
                question_list.append(data)

        self.ans_str = "".join(ans_list)
        question_list.append("=")
        question_str = "".join(question_list)
        question_len = len(question_str)


        label = tk.Label(self.showquestion, text = question_str, font = ("宋体", 20))
        label.place(x = 200, y =200)
        button = tk.Button(self.showquestion, text = '下一题', fg = "red", highlightbackground = 'darkgreen', command = self.nextquestion, width = 10)
        button.place(x = 250, y = 300)
        self.showquestion.entry = tk.Entry()
        self.showquestion.entry.place(x = 200 + question_len * 15, y = 200)

    def nextquestion(self, ):
        input = self.showquestion.entry.get()
        print(input)
        if input == self.ans_str:
            global point
            point = point + 10
            print(point)
        self.showquestion.destroy()
        showquestion10(self.master)


class showquestion10():
    def __init__(self, master):

        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width = 600, height = 400)
        self.showquestion.place(x = 0, y = 0)
        # 找出之前未读取过的题目
        global question_num
        n = guim.getquestion_num()
        while True:
            num = ran.randint(1, n)
            flag = 1
            for i in question_num:
                if num == question_num:
                    flag = 0
            if flag == 1:
                question_num.append(num)
                break

        num = question_num[-1]
        question = lc.getline('../res/questions.txt', num)

        ans_list = []
        flag = 0
        question_list = []
        for data in question:
            if data == '\n':
                break
            if flag == 1:
                ans_list.append(data)
            if data == '=':
                flag = 1
            if flag == 0:
                question_list.append(data)

        self.ans_str = "".join(ans_list)
        question_list.append("=")
        question_str = "".join(question_list)
        question_len = len(question_str)


        label = tk.Label(self.showquestion, text = question_str, font = ("宋体", 20))
        label.place(x = 200, y =200)
        button = tk.Button(self.showquestion, text = '下一题', fg = "red", highlightbackground = 'darkgreen', command = self.nextquestion, width = 10)
        button.place(x = 250, y = 300)
        self.showquestion.entry = tk.Entry()
        self.showquestion.entry.place(x = 200 + question_len * 15, y = 200)

    def nextquestion(self, ):
        input = self.showquestion.entry.get()
        print(input)
        if input == self.ans_str:
            global point
            point = point + 10
            print(point)
        self.showquestion.destroy()
        guim.endface(self.master)