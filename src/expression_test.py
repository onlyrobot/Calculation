'''
Date: 2020/1/18
Description: expression模块的测试文件
'''


import expression as exp 


def main():
    # 正常用例
    print('2 + 3 =', exp.Expression(exp.Operator.add, 2, 3).eval())
    # 除数为零的用例
    try:
        exp.Expression(exp.Operator.divide, 1, 0).eval()
    except RuntimeError as re:
        print(re)
    # 乘方包含分数的用例
    try:
        exp.Expression(exp.Operator.power, exp.Expression(exp.Operator.divide, 
        1, 4), 2).eval()
    except RuntimeError as re:
        print(re)


if __name__ == '__main__':
    main()