'''
Date: 2020/1/3
Description:终端操作
'''
import  utilities as ut
import  tkinter as tk






def terminal():
    # question_num = input("input how many question do you want")
    # ut.gen_question(question_num)

    f_handle = open("question.txt", mode = 'r', encoding = "utf-8")
    f_content = f_handle.read()
    #print(f_content)


    point = 0
    flag = 0
    ans = []
    ans_str = "ab"
    count = 1
    for letter in f_content:
         #print(letter, end = '')
        if count == 11:
            break
        if letter != '\n':
            if flag == 1:        #遇见等号，等号后面为答案
                ans.append(letter)   #先将等号后的答案存储在列表，然后保存在ans_str中，改成字符串形式和输入的答案进行比较
                continue
            print(letter, end = '')
            if letter == '=':
                flag = 1
        else:
            ans_str = "".join(ans)
            flag = 0
            input_ans = input("\nyour answer:\n")
            count += 1

            if input_ans == ans_str:
                print("you are right, you get 10 points")
                ans.clear()
                point += 10
            else:
                print("you are wrong, come on next time")
                ans.clear()


    print("your points is:" + str(point))
    print("do you want to record your score?\n" + "1:yes\n2:no")
    recordFlag = input()
    if recordFlag == '1':
        recordScore(str(point))
    print("1:show score recording\n2:exit\n")
    showScoreFlag = input()
    if showScoreFlag == '1':
        showRecord()

    f_handle.close()

def recordScore(point):
    # 存入成绩
    file = open('score.txt', 'a')
    file.write(point)
    file.write('\n')
    file.close()
    print("record success\n")

def showRecord():
    #展示历史成绩
    file = open('score.txt', 'r')
    fileConten = file.read()
    print(fileConten)