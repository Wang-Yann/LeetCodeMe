#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-29 18:00:00
# @Last Modified : 2020-06-29 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 在一排多米诺骨牌中，A[i] 和 B[i] 分别代表第 i 个多米诺骨牌的上半部分和下半部分。（一个多米诺是两个从 1 到 6 的数字同列平铺形成的 —— 
# 该平铺的每一半上都有一个数字。） 
# 
#  我们可以旋转第 i 张多米诺，使得 A[i] 和 B[i] 的值交换。 
# 
#  返回能使 A 中所有值或者 B 中所有值都相同的最小旋转次数。 
# 
#  如果无法做到，返回 -1. 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# 输出：2
# 解释：
# 图一表示：在我们旋转之前， A 和 B 给出的多米诺牌。
# 如果我们旋转第二个和第四个多米诺骨牌，我们可以使上面一行中的每个值都等于 2，如图二所示。
#  
# 
#  示例 2： 
# 
#  输入：A = [3,5,1,2,3], B = [3,6,3,3,4]
# 输出：-1
# 解释：
# 在这种情况下，不可能旋转多米诺牌使一行的值相等。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A[i], B[i] <= 6 
#  2 <= A.length == B.length <= 20000 
#  
#  Related Topics 贪心算法 数组

"""

import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        """GOOD"""
        intersect = functools.reduce(set.__and__, [set(d) for d in zip(A, B)])
        if not intersect:
            return -1
        x = intersect.pop()
        return min(len(A) - A.count(x), len(B) - B.count(x))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(A=[2, 1, 2, 4, 2, 2], B=[5, 2, 6, 2, 3, 2]), 2),
    pytest.param(dict(A=[3, 5, 1, 2, 3], B=[3, 6, 3, 3, 4]), -1),
])
def test_solutions(kwargs, expected):
    assert Solution().minDominoRotations(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
