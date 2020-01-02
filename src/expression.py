'''
Date: 2019/12/26
Description: 定义了表达式的表示方法、如何从字符串中解析表达式、表达式求值等
'''


import enum


def gcd(x, y):
    '''求解最大公因数'''
    if x > y:
        big, small = x, y 
    else:
        big, small = y, x 
    z = big % small
    while z != 0:
        big, small = small, z 
        z = big % small
    return small


def lcm(x, y):
    '''求解最小公倍数'''
    z = gcd(x, y)
    return x * y // z


def add(x, y):
    '''加法运算，支持数值和分数类型'''
    # 如果x,y都为数值类型
    if type(x) != Expression and type(y) != Expression:
        return x + y
    # 如果x,y至少一个不为数值类型
    # 先将x,y解析成分子分母的形式
    if type(x) == Expression:
        l_numerator, l_denominator = x.left, x.right
    else:
        l_numerator, l_denominator = x, 1
    if type(y) == Expression:
        r_numerator, r_denominator = y.left, y.right
    else:
        r_numerator, r_denominator = y, 1
    # 对分数进行运算
    denominator = lcm(l_denominator, r_denominator)
    numerator = (l_numerator * (denominator // l_denominator) + 
    r_numerator * (denominator // r_denominator))
    return Expression(Operator.divide, numerator, denominator)


def minus(x, y):
    '''减法运算，支持数值和分数类型'''
    # 如果x,y都为数值类型
    if type(x) != Expression and type(y) != Expression:
        return x - y
    # 如果x,y至少一个不为数值类型
    # 先将x,y解析成分子分母的形式
    if type(x) == Expression:
        l_numerator, l_denominator = x.left, x.right
    else:
        l_numerator, l_denominator = x, 1
    if type(y) == Expression:
        r_numerator, r_denominator = y.left, y.right
    else:
        r_numerator, r_denominator = y, 1
    # 对分数进行运算
    denominator = lcm(l_denominator, r_denominator)
    numerator = (l_numerator * (denominator // l_denominator) - 
    r_numerator * (denominator // r_denominator))
    return Expression(Operator.divide, numerator, denominator)


def multiply(x, y):
    '''乘法运算，支持数值和分数类型'''
    # 如果x,y都为数值类型
    if type(x) != Expression and type(y) != Expression:
        return x * y
    # 如果x,y至少一个不为数值类型
    # 先将x,y解析成分子分母的形式
    if type(x) == Expression:
        l_numerator, l_denominator = x.left, x.right
    else:
        l_numerator, l_denominator = x, 1
    if type(y) == Expression:
        r_numerator, r_denominator = y.left, y.right
    else:
        r_numerator, r_denominator = y, 1
    # 对分数进行运算
    denominator = l_denominator * r_denominator
    numerator = l_numerator * r_numerator
    temp = gcd(denominator, numerator)
    denominator //= temp 
    numerator //= temp 
    # 如果约分后分母为1，则返回分子
    if denominator == 1:
        return numerator
    # 否则返回分数形式的表达式
    return Expression(Operator.divide, numerator, denominator)

def divide(x, y):
    '''除法运算，支持数值和分数类型，当分母为零时打印错误并退出程序'''
    # 如果x,y都为数值类型
    if type(x) != Expression and type(y) != Expression:
        if y == 0:
            print('error: divided by 0')
        temp = gcd(x, y)
        numerator = x // temp 
        denominator = y // temp 
        if denominator == 1:
            return numerator
        else:
            return Expression(Operator.divide, numerator, denominator)
    # 如果x,y至少一个不为数值类型
    # 先将x,y解析成分子分母的形式
    if type(x) == Expression:
        l_numerator, l_denominator = x.left, x.right
    else:
        l_numerator, l_denominator = x, 1
    if type(y) == Expression:
        r_numerator, r_denominator = y.left, y.right
    else:
        r_numerator, r_denominator = y, 1
    # 对分数进行运算
    denominator = l_denominator * r_numerator
    numerator = l_numerator * r_denominator
    if denominator == 0:
        print('error: divided by 0')
    temp = gcd(denominator, numerator)
    denominator //= temp 
    numerator //= temp 
    # 如果约分后分母为1，则返回分子
    if denominator == 1:
        return numerator
    # 否则返回分数形式的表达式
    return Expression(Operator.divide, numerator, denominator)

def power(x, y):
    '''乘方运算，支持数值类型，当涉及到分数时报错并退出程序'''
    if type(x) == Expression or type(y) == Expression:
        print('error: power cannot be fraction') 
        exit(-1)
    else:
        return x ** y


# 运算符枚举类，枚举成员到值分别是(优先级,运算函数,符号表示)
Operator = enum.Enum('Operator', {'add': (0, add, '+'), 
'minus': (0, minus, '-'), 'multiply': (1, multiply, '*'), 
'divide': (1, divide, '/'), 'power': (2, power, '^')})


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
        '''表达式求值'''
        # 如果表达式是数值类型，直接返回
        if self.root not in Operator:
            return self.root
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


def main():
    a = Expression(Operator.power, 2, Expression(Operator.divide, 8, 4))
    b = Expression(Operator.multiply, Expression(Operator.add, 1, 2), Expression(Operator.minus, 2, 4))
    c = Expression(Operator.divide, Expression(Operator.add, 2, 5), 6)
    print(a, '=', a.eval())
    print(b, '=', b.eval())
    print(c, '=', c.eval())


if __name__ == '__main__':
    main()