#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 16:30:27
# @Last Modified : 2020-04-26 16:30:27
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定一个表达式 expression 如 expression = "e + 8 - a + 5" 和一个求值映射，如 {"e": 1}（给定的形式为 ev
# alvars = ["e"] 和 evalints = [1]），返回表示简化表达式的标记列表，例如 ["-1*a","14"]
#
#
#  表达式交替使用块和符号，每个块和符号之间有一个空格。
#  块要么是括号中的表达式，要么是变量，要么是非负整数。
#  块是括号中的表达式，变量或非负整数。
#  变量是一个由小写字母组成的字符串（不包括数字）。请注意，变量可以是多个字母，并注意变量从不具有像 "2x" 或 "-x" 这样的前导系数或一元运算符 。
#
#
#
#  表达式按通常顺序进行求值：先是括号，然后求乘法，再计算加法和减法。例如，expression = "1 + 2 * 3" 的答案是 ["7"]。
#
#  输出格式如下：
#
#
#  对于系数非零的每个自变量项，我们按字典排序的顺序将自变量写在一个项中。例如，我们永远不会写像 “b*a*c” 这样的项，只写 “a*b*c”。
#  项的次数等于被乘的自变量的数目，并计算重复项。(例如，"a*a*b*c" 的次数为 4。)。我们先写出答案的最大次数项，用字典顺序打破关系，此时忽略词的前
# 导系数。
#  项的前导系数直接放在左边，用星号将它与变量分隔开(如果存在的话)。前导系数 1 仍然要打印出来。
#  格式良好的一个示例答案是 ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"] 。
#  系数为 0 的项（包括常数项）不包括在内。例如，“0” 的表达式输出为 []。
#
#
#
#
#  示例：
#
#  输入：expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
# 输出：["-1*a","14"]
#
# 输入：expression = "e - 8 + temperature - pressure",
# evalvars = ["e", "temperature"], evalints = [1, 12]
# 输出：["-1*pressure","5"]
#
# 输入：expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
# 输出：["1*e*e","-64"]
#
# 输入：expression = "7 - 7", evalvars = [], evalints = []
# 输出：[]
#
# 输入：expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []
# 输出：["5*a*b*c"]
#
# 输入：expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))
# ",
# evalvars = [], evalints = []
# 输出：["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c
# ","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b
# *b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c"
# ,"-1*b*c"]
#
#
#
#
#  提示：
#
#
#  expression 的长度在 [1, 250] 范围内。
#  evalvars, evalints 在范围 [0, 100] 内，且长度相同。
#
#  Related Topics 栈 哈希表 字符串
#  👍 21 👎 0

"""


import collections
from typing import List


class Poly(collections.Counter):

    def __init__(self, expr=None):
        if expr is None:
            return
        if expr.isdigit():
            self.update({(): int(expr)})
        else:
            self[(expr,)] += 1

    def __add__(self, other):
        self.update(other)
        return self

    def __sub__(self, other):
        self.update({
            k: -v for k, v in other.items()
        })
        return self

    def __mul__(self, other):
        def merge(k1, k2):
            result = []
            i, j = 0, 0
            while i != len(k1) or j != len(k2):
                if j == len(k2):
                    result.append(k1[i])
                    i += 1
                elif i == len(k1):
                    result.append(k2[j])
                    j += 1
                elif k1[i] < k2[j]:
                    result.append(k1[i])
                    i += 1
                else:
                    result.append(k2[j])
                    j += 1
            return result

        res = Poly()
        for k1, v1 in self.items():
            for k2, v2 in other.items():
                res.update({
                    tuple(merge(k1, k2)): v1 * v2
                })

        return res

    def eval(self, lookup):
        result = Poly()
        for polies, c in self.items():
            key = []
            for var in polies:
                if var in lookup:
                    c *= lookup[var]
                else:
                    key.append(var)
            result[tuple(key)] += c
        return result

    def to_list(self):
        return ["*".join(
            (str(v),) + k) for k, v in sorted(self.items(),
                                              key=lambda x: (-len(x[0]), x[0])
                                              ) if v
        ]


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str],
                          evalints: List[int]) -> List[str]:
        """Too Hard"""
        operands, operators = [], []

        def compute():
            """多重赋值：右边的表达式从左到右计算"""
            left, right = operands.pop(), operands.pop()
            op = operators.pop()
            if op == "+":
                operands.append(left + right)
            elif op == "-":
                operands.append(left - right)
            elif op == "*":
                operands.append(left * right)

        def parse(s):
            if not s:
                return Poly()
            operand = ""
            length = len(s)
            for i in range(length - 1, -1, -1):
                if s[i].isalnum():
                    operand += s[i]
                    if i == 0 or not s[i - 1].isalnum():
                        operands.append(Poly(operand[::-1]))
                        operand = ""
                elif s[i] == ")" or s[i] == "*":
                    operators.append(s[i])
                elif s[i] == "+" or s[i] == "-":
                    while operators and operators[-1] == "*":
                        compute()
                    operators.append(s[i])
                elif s[i] == "(":
                    while operators[-1] != ")":
                        compute()
                    operators.pop()
            while operators:
                compute()
            return operands[-1]

        lookup = dict(zip(evalvars, evalints))
        ret = parse(expression).eval(lookup).to_list()
        return ret


if __name__ == '__main__':
    sol = Solution()
    samples = [
        dict(
            expression="e + 8 - a + 5", evalvars=["e"], evalints=[1]
        ),
        dict(
            expression="e - 8 + temperature - pressure",
            evalvars=["e", "temperature"], evalints=[1, 12]
        ),
        dict(
            expression="(e + 8) * (e - 8)", evalvars=[], evalints=[]
        ),
        dict(
            expression="7 - 7", evalvars=[], evalints=[]
        ),
        dict(
            expression="a * b * c + b * a * c * 4", evalvars=[], evalints=[]
        ),
        dict(
            expression="((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
            evalvars=[], evalints=[]
        )

    ]
    lists = [(x["expression"], x["evalvars"], x["evalints"]) for x in samples]
    res = [sol.basicCalculatorIV(*x) for x in lists]
    print(res)
