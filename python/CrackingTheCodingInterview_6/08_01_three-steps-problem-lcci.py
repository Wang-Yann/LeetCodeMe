#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 10:27:25
# @Last Modified : 2020-07-13 10:27:25
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模100
# 0000007。 
# 
#  示例1: 
# 
#  
#  输入：n = 3 
#  输出：4
#  说明: 有四种走法
#  
# 
#  示例2: 
# 
#  
#  输入：n = 5
#  输出：13
#  
# 
#  提示: 
# 
#  
#  n范围在[1, 1000000]之间 
#  
#  Related Topics 动态规划 
#  👍 16 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def waysToStep(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 1:
            return 1
        elif n == 2:
            return 2
        a, b, c = 1, 1, 2
        for i in range(3, n + 1):
            a, b, c = b, c, (a + b + c) % MOD
        return c

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=3), 4],
    [dict(n=5), 13],
    [dict(n=900750), 916454207],
])
def test_solutions(kw, expected):
    assert Solution().waysToStep(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
