'''
Date: 2020/1/3
Description: 四则运算出题程序的主调函数
usage: interaction [option]
    or: interaction -n [count]
    调用交互界面（默认图形用户界面）或者生成指定数量（默认1000道）的四则运算题目到默认文件中
    -t, --terminal    调用命令行交互界面
    -g, --gui         调用图形交互界面
    -n, --num         指定生成的题目数量
'''


import sys
import utilities as utl 
import terminal as ter
import  gui as gui



def main():
    if len(sys.argv) == 1:
        print('Usage: interaction [option] or interaction -n [count]\n' + 
        '调用交互界面（默认图形用户界面）或者生成指定数量（默认1000道）的四则运算题目' + 
        '到默认文件(../res/questions.txt)中\n-t, --terminal    调用命令行交互界面\n' + 
        '-g, --gui         调用图形交互界面\n-n, --num         指定生成的题目数量')
        gui.gui()
    elif sys.argv[1] == '-t' or sys.argv[1] == '--terminal':
        ter.terminal()
    elif sys.argv[1] == '-g' or sys.argv[1] == '--gui':
        gui.gui()
    elif sys.argv[1] == '-n' or sys.argv[1] == '--num':
        if len(sys.argv) == 2:
            utl.gen_questions(1000)
        else:
            try:
                num = int(sys.argv[2])
                utl.gen_questions(num)
            except Exception:
                print('error: invalid param')
    else:
        print('error: invalid param')



if __name__ == '__main__':
    main()