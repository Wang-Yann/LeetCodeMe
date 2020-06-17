#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 返回所有长度为 N 且满足其每两个连续位上的数字之间的差的绝对值为 K 的非负整数。 
# 
#  请注意，除了数字 0 本身之外，答案中的每个数字都不能有前导零。例如，01 因为有一个前导零，所以是无效的；但 0 是有效的。 
# 
#  你可以按任何顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  输入：N = 3, K = 7
# 输出：[181,292,707,818,929]
# 解释：注意，070 不是一个有效的数字，因为它有前导零。
#  
# 
#  示例 2： 
# 
#  输入：N = 2, K = 1
# 输出：[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 9 
#  0 <= K <= 9 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return list(range(10))
        candidates = [[vv for vv in range(10) if abs(vv - v) == K] for v in range(10)]
        dp = list(range(1, 10))
        for i in range(1, N):
            dp = [v * 10 + digit for v in dp for digit in candidates[v % 10]]
        return dp


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(N=1, K=0), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]],
    # [dict(N=3, K=7), [181, 292, 707, 818, 929]],
    # [dict(N=2, K=1), [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]],
])
def test_solutions(kw, expected):
    assert sorted(Solution().numsSameConsecDiff(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
