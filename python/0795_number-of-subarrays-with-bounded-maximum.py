#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个元素都是正整数的数组A ，正整数 L 以及 R (L <= R)。 
# 
#  求连续、非空且其中最大元素满足大于等于L 小于等于R的子数组个数。 
# 
#  例如 :
# 输入: 
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# 输出: 3
# 解释: 满足条件的子数组: [2], [2, 1], [3].
#  
# 
#  注意: 
# 
#  
#  L, R 和 A[i] 都是整数，范围在 [0, 10^9]。 
#  数组 A 的长度范围在[1, 50000]。 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        """
        count(B) 用于计算所有元素都小于等于 B 的子数组数量
        GOOD
        """
        def count_res(A, bound):
            ans = cur = 0
            for x in A:
                if x <= bound:
                    cur += 1
                else:
                    cur = 0
                ans += cur
            return ans
        # print(count_res(A, R) , count_res(A, L - 1))
        return count_res(A, R) - count_res(A, L - 1)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    # (dict(A=[2, 1, 4, 3], L=2, R=3, ), 3),
    (dict(A=[2, 9, 2, 5, 6], L=2, R=8, ), 7),
])
def test_solutions(kwargs, expected):
    assert Solution().numSubarrayBoundedMax(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
