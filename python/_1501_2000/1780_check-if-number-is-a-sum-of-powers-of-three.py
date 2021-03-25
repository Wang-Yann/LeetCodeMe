#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-11 03:01:55
# @Last Modified : 2021-03-11 03:01:55
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。 
# 
#  对于一个整数 y ，如果存在整数 x 满足 y == 3x ，我们称这个整数 y 是三的幂。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 12
# 输出：true
# 解释：12 = 31 + 32
#  
# 
#  示例 2： 
# 
#  输入：n = 91
# 输出：true
# 解释：91 = 30 + 32 + 34
#  
# 
#  示例 3： 
# 
#  输入：n = 21
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 107 
#  
#  Related Topics 递归 数学 回溯算法 
#  👍 10 👎 0


import math

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        choices = [3 ** i for i in range(int(math.log(10 ** 7, 3)) + 1)]
        N = len(choices)
        used = [False] * N

        def helper(pos, cur_num):
            if cur_num == 0:
                return True
            if pos >= N:
                return False
            for i in range(pos, N):
                v = choices[i]
                if v > cur_num:
                    break
                used[i] = True
                if helper(i + 1, cur_num - v):
                    return True
                used[i] = False
            return False

        return helper(0, n)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        巧妙
        转换为3进制
        转换为三进制数计算每一位， 如果出现某一位为2则不满足题意
        """
        while n > 0:
            if n % 3 == 2:
                return False
            n = n // 3
        return True


@pytest.mark.parametrize("kw,expected", [
    [dict(n=12), True],
    [dict(n=91), True],
    [dict(n=21), False],
    [dict(n=29781), False],
    [dict(n=6378022), True],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().checkPowersOfThree(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
