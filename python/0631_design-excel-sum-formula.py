#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-24 09:36:33
# @Last Modified : 2020-07-24 09:36:33
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你的任务是实现 Excel 的求和功能，具体的操作如下： 
# 
#  Excel(int H, char W): 这是一个构造函数，输入表明了 Excel 的高度和宽度。H 是一个正整数，范围从 1 到 26，代表高度。W 
# 是一个字符，范围从 'A' 到 'Z'，宽度等于从 'A' 到 W 的字母个数。Excel 表格是一个高度 * 宽度的二维整数数组，数组中元素初始化为 0。第一
# 行下标从 1 开始，第一列下标从 'A' 开始。 
# 
#  
# 
#  void Set(int row, char column, int val): 设置 C(row, column) 中的值为 val。 
# 
#  
# 
#  int Get(int row, char column): 返回 C(row, column) 中的值。 
# 
#  
# 
#  int Sum(int row, char column, List of Strings : numbers): 这个函数会将计算的结果放入 C(row
# , column) 中，计算的结果等于在 numbers 中代表的所有元素之和，这个函数同时也会将这个结果返回。求和公式会一直计算更新结果直到这个公式被其他的值
# 或者公式覆盖。 
# 
#  numbers 是若干字符串的集合，每个字符串代表单个位置或一个区间。如果这个字符串表示单个位置，它的格式如下：ColRow，例如 "F7" 表示位置 (
# 7, F) 。如果这个字符串表示一个区间，它的格式如下：ColRow1:ColRow2。区间就是左上角为 ColRow1 右下角为 ColRow2 的长方形。 
# 
# 
#  
# 
#  样例 1 ： 
# 
#  
# 
#  Excel(3,"C"); 
# // 构造一个 3*3 的二维数组，初始化全是 0。
# //   A B C
# // 1 0 0 0
# // 2 0 0 0
# // 3 0 0 0
# 
# Set(1, "A", 2);
# // 设置 C(1,"A") 为 2。
# //   A B C
# // 1 2 0 0
# // 2 0 0 0
# // 3 0 0 0
# 
# Sum(3, "C", ["A1", "A1:B2"]);
# // 将 C(3,"C") 的值设为 C(1,"A") 单点，左上角为 C(1,"A") 右下角为 C(2,"B") 的长方形，所有元素之和。返回值 4。 
# 
# //   A B C
# // 1 2 0 0
# // 2 0 0 0
# // 3 0 0 4
# 
# Set(2, "B", 2);
# // 将 C(2,"B") 设为 2。 注意 C(3, "C") 的值也同时改变。
# //   A B C
# // 1 2 0 0
# // 2 0 2 0
# // 3 0 0 6
#  
# 
#  
# 
#  注释 ： 
# 
#  
#  你可以认为不会出现循环求和的定义，比如说： A1 = sum(B1) ，B1 = sum(A1)。 
#  测试数据中，字母表示用双引号。 
#  请记住清零 Excel 类中的变量，因为静态变量、类变量会在多组测试数据中保存之前结果。详情请看这里。 
#  
# 
#  
#  Related Topics 设计 
#  👍 16 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Excel:

    def __init__(self, H: int, W: str):
        self.m = {}
        self.mat = [[0] * (self.col_idx(W) + 1) for _ in range(H)]

    def col_idx(self, char):
        return ord(char) - ord("A")

    def set(self, r: int, c: str, v: int) -> None:
        if (r, c) in self.m:
            self.m.pop((r, c))
        self.mat[r - 1][self.col_idx(c)] = v

    def get(self, r: int, c: str) -> int:
        if (r, c) in self.m:
            return self.sum(r, c, self.m[(r, c)])
        return self.mat[r - 1][self.col_idx(c)]

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        res = 0
        for s in strs:
            if ":" not in s:
                y = s[0]
                x = int(s[1:])
                res += self.get(x, y)
            else:
                f, t = s.split(":")
                for i in range(int(f[1:]), int(t[1:]) + 1):
                    for j in range(ord(f[0]), ord(t[0]) + 1):
                        res += self.get(i, chr(j))
        self.m[r, c] = strs
        # print(self.m)
        return res


# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    ex = Excel(3, "C")
    ex.set(1, "A", 2)
    assert ex.sum(3, "C", ["A1", "A1:B2"]) == 4
    ex.set(2, "B", 2)
    assert ex.get(3, "C") == 6


def test1():
    ops = ["Excel", "set", "set", "set", "set", "set", "set", "set", "set", "set", "set", "set", "set", "set",
           "set", "set", "set", "set", "set", "set", "set", "set", "set", "set", "set", "set", "set", "sum",
           "sum", "sum", "sum", "sum", "sum", "sum", "sum", "sum", "sum", "sum", "sum", "sum", "sum", "sum",
           "sum", "sum", "sum", "sum", "sum", "sum", "sum", "sum", "sum", "sum", "sum"]
    args = [[26, "Z"], [1, "A", 0], [1, "B", 1], [1, "C", 2], [1, "D", 3], [1, "E", 4], [1, "F", 5], [1, "G", 6],
            [1, "H", 7], [1, "I", 8], [1, "J", 9], [1, "K", 10], [1, "L", 11], [1, "M", 12], [1, "N", 13],
            [1, "O", 14], [1, "P", 15], [1, "Q", 16], [1, "R", 17], [1, "S", 18], [1, "T", 19],
            [1, "U", 20], [1, "V", 21], [1, "W", 22],
            [1, "X", 23], [1, "Y", 24], [1, "Z", 25], [2, "A", ["A1:A1"]], [2, "B", ["A1:B1"]], [2, "C", ["A1:C1"]],
            [2, "D", ["A1:D1"]], [2, "E", ["A1:E1"]], [2, "F", ["A1:F1"]], [2, "G", ["A1:G1"]], [2, "H", ["A1:H1"]],
            [2, "I", ["A1:I1"]], [2, "J", ["A1:J1"]], [2, "K", ["A1:K1"]], [2, "L", ["A1:L1"]], [2, "M", ["A1:M1"]],
            [2, "N", ["A1:N1"]], [2, "O", ["A1:O1"]], [2, "P", ["A1:P1"]], [2, "Q", ["A1:Q1"]], [2, "R", ["A1:R1"]],
            [2, "S", ["A1:S1"]], [2, "T", ["A1:T1"]], [2, "U", ["A1:U1"]], [2, "V", ["A1:V1"]], [2, "W", ["A1:W1"]],
            [2, "X", ["A1:X1"]], [2, "Y", ["A1:Y1"]], [2, "Z", ["A1:Z1"]]]
    ex = Excel(26, "Z")
    for op, arg in zip(ops[1:], args[1:]):
        x = getattr(ex, op)(*arg)
        if op != set:
            print(x)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
