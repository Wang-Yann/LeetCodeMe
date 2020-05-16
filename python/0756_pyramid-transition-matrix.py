#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 现在，我们用一些方块来堆砌一个金字塔。 每个方块用仅包含一个字母的字符串表示。 
# 
#  使用三元组表示金字塔的堆砌规则如下： 
# 
#  对于三元组(A, B, C) ，“C”为顶层方块，方块“A”、“B”分别作为方块“C”下一层的的左、右子块。当且仅当(A, B, C)是被允许的三元组，我
# 们才可以将其堆砌上。 
# 
#  初始时，给定金字塔的基层 bottom，用一个字符串表示。一个允许的三元组列表 allowed，每个三元组用一个长度为 3 的字符串表示。 
# 
#  如果可以由基层一直堆到塔尖就返回 true，否则返回 false。 
# 
#  
# 
#  示例 1: 
# 
#  输入: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
# 输出: true
# 解析:
# 可以堆砌成这样的金字塔:
#     A
#    / \
#   G   E
#  / \ / \
# B   C   D
# 
# 因为符合('B', 'C', 'G'), ('C', 'D', 'E') 和 ('G', 'E', 'A') 三种规则。
#  
# 
#  示例 2: 
# 
#  输入: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
# 输出: false
# 解析:
# 无法一直堆到塔尖。
# 注意, 允许存在像 (A, B, C) 和 (A, B, D) 这样的三元组，其中 C != D。
#  
# 
#  
# 
#  注意： 
# 
#  
#  bottom 的长度范围在 [2, 8]。 
#  allowed 的长度范围在[0, 200]。 
#  方块的标记字母范围为{'A', 'B', 'C', 'D', 'E', 'F', 'G'}。 
#  
#  Related Topics 位运算 深度优先搜索

"""
import collections
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        """
        TODO TODO TODO
        我们需要从三元组列表中创建一个转换映射 T。这个映射 T[x][y] = {set of z} 将是左孩子 x 和右孩子 y 所有可能的父块。
        然后，为了求解下一行，我们生成下一行所有的可能组合并求解它们。如果这些组合中有任一一行是可解的，则返回 True

        https://leetcode-cn.com/problems/pyramid-transition-matrix/solution/jin-zi-ta-zhuan-huan-ju-zhen-by-leetcode/
        """
        T = collections.defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)

        def solve(A):
            if len(A) == 1:
                return True
            return any(solve(cand) for cand in build(A, []))

        def build(A, ans, i=0):
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                for w in T[A[i], A[i + 1]]:
                    ans.append(w)
                    for res in build(A, ans, i + 1):
                        yield res
                    ans.pop()

        return solve(bottom)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        """
        https://leetcode-cn.com/problems/pyramid-transition-matrix/solution/rong-yi-li-jie-de-pythondai-ma-by-a-bai-152/
        GOOD

        """
        f = collections.defaultdict(lambda:collections.defaultdict(list))
        for a, b, c in allowed:
            f[a][b].append(c)

        def pyramid(inner_bottom):
            # print("inner_bottom",inner_bottom)
            if len(inner_bottom) == 1:
                return True
            for items in itertools.product(*(f[x][y] for x, y in zip(inner_bottom, inner_bottom[1:]))):
                if pyramid(items):
                    return True
            return False

        return pyramid(bottom)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(bottom="BCD", allowed=["BCG", "CDE", "GEA", "FFF"]), True),
    pytest.param(dict(bottom="AABA", allowed=["AAA", "AAB", "ABA", "ABB", "BAC"]), False),
])
def test_solutions(kwargs, expected):
    assert Solution().pyramidTransition(**kwargs) == expected
    assert Solution1().pyramidTransition(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
