'''
Date: 2020/1/3
Description: 终端操作
'''


import utilities as utl 
import time
import random


def show_history_score():
    print('user\tdate\t\tscore')
    scores = utl.read_score()
    for score in scores[:: -1][: 5]:
        print('\t'.join(score))


def main():
    question_num = int(input("input how many question do you want to generate\n"))
    utl.gen_questions(question_num)
    questions, score = utl.read_questions().split('\n'), 0
    for question in questions[random.randint(0, question_num - 10):][: 10]:
        body, answer = question.split('=')
        if answer == input(body + '='):
            score += 10
            print('right, score + 10')
        else:
            print('wrong, score + 0')
    print('you got', score, 'score in total')
    if input("do you want to save your score?(n/y)") == 'y':
        username = input('username:')
        date = time.strftime('%Y/%m/%d', time.localtime())
        utl.save_score([(username, date, str(score))])
        show_history_score()


if __name__ == '__main__':
    main()
