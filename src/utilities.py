'''
Date: 2020/1/2
Description: 处理表达式到使用工具
'''


import random
import expression as exp 


def check_valid(root, left, right):
    if root is exp.Operator.divide and right.value.root == 0:
        return False 
    if root is exp.Operator.power and (left.value.root is exp.Operator.divide 
    or right.value.root is exp.Operator.divide or abs(right.value.root) > 3):
        return False
    if right.value.root not in exp.Operator and right.value.root < 0:
        return False 
    while left.root is root:
        left = left.right 
    while right.root is root:
        right = right.left
    return left.no <= right.no


def gen_question(n):
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
        last = current
        if remain <= 0:
            break
    
    for question in questions:
        print(question, '=', question.eval())


def set_config(**kargvs):
    pass 


def get_cfg(*args):
    pass 


def main():
    gen_question(1000)


if __name__ == '__main__':
    main()