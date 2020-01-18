'''
Date: 2020/1/18
Description: utilities模块的测试文件
'''


import utilities as utl 


def check(questions):
    '''检查每个生成的问题是否合法'''
    for question in questions:
        try:
            question.eval()
        except RuntimeError as re:
            print(re)


def main():
    # 生成1000道不重复的题目
    check(utl.gen_questions(1000))
    # 读取题目
    print(utl.read_questions()[: 5])
    # 将乘方的显示符号设为^
    utl.set_config(power='^')
    # 获取配置'power'的值
    print(utl.get_config('power'))
    # 保存分数到历史文件
    utl.save_score([('pengyao', '2020/1/1', '99'), ('zouxin', '2020/1/1', '99')])
    # 从文件中读取历史分数
    print(utl.read_score()[: 5])


if __name__ == '__main__':
    main()