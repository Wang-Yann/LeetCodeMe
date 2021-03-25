#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。 
# 
#  返回使 A 中的每个值都是唯一的最少操作次数。 
# 
#  示例 1: 
# 
#  输入：[1,2,2]
# 输出：1
# 解释：经过一次 move 操作，数组将变为 [1, 2, 3]。 
# 
#  示例 2: 
# 
#  输入：[3,2,1,2,1,7]
# 输出：6
# 解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
# 可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
#  
# 
#  提示： 
# 
#  
#  0 <= A.length <= 40000 
#  0 <= A[i] < 40000 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        """
        在对数组排序之后，可以通过保证数组的最后一个元素，经过+1操作后比前面所有元素大即可,此时子问题的最优解会收敛于全局最优解
        """
        A.sort()
        ans = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                ans += A[i - 1] - A[i] + 1
                A[i] = A[i - 1] + 1
        # print(A)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([1, 2, 2], 1),
    pytest.param([3, 2, 1, 2, 1, 7], 6),
])
def test_solutions(args, expected):
    assert Solution().minIncrementForUnique(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
