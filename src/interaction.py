'''
Date: 2020/1/3
Description:管理Gui和命令行
'''

import terminal as ter
import  gui as gui

def interaction():
    print("what way do you want?\n1:terminal\n2:gui")
    choose = input()
    if choose == '1':
        print("you choose terminal")
    else:
        print("you choose gui")
    return  choose

def main():
    choose = interaction()
    if choose == '1':
        ter.terminal()
    else:
        gui.gui()


if __name__ == '__main__':
    main()