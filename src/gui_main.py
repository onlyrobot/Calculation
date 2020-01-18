'''
Date: 2020/1/8
Description: gui的主界面及分数显示界面
'''
import tkinter as tk
import gui_question as guiq
import utilities as ut
import tkinter.messagebox
import time as ti

question_num = 0

def getquestion_num():
    global question_num
    return question_num

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
        self.initface = tk.Frame(self.master, width = 600, height = 400)
        self.initface.place(x = 0, y = 0)
        label = tk.Label(self.initface, text = '运算生成器', font = ("宋体", 20))
        label.place(x = 250, y =100)
        button_gen = tk.Button(self.initface, text = '生成题目', fg = "red", highlightbackground = 'darkgreen', command = self.gen, width = 10)
        button_gen.place(x = 200, y = 300)
        button_start = tk.Button(self.initface, text = '开始答题', fg = "red", highlightbackground = 'darkgreen', command = self.change, width = 10)
        button_start.place(x = 300, y = 300)

    def gen(self,):
        self.initface.destroy()
        gen_calculation(self.master)

    def change(self,):
        self.initface.destroy()
        #endface(self.master)
        guiq.showquestion1(self.master)
        # for i in range [1, 11]:
        #     guiq.showquestion(self.master, i)
class gen_calculation():
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
        ut.gen_questions(input_int)
        tk.messagebox.showinfo('提示','生成题目成功！')
        self.gen_cal.destroy()
        guiq.showquestion1(self.master)

class endface():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.endface = tk.Frame(self.master, width = 600, height = 400)
        self.endface.place(x = 0, y = 0)
        self.label = tk.Label(self.endface, text = '做题结束', font = ("宋体", 20))
        self.label.place(x = 250, y = 200)
        btnnext = tk.Button(self.endface, text = '结束答题', command = self.change, width = 10)
        btnnext.place(x = 250, y = 300)


    def change(self,):
        self.endface.destroy()
        savepoint(self.master)


class savepoint():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.savepoint = tk.Frame(self.master, width = 600, height = 400)
        self.savepoint.place(x = 0, y = 0)
        point = guiq.getpoint()
        label = tk.Label(self.savepoint, text = ("你的分数是：" + str(point) + "\n输入用户名"), font = ("宋体", 20), fg = "red")
        label.place(x = 200, y = 100)
        self.savepoint.entry = tk.Entry()
        self.savepoint.entry.place(x = 200, y = 200)
        button = tk.Button(self.savepoint, text = '确定', command = self.determine, width = 10)
        button.place(x = 250, y = 300)

    def determine(self, ):
        name = self.savepoint.entry.get()
        point = str(guiq.getpoint())
        time = ti.strftime('%Y/%m/%d', ti.localtime())
        print(time)
        data = [(name, time, point),]
        print(data)
        ut.save_score(data)
        tk.messagebox.showinfo('提示', '保存成功！')
        self.savepoint.destroy()
        showpoint(self.master)


class showpoint():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.showpoint = tk.Frame(self.master, width = 600, height = 400)
        self.showpoint.place(x = 0, y = 0)
        self.label = tk.Label(self.showpoint, text = '点击查看最近记录', font = ('宋体', 20))
        self.label.place(x = 220, y = 100)
        self.button_show = tk.Button(self.showpoint, text = '展示分数', command = self.show, width = 10)
        self.button_show.place(x = 250, y = 300)


    def show(self, ):
        self.label.place_forget()
        self.button_show.place_forget()
        score = ut.read_score()
        for i in range(-5, 0):
            label = tk.Label(self.showpoint, text = score[i], font = ('宋体', 20))
            label.place(x = 100, y = -50 * i)




if __name__ == '__main__':
    root = tk.Tk()
    baseinterface(root)
    root.mainloop()