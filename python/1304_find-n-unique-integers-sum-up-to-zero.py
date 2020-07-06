#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数 n，请你返回 任意 一个由 n 个 各不相同 的整数组成的数组，并且这 n 个数相加和为 0 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 5
# 输出：[-7,-1,1,3,4]
# 解释：这些数组也是正确的 [-5,-1,1,2,3]，[-3,-1,2,-2,4]。
#  
# 
#  示例 2： 
# 
#  输入：n = 3
# 输出：[-1,0,1]
#  
# 
#  示例 3： 
# 
#  输入：n = 1
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 1000 
#  
#  Related Topics 数组

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools
from common_utils import TreeNode, ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0] if n % 2 == 1 else []
        for i in range(1, n // 2 + 1):
            ans.append(i)
            ans.append(-i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(n=5), [-7, -1, 1, 3, 4]],
    [dict(n=3), [-1, 0, 1]],
    [dict(n=1), [0]],
])
def test_solutions(kw, expected):
    res = Solution().sumZero(**kw)
    assert len(res) == kw["n"] and sum(res) == 0


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
