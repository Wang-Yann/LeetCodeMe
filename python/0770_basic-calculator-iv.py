#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 16:30:27
# @Last Modified : 2020-04-26 16:30:27
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

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
