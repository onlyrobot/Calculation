'''
Date: 2020/1/3
Description:终端操作
'''
import  utilities as ut
import  tkinter as tk
import time as ti
import random as ran
import linecache as lc

question_line = []
point = 0
question = 'a'

def terminal():
    question_num_str = input("input how many question do you want\n")
    question_num = int(question_num_str)
    ut.gen_questions(question_num)

    #f_handle = open("../res/questions.txt", mode = 'r', encoding = "utf-8")
    #f_content = f_handle.read()
    #print(f_content)


    for i in range(1, 11):
        num = ran.randint(1, question_num)
        if i == 1:
            global question_line
            global question
            question_line.append(num)
            question = lc.getline('../res/questions.txt', num)
        else:
            while True:
                num = ran.randint(1, question_num)
                flag = 1
                for i in question_line:
                    if num == i:
                        flag = 0
                if flag == 1:
                    question_line.append(num)
                    break
            question = lc.getline('../res/questions/txt', question_line[-1])
        ans_list = []
        flag_list = 0
        question_list = []
        for data in question:
            if data == '\n':
                break
            if flag_list == 1:
                ans_list.append(data)
            if data == '=':
                flag_list = 1
            if flag_list == 0:
                question_list.append(data)
        ans_str = "".join(ans_list)
        question_list.append("=")
        question_str = "".join(question_list)
        print(question_str)
        input_ans = input()
        if input_ans == ans_str:
            print("you are right, you get 10 points!")
            global point
            point += 10
        else:
            print("you are wrong, come on next time!")

    # for letter in f_content:
    #      #print(letter, end = '')
    #     if count == 11:
    #         break
    #     if letter != '\n':
    #         if flag == 1:        #遇见等号，等号后面为答案
    #             ans.append(letter)   #先将等号后的答案存储在列表，然后保存在ans_str中，改成字符串形式和输入的答案进行比较
    #             continue
    #         print(letter, end = '')
    #         if letter == '=':
    #             flag = 1
    #     else:
    #         ans_str = "".join(ans)
    #         flag = 0
    #         input_ans = input("\nyour answer:\n")
    #         count += 1
    #
    #         if input_ans == ans_str:
    #             print("you are right, you get 10 points")
    #             ans.clear()
    #             point += 10
    #         else:
    #             print("you are wrong, come on next time")
    #             ans.clear()


    print("your points is:" + str(point))
    print("do you want to record your score?\n" + "1:yes\n2:no")
    recordFlag = input()
    if recordFlag == '1':
        name = input("please input your name:\n")
        point_str = str(point)
        time = ti.strftime('%Y/%m/%d', ti.localtime())
        data = [(name, time, point_str),]
        ut.save_score(data)
    print("1:show recent recording\n2:exit")
    showScoreFlag = input()
    if showScoreFlag == '1':
        data = ut.read_score()
        for i in range(-5, 0):
            print(data[i])
    #f_handle.close()

if __name__ == '__main__':
    terminal()