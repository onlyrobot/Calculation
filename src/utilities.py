'''
Date: 2020/1/2
Description: 处理表达式到使用工具
'''


import sys 
import random
import pickle
import expression as exp 


def check_valid(root, left, right):
    '''检查将要生成到表达式是否合法'''
    # 如果存在分母为零
    if root is exp.Operator.divide and right.value.root == 0:
        return False 
    # 当运算符为乘方时，要求不能有分数，而且指数不能太大
    if root is exp.Operator.power and (left.value.root is exp.Operator.divide 
    or right.value.root is exp.Operator.divide or abs(right.value.root) > 3):
        return False
    # 对负数在表达式中的位置进行了约束，像1+-2这种类型到应该避免
    if right.value.root not in exp.Operator and right.value.root < 0:
        return False 
    # 下面保证了生成的所有表达式都是非重复的
    while left.root is root:
        left = left.right 
    while right.root is root:
        right = right.left
    return left.no <= right.no


def gen_question(n):
    '''生成数量为n到表达式，同时避免重复，除了返回生成到表达式列表外还将所有表达式保存到文件中'''
    if n < 100:
        print('error: question number too less')
    nums_count = n // 35
    questions = [exp.Expression(i) for i in range(-nums_count, nums_count)]
    for i in range(len(questions)):
        questions[i].value = questions[i]
        questions[i].no = i 
    remain = 10 * n
    last = 0
    while True:
        current = len(questions)
        for i in range(current):
            for j in range(max(last, i), current):
                for op in exp.Operator:
                    if not check_valid(op, questions[i], questions[j]):
                        continue
                    question = exp.Expression(op, questions[i], questions[j])
                    question.value = op.value[1](questions[i].value, questions[j].value)
                    question.no = len(questions)
                    questions.append(question)
                    remain -= 1
            if remain <= 0:
                break
        if remain <= 0:
            break
        last = current
    questions = questions[(nums_count + 1) * 2: (nums_count + 1) * 2 + n]
    
    questions_str = [question.__str__() + '=' + question.eval().__str__() 
    + '\n' for question in questions]
    print(sys.path[0])
    with open(sys.path[0] + '/../res/questions.txt', 'w') as save_file:
        save_file.writelines(questions_str)
    return questions


def set_config(**kargvs):
    '''设置配置信息，参数为键值对'''
    with open(sys.path[0] + '/../res/setting.config', 'rb+') as config_file:
        try:
            config_dict = pickle.load(config_file)
        except:
            config_dict = {}
        for key, value in kargvs.items():
            config_dict[key] = value 
        pickle.dump(config_dict, config_file)


def get_config(key):
    '''获取key的配置信息，当不存在时返回None'''
    try:
        config_file = open(sys.path[0] + '/../res/setting.config', 'rb')
        config_dict = pickle.load(config_file)
        config_file.close()
        if key in config_dict:
            return config_dict[key]
        return None
    except:
        return None


def main():
    gen_question(1000)
    set_config(power='^')
    print(get_config('power'))


if __name__ == '__main__':
    main()