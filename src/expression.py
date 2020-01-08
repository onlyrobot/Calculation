'''
Date: 2019/12/26
Description: 定义了表达式的表示方法、如何从字符串中解析表达式、表达式求值等
'''


import enum
import functools


def gcd(x, y):
    '''求解最大公因数'''
    if x == 0 or y == 0:
        return 0
    if x > y:
        big, small = x, y 
    else:
        big, small = y, x 
    z = big % small
    while z != 0:
        big, small = small, z 
        z = big % small
    return abs(small)


def lcm(x, y):
    '''求解最小公倍数'''
    z = gcd(x, y)
    if z == 0:
        return max(x, y)
    return x * y // z


def add(left, right):
    '''加法运算，支持数值和分数类型'''
    # 如果left,right都为数值类型
    if left.root not in Operator and right.root not in Operator:
        return Expression(left.root + right.root)
    # 如果left,right至少一个不为数值类型
    # 先将left,right解析成分子分母的形式
    if left.root in Operator:
        l_numerator, l_denominator = left.left.root, left.right.root
    else:
        l_numerator, l_denominator = left.root, 1
    if right.root in Operator:
        r_numerator, r_denominator = right.left.root, right.right.root
    else:
        r_numerator, r_denominator = right.root, 1
    # 对分数进行运算
    denominator = lcm(l_denominator, r_denominator)
    numerator = (l_numerator * (denominator // l_denominator) + 
    r_numerator * (denominator // r_denominator))
    if numerator == 0:
        return Expression(0)
    return Expression(Operator.divide, numerator, denominator)


def minus(left, right):
    '''减法运算，支持数值和分数类型'''
    # 如果left,right都为数值类型
    if left.root not in Operator and right.root not in Operator:
        return Expression(left.root - right.root)
    # 如果left,right至少一个不为数值类型
    # 先将left,right解析成分子分母的形式
    if left.root in Operator:
        l_numerator, l_denominator = left.left.root, left.right.root
    else:
        l_numerator, l_denominator = left.root, 1
    if right.root in Operator:
        r_numerator, r_denominator = right.left.root, right.right.root
    else:
        r_numerator, r_denominator = right.root, 1
    # 对分数进行运算
    denominator = lcm(l_denominator, r_denominator)
    numerator = (l_numerator * (denominator // l_denominator) - 
    r_numerator * (denominator // r_denominator))
    if numerator == 0:
        return Expression(0)
    return Expression(Operator.divide, numerator, denominator)


def multiply(left, right):
    '''乘法运算，支持数值和分数类型'''
    # 如果left,right都为数值类型
    if left.root not in Operator and right.root not in Operator:
        return Expression(left.root * right.root)
    # 如果left,right至少一个不为数值类型
    # 先将left,right解析成分子分母的形式
    if left.root in Operator:
        l_numerator, l_denominator = left.left.root, left.right.root
    else:
        l_numerator, l_denominator = left.root, 1
    if right.root in Operator:
        r_numerator, r_denominator = right.left.root, right.right.root
    else:
        r_numerator, r_denominator = right.root, 1
    # 对分数进行运算
    denominator = l_denominator * r_denominator
    numerator = l_numerator * r_numerator
    if numerator == 0:
        return Expression(0)
    temp = gcd(denominator, numerator)
    denominator //= temp 
    numerator //= temp 
    # 如果约分后分母为1，则返回分子
    if denominator == 1:
        return Expression(numerator)
    # 否则返回分数形式的表达式
    return Expression(Operator.divide, numerator, denominator)

def divide(left, right):
    '''除法运算，支持数值和分数类型，当分母为零时打印错误并退出程序'''
    # 如果left,right都为数值类型
    if left.root not in Operator and right.root not in Operator:
        if right.root == 0:
            print('error: divided by 0')
            exit(-1)
        if left.root == 0:
            return Expression(0)
        temp = gcd(left.root, right.root)
        numerator = left.root // temp 
        denominator = right.root // temp 
        sign = denominator // abs(denominator)
        if denominator == 1 or denominator == -1:
            return Expression(numerator)
        else:
            return Expression(Operator.divide, numerator * sign, abs(denominator))
    # 如果left,right至少一个不为数值类型
    # 先将left,right解析成分子分母的形式
    if left.root in Operator:
        l_numerator, l_denominator = left.left.root, left.right.root
    else:
        l_numerator, l_denominator = left.root, 1
    if right.root in Operator:
        r_numerator, r_denominator = right.left.root, right.right.root
    else:
        r_numerator, r_denominator = right.root, 1
    # 对分数进行运算
    denominator = l_denominator * r_numerator
    numerator = l_numerator * r_denominator
    if denominator == 0:
        print('error: divided by 0')
        exit(-1)
    if numerator == 0:
        return Expression(0)
    temp = gcd(denominator, numerator)
    denominator //= temp 
    numerator //= temp 
    sign = denominator // abs(denominator)
    # 如果约分后分母为1，则返回分子
    if denominator == 1 or denominator == -1:
        return Expression(numerator * sign)
    # 否则返回分数形式的表达式
    return Expression(Operator.divide, numerator * sign, abs(denominator))

def power(left, right):
    '''乘方运算，支持数值类型，当涉及到分数时报错并退出程序'''
    if left.root is Operator.divide or right.root is Operator.divide:
        print('error: power cannot be fraction') 
        exit(-1)
    if right.root >= 0: 
        return Expression(left.root ** right.root)
    else:
        return Operator.divide.value[1](Expression(1), Expression(left.root ** -right.root))

# 运算符枚举类，枚举成员到值分别是(优先级,运算函数,符号表示)
Operator = enum.Enum('Operator', {'add': (0, add, '+'), 
'minus': (0, minus, '-'), 'multiply': (1, multiply, '*'), 
'divide': (1, divide, '/'), 'power': (2, power, '^')})


@functools.total_ordering
class Expression:
    '''表达式类，实现表达式树形表示和求值运算
    
    Attributes:
        root: 根节点，可以由运算符或数值充当
        left: 左节点，当根节点是数值时该节点无意义，否则表示表达式的左子节点
        right: 右节点，当根节点是数值时该节点无意义，否则表示表达式到右字节点
    '''
    def __init__(self, root, left=None, right=None):
        self.root, self.left, self.right = root, left, right
        if left is not None and type(left) is not Expression:
            self.left = Expression(left)
        if right is not None and type(right) is not Expression:
            self.right = Expression(right)

    # def parse(self, s):
    #     ops = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '**': 3}
    #     exp_stack, op_stack = [], []
    #     for c in s:
    #         if c in ops:
    #             while op_stack and ops[c] <= ops[op_stack[-1]]:
    #                 exp_stack.append(Expression(op_stack.pop(), exp_stack.pop(), exp_stack.pop()))
    #             op_stack.append(c)
    #         elif c == '(':
    #             op.append('(')
    #         elif c == ')':
    #             op = op_stack.pop()
    #             while op != '(':
    #                 exp_stack.append(Expression(op, exp_stack.pop(), exp_stack.pop()))
    #                 op = op_stack.pop()
    #         else:
    #             c = float(c)
    #             exp_stack.append(Expression(c))
    #     while op_stack:
    #         exp_stack.append(Expression(op_stack.pop(), exp_stack.pop(), exp_stack.pop()))
    #     self.root = exp_stack.pop()

    def eval(self):
        '''表达式求值，返回结果为一个表达式'''
        # 如果表达式是数值类型，直接返回
        if self.root not in Operator:
            return self
        # 否则递归求解表达式
        left = self.left.eval()
        right = self.right.eval()
        return self.root.value[1](left, right)

    def __str__(self):
        '''将表达式转换成字符串格式'''
        # 如果表达式是数值类型，直接转换成字符串返回
        if self.root not in Operator:
            return str(self.root)
        # 对左右子树分别递归调用转换函数，并根据优先级关系在合适的地方加上括号
        left_root, right_root = self.left.root, self.right.root
        # 对左子树递归
        if left_root not in Operator or self.root.value[0] <= left_root.value[0]:
            s = self.left.__str__()
        else:
            s = '(' + self.left.__str__() + ')'
        s += self.root.value[2]
        # 对右子树递归
        if right_root not in Operator or self.root.value[0] < right_root.value[0]:
            s += self.right.__str__()
        else:
            s += '(' + self.right.__str__() + ')'
        return s

    def get_value(self):
        temp = self.eval()
        if temp.root is Operator.divide:
            return temp.left.root / temp.right.root
        else:
            return temp.root

    def __lt__(self, other):
        a = self.get_value()
        if type(other) is not Expression:
            b = other 
        else:
            b = other.get_value()
        return a < b

    def __eq__(self, other):
        a = self.get_value()
        if type(other) is not Expression:
            b = other
        else:
            b = other.get_value()
        return a == b


def main():
    a = Expression(Operator.power, 2, Expression(Operator.divide, 8, 4))
    b = Expression(Operator.multiply, Expression(Operator.add, 1, 2), Expression(Operator.minus, 2, 4))
    c = Expression(Operator.divide, Expression(Operator.add, 2, 5), 6)
    d = Expression(Operator.add, Expression(Operator.divide, 4, 3), Expression(2))
    e = Expression(0)
    print(a, '=', a.eval())
    print(b, '=', b.eval())
    print(c, '=', c.eval())
    print(d, '=', d.eval())
    print('a<b?', a < b)
    print('e==0?', e == 0)
    print('gcd:', gcd(-15, 3))
    print('lcm:', lcm(3, 5))


if __name__ == '__main__':
    main()