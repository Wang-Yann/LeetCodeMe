#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。 
# 
#  在此处，环形数组意味着数组的末端将会与开头相连呈环状。（形式上，当0 <= i < A.length 时 C[i] = A[i]，而当 i >= 0 时 
# C[i+A.length] = C[i]） 
# 
#  此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。（形式上，对于子数组 C[i], C[i+1], ..., C[j]，不存在 i <= k1, 
# k2 <= j 其中 k1 % A.length = k2 % A.length） 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3
#  
# 
#  示例 2： 
# 
#  输入：[5,-3,5]
# 输出：10
# 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
#  
# 
#  示例 3： 
# 
#  输入：[3,-1,2,-1]
# 输出：4
# 解释：从子数组 [2,-1,3] 得到最大和 2 + (-1) + 3 = 4
#  
# 
#  示例 4： 
# 
#  输入：[3,-2,2,-3]
# 输出：3
# 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
#  
# 
#  示例 5： 
# 
#  输入：[-2,-3,-1]
# 输出：-1
# 解释：从子数组 [-1] 得到最大和 -1
#  
# 
#  
# 
#  提示： 
# 
#  
#  -30000 <= A[i] <= 30000 
#  1 <= A.length <= 30000 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        """
        Kadane 算法
        最大值max在原数组中。
        最大值max在环形数组中。
        第一种情况无非就是Kadane算法。我们思考第二种情况。假设输入数组为A，那么A[0]和A[A.length-1]在第二种情况下一定会被选中。
        那么我们的思路就是找到一个A的subArray并且让这个subArray和最小。假设i是subArray的起点，j是subArray的重点，
        那么i>=0&&j<=A.length-2。这就是A[1,A.length-2]的Kadane问题了

        https://leetcode-cn.com/problems/maximum-sum-circular-subarray/solution/liang-ci-kadanesuan-fa-qiu-jie-by-user7648/

        """
        last = A[0]
        max_val = sum_val = last
        for i in range(1, len(A)):
            sum_val += A[i]
            if last < 0:
                last = A[i]
            else:
                last = last + A[i]
            max_val = max(max_val, last)
        min_val = last = 0
        for i in range(1, len(A)):
            if last > 0:
                last = A[i]
            else:
                last += A[i]
            min_val = min(min_val, last)
        return max(max_val, sum_val - min_val)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        N = len(A)
        ans = cur = float("-inf")
        for x in A:
            cur = x + max(cur, 0)
            ans = max(ans, cur)
        rightsums = [0] * N
        rightsums[-1] = A[-1]
        for i in range(N - 2, -1, -1):
            rightsums[i] = rightsums[i + 1] + A[i]
        maxright = [0] * N
        maxright[-1] = rightsums[-1]
        for i in range(N - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], rightsums[i])
        # print(maxright)
        leftsum = 0
        for i in range(N - 2):
            leftsum += A[i]
            ans = max(ans, leftsum + maxright[i + 2])
        return ans


class Solution2(object):

    def maxSubarraySumCircular(self, A):
        """
        最小化 [i+1,j-1]内部和
        由于区间 [i+1, j-1][i+1,j−1] 必须非空，我们将搜索分成 A[1:] 和 A[:-1] 两个区间考虑
        """
        # ans1: answer for one-interval subarray
        ans1 = cur = float('-inf')
        for x in A:
            cur = x + max(cur, 0)
            ans1 = max(ans1, cur)

        # ans2: answer for two-interval subarray, interior in A[1:]
        ans2 = cur = float('inf')
        for i in range(1, len(A)):
            cur = A[i] + min(cur, 0)
            ans2 = min(ans2, cur)
        ans2 = sum(A) - ans2

        # ans3: answer for two-interval subarray, interior in A[:-1]
        ans3 = cur = float('inf')
        for i in range(len(A) - 1):
            cur = A[i] + min(cur, 0)
            ans3 = min(ans3, cur)
        ans3 = sum(A) - ans3

        return max(ans1, ans2, ans3)


@pytest.mark.parametrize("args,expected", [
    ([1, -2, 3, -2], 3),
    ([5, -3, 5], 10),
    ([3, -1, 2, -1], 4),
    ([3, -2, 2, -3], 3),
    pytest.param([-2, -3, -1], -1),
])
def test_solutions(args, expected):
    assert Solution().maxSubarraySumCircular(args) == expected
    assert Solution1().maxSubarraySumCircular(args) == expected
    assert Solution2().maxSubarraySumCircular(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
