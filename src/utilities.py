'''
Date: 2020/1/2
Description: 处理表达式到使用工具
'''


import sys 
import random
import pickle
from itertools import product
import expression as exp 


def check_valid(op, left, right):
    '''检查将要生成到表达式是否合法'''
    # left_right, right_left分别表示左子表达式的（最）右边数值和右表达式的（最）左边数值
    left_right, right_left = left, right
    # 保证生成的所有表达式都是非重复的
    while left_right.root is op:
        left_right = left_right.right 
    while right_left.root is op:
        right_left = right_left.left
    if left_right.no > right_left.no:
        return False
    # 不能存在分母为零的情况
    if op is exp.Operator.divide and right.value.root == 0:
        return False 
    # 当运算符为乘方时，要求不能有分数，0的幂不能为负数，而且指数不能太大
    if op is exp.Operator.power and (left.value.root is exp.Operator.divide 
    or right.value.root is exp.Operator.divide or left.value == 0 and 
    right.value < 0 or abs(right.value.root) > 3):
        return False
    # 对负数在表达式中的位置进行了约束，像1+-2或1--1/2这种类型到应该避免
    while right_left.root in exp.Operator:
        right_left = right_left.left
    if right_left.root < 0:
        return False
    # 计算的最终结果绝对值不能太大或太小，如果是真分数形式要求分子分母不能过大
    # 不能包含题目本身就是答案（如1/25本身就无法再化简）的情况
    result = op.value[1](left.value, right.value)
    if (result < -2500 or result > 2500 or result < 0 and result > -1 / 2500 
    or result > 0 and result < 1 / 2500):
        return False
    if result.root is exp.Operator.divide and (result.left > 300 or 
    result.left < -300 or result.right > 300 or result.right < -300):
        return False 
    if (result.root is exp.Operator.divide and result.left.root == 
    left.value.root and result.right.root == right.value.root):
        return False
    return True


def init_numbers(n, front, back):
    '''在指定范围内初始化n个数字作为生成表达式到基础
    
    比如随机生成10个0～100中到数字

    Args:
        n: 生成多少个数字
        front: 范围开始（包含）
        back: 范围结束（包含）

    Returns:
        返回生成的数字列表
    '''
    if n == 1:
        return [random.randint(front, back)]
    elif n == 0:
        return []
    center = (front + back) // 2
    part1 = random.randint(max(0, n - back + center), 
    min(n, center - front + 1))
    part2 = n - part1 
    numbers = init_numbers(part1, front, center)
    numbers.extend(init_numbers(part2, center + 1, back))
    return numbers  


def product_questions(n, questions, a, b, drop_out):
    '''由已生成的表达式组合成更复杂的表达式'''
    for left, right, op in product(a, b, exp.Operator):
        if random.random() < drop_out:
            continue
        if not check_valid(op, left, right):
            continue
        question = exp.Expression(op, left, right)
        question.value = op.value[1](left.value, right.value)
        question.no = len(questions)
        questions.append(question)
        if len(questions) >= n:
            return 


def gen_questions(n):
    '''生成n个不重复的表达式，返回并保存到文件中'''
    number_num = 200
    numbers = init_numbers(number_num, -150, 150)
    questions = [exp.Expression(number) for number in numbers]
    for pos in range(len(questions)):
        questions[pos].value = questions[pos]
        questions[pos].no = pos 
    last = 0
    while len(questions) - number_num < n:
        temp = len(questions)
        product_questions(n + number_num, questions, 
        questions[random.randint(0, temp // 10):: random.randint(1, temp // 10)], 
        questions[last:: random.randint(1, temp // 10)], 0.1)
        if len(questions) != temp:
            last = temp
        else:
            questions, last = questions[: number_num], 0
    questions = questions[number_num:]
    questions_str = [question.__str__() + '=' + question.eval().__str__() 
    + '\n' for question in questions]
    print(sys.path[0])
    with open(sys.path[0] + '/../res/questions.txt', 'w') as save_file:
        save_file.writelines(questions_str)
    return questions


def read_questions():
    with open(sys.path[0] + '/../res/questions.txt', 'r') as questions_file:
        return questions_file.read()


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


def save_score(scores):
    '''保存历史分数信息
    
    Args:
        scores: 三元组（用户名，时间，获得的分数）组成的列表
    '''
    with open(sys.path[0] + '/../res/score.dat', 'a') as score_file:
        score_file.writelines(['\t'.join(score) + '\n' for score in scores])


def read_score():
    '''读取历史分数信息
    
    Returns:
        返回三元组（用户名，时间，获得的分数）组成到列表，每个三元组代表一个历史记录
    '''
    try:
        score_file = open(sys.path[0] + '/../res/score.dat', 'r')
        raw_data = score_file.read().split('\n')
        score_file.close()
        scores = [score.split('\t') for score in raw_data[: -1]]
        return scores 
    except:
        return []


def main():
    # 生成1000道不重复的题目
    gen_questions(1000)
    # 读取题目
    print(read_questions())
    # 将乘方的显示符号设为^
    set_config(power='^')
    # 获取配置'power'的值
    print(get_config('power'))
    # 保存分数到历史文件
    save_score([('pengyao', '2020/1/1', '99'), ('zouxin', '2020/1/1', '99')])
    # 从文件中读取历史分数
    print(read_score())


if __name__ == '__main__':
    main()