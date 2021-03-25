#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-26 20:57:45
# @Last Modified : 2020-04-26 20:57:45
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个化学式formula（作为字符串），返回每种原子的数量。
#
#  原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。
#
#  如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。
#
#
#  两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。
#
#  一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。
#
#  给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数
# 量（如果数量大于 1），以此类推。
#
#  示例 1:
#
#
# 输入:
# formula = "H2O"
# 输出: "H2O"
# 解释:
# 原子的数量是 {'H': 2, 'O': 1}。
#
#
#  示例 2:
#
#
# 输入:
# formula = "Mg(OH)2"
# 输出: "H2MgO2"
# 解释:
# 原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
#
#
#  示例 3:
#
#
# 输入:
# formula = "K4(ON(SO3)2)2"
# 输出: "K4N2O14S4"
# 解释:
# 原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
#
#
#  注意:
#
#
#  所有原子的第一个字母为大写，剩余字母都是小写。
#  formula的长度在[1, 1000]之间。
#  formula只包含字母、数字和圆括号，并且题目中给定的是合法的化学式。
#
#  Related Topics 栈 递归 哈希表
#  👍 76 👎 0

"""

import collections
import re

import pytest


class Solution0:

    def countOfAtoms(self, formula: str) -> str:
        """
        TODO
        官方解法 HARD
        """
        N = len(formula)
        idx = 0
        ans = []

        def parseRecu():
            nonlocal idx
            count = collections.Counter()
            while idx < N and formula[idx] != ")":
                if formula[idx] == "(":
                    idx += 1
                    for name, v in parseRecu().items():
                        count[name] += v
                else:
                    i_start = idx
                    idx += 1
                    while idx < N and formula[idx].islower():
                        idx += 1
                    name = formula[i_start:idx]
                    i_start = idx
                    while idx < N and formula[idx].isdigit():
                        idx += 1
                    count[name] += int(formula[i_start:idx] or 1)
            idx += 1
            i_start = idx
            while idx < N and formula[idx].isdigit():
                idx += 1
            if i_start < idx:
                multi_times = int(formula[i_start:idx])
                for name in count:
                    # print("count",name,multi_times)
                    count[name] *= multi_times
            # print("[]",formula,count)
            return count

        counter = parseRecu()
        for name_key in sorted(counter):
            ans.append(name_key)
            times = counter[name_key]
            if times > 1:
                ans.append(str(times))
        return "".join(ans)


class Solution:

    def countOfAtoms(self, formula: str) -> str:
        """
        官方解法 正则
        """
        parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stack = [collections.Counter()]
        for name, m1, left_open, right_open, m2 in parse:
            if name:
                stack[-1][name] += int(m1 or 1)
            if left_open:
                stack.append(collections.Counter())
            if right_open:
                top = stack.pop()
                for k in top:
                    stack[-1][k] += top[k] * int(m2 or 1)
        return "".join(
            name + (str(stack[-1][name]) if stack[-1][name] > 1 else "")
            for name in sorted(stack[-1])
        )


@pytest.mark.parametrize("args,expected", [
    ["H2O", "H2O", ],
    ["Mg(OH)2", 'H2MgO2', ],
    ["K4(ON(SO3)2)2", 'K4N2O14S4'],
])
def test_solutions(args, expected):
    assert Solution().countOfAtoms(args) == expected
    assert Solution0().countOfAtoms(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
