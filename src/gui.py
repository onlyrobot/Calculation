'''
Date: 2020/1/8
Description: gui的主界面及分数显示界面
'''


import tkinter as tk
import utilities as utl
import tkinter.messagebox
import time


class BaseFrame():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('Calculation')
        self.root.geometry('600x400')
        InitFrame(self.root)


class InitFrame():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.Initface = tk.Frame(self.master, width = 600, height = 400)
        self.Initface.place(x = 0, y = 0)
        label = tk.Label(self.Initface, text = '运算生成器', font = ("宋体", 20))
        label.place(x = 250, y =100)
        button_gen = tk.Button(self.Initface, text = '生成题目', fg = "red", highlightbackground = 
        'darkgreen', command = self.gen, width = 10)
        button_gen.place(x = 200, y = 300)
        button_start = tk.Button(self.Initface, text = '开始答题', fg = "red", highlightbackground = 
        'darkgreen', command = self.change, width = 10)
        button_start.place(x = 300, y = 300)

    def gen(self):
        self.Initface.destroy()
        GenCalculation(self.master)

    def change(self):
        self.Initface.destroy()
        ShowQuestion(self.master)
        # guiq.showquestion1(self.master)

class GenCalculation():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.gen_cal = tk.Frame(self.master, width = 600, height = 400)
        self.gen_cal.place(x = 0, y = 0)
        self.label = tk.Label(self.gen_cal, text = "输入想生成的题目数量", font = ("宋体", 20))
        self.label.place(x = 200, y = 100)
        self.gen_cal.entry = tk.Entry()
        self.gen_cal.entry.place(x = 200, y = 200)
        button = tk.Button(self.gen_cal, text = '开始答题', command = self.change, width = 10)
        button.place(x = 250, y = 300)

    def change(self, ):
        input = self.gen_cal.entry.get()
        input_int = int(input)
        global question_num
        question_num = input_int
        utl.gen_questions(input_int)
        tk.messagebox.showinfo('提示','生成题目成功！')
        self.gen_cal.destroy()
        ShowQuestion(self.master)

class EndInterface():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.EndInterface = tk.Frame(self.master, width = 600, height = 400)
        self.EndInterface.place(x = 0, y = 0)
        self.label = tk.Label(self.EndInterface, text = '做题结束', font = ("宋体", 20))
        self.label.place(x = 250, y = 200)
        btnnext = tk.Button(self.EndInterface, text = '结束答题', command = self.change, width = 10)
        btnnext.place(x = 250, y = 300)


    def change(self,):
        self.EndInterface.destroy()
        SavePoint(self.master)


class ShowQuestion():
    score = 0
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.showquestion = tk.Frame(self.master, width = 600, height = 400)
        self.showquestion.place(x = 0, y = 0)
        self.questions = utl.read_questions().split('\n')
        self.body, self.answer = self.questions[0].split('=')
        ShowQuestion.score, self.pos = 0, 1
        self.label = tk.Label(self.showquestion, text = self.body, font = ("宋体", 20))
        self.label.place(x = 200, y =200)
        button = tk.Button(self.showquestion, text = '下一题', fg = "red", highlightbackground = 'darkgreen', 
        command = self.confirm, width = 10)
        button.place(x = 250, y = 300)
        self.entry = tk.Entry()
        self.entry.place(x = 200, y = 250)
        
    def confirm(self, ):
        answer = self.entry.get()
        print(answer)
        if answer == self.answer:
            ShowQuestion.score += 10
            print('right, score + 10')
        else:
            print('wrong, score + 0')
        if self.pos == 10 or self.pos >= len(self.questions):
            EndInterface(self.master)
        else:
            self.body, self.answer = self.questions[self.pos].split('=')
            self.label.config(text=self.body)
            self.pos += 1


class SavePoint():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.SavePoint = tk.Frame(self.master, width = 600, height = 400)
        self.SavePoint.place(x = 0, y = 0)
        point = ShowQuestion.score
        label = tk.Label(self.SavePoint, text = ("你的分数是：" + str(point) + "\n输入用户名"), font = ("宋体", 20), fg = "red")
        label.place(x = 200, y = 100)
        self.SavePoint.entry = tk.Entry()
        self.SavePoint.entry.place(x = 200, y = 200)
        button = tk.Button(self.SavePoint, text = '确定', command = self.determine, width = 10)
        button.place(x = 250, y = 300)

    def determine(self, ):
        name = self.SavePoint.entry.get()
        point = str(ShowQuestion.score)
        date = time.strftime('%Y/%m/%d', time.localtime())
        print(date)
        data = [(name, date, point),]
        print(data)
        utl.save_score(data)
        tk.messagebox.showinfo('提示', '保存成功！')
        self.SavePoint.destroy()
        ShowPoint(self.master)


class ShowPoint():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.ShowPoint = tk.Frame(self.master, width = 600, height = 400)
        self.ShowPoint.place(x = 0, y = 0)
        self.label = tk.Label(self.ShowPoint, text = '点击查看最近记录', font = ('宋体', 20))
        self.label.place(x = 220, y = 100)
        self.button_show = tk.Button(self.ShowPoint, text = '展示分数', command = self.show, width = 10)
        self.button_show.place(x = 250, y = 300)


    def show(self, ):
        self.label.place_forget()
        self.button_show.place_forget()
        score = utl.read_score()
        for i in range(-5, 0):
            label = tk.Label(self.ShowPoint, text = score[i], font = ('宋体', 20))
            label.place(x = 100, y = -50 * i)



def main():
    root = tk.Tk()
    BaseFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()