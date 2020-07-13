#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 11:56:23
# @Last Modified : 2020-07-13 11:56:23
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个布尔表达式和一个期望的布尔结果 result，布尔表达式由 0 (false)、1 (true)、& (AND)、 | (OR) 和 ^ (XOR)
#  符号组成。实现一个函数，算出有几种可使该表达式得出 result 值的括号方法。 
# 
#  示例 1: 
# 
#  输入: s = "1^0|0|1", result = 0
# 
# 输出: 2
# 解释: 两种可能的括号方法是
# 1^(0|(0|1))
# 1^((0|0)|1)
#  
# 
#  示例 2: 
# 
#  输入: s = "0&0&0&1^1|0", result = 1
# 
# 输出: 10 
# 
#  提示： 
# 
#  
#  运算符的数量不超过 19 个 
#  
#  Related Topics 栈 字符串 
#  👍 22 👎 0

"""

import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countEval(self, s: str, result: int) -> int:
        """
        TODO
        {
            符号: {
                需要计算出的结果: {
                    [(左子式需要计算的结果，右子式需要计算的结果)]
                }
            }

        }
        """

        @functools.lru_cache(None)
        def dfs(expression, result):
            # 边界情况
            if len(expression) == 1:
                return int(bool(int(expression)) == result)

            # 递归计算左右子式的结果
            total = 0
            for i in range(len(expression)):
                if expression[i] in OPS_SPACE:
                    for lr, rr in OPS_SPACE[expression[i]][result]:
                        total += dfs(expression[:i], lr) * dfs(expression[i + 1:], rr)
            return total

        OPS_SPACE = {
            '&': {
                True: [(True, True)],
                False: [(True, False), (False, True), (False, False)]
            },
            '|': {
                True: [(True, False), (False, True), (True, True)],
                False: [(False, False)]
            },
            '^': {
                True: [(True, False), (False, True)],
                False: [(True, True), (False, False)]
            }
        }
        return dfs(s, result)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="1^0|0|1", result=0), 2],
    [dict(s="0&0&0&1^1|0", result=1), 10],
])
def test_solutions(kw, expected):
    assert Solution().countEval(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
