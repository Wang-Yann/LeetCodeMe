#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。 
# 
#  换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元
# 素总和是所有子数组之中最大的。 
# 
#  注意，删除一个元素后，子数组 不能为空。 
# 
#  请看示例： 
# 
#  示例 1： 
# 
#  输入：arr = [1,-2,0,3]
# 输出：4
# 解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。 
# 
#  示例 2： 
# 
#  输入：arr = [1,-2,-2,3]
# 输出：3
# 解释：我们直接选出 [3]，这就是最大和。
#  
# 
#  示例 3： 
# 
#  输入：arr = [-1,-1,-1,-1]
# 输出：-1
# 解释：最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中删去 -1 来得到 0。
#      我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个 -1。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  -10^4 <= arr[i] <= 10^4 
#  
#  Related Topics 动态规划

"""
import sys
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        """
        GOOD
        考察以arr[i]为结尾的删除和不删除的两种情况
        两个DP数组，分别考察不删除和不删除的两种情况
        """
        N = len(arr)
        if N == 1:
            return arr[0]
        # // dp1[i]代表以arr[i]为结尾的最大连续子数组和
        dp1 = [0] * N
        # // dp2[i]代表以arr[i]为结尾的并且删除了一个元素（可能是arr[i]自己）后最大的连续子数组和
        dp2 = [0] * N

        dp1[0] = arr[0]
        for i in range(1, N):
            dp1[i] = max(arr[i], dp1[i - 1] + arr[i])
        dp2[0] = arr[0]
        # // 因为删除元素后不能为空，所以以arr[1]为结尾的只有一种情况即arr[0] arr[1]，要么删除arr[0]，要么删除arr[1]
        dp2[1] = max(arr[0], arr[1])
        for i in range(2, N):
            dp2[i] = max(dp1[i - 1], dp2[i - 1] + arr[i])
        # print(dp1,dp2)
        ans = float("-inf")
        for i in range(N):
            ans = max(dp1[i], ans, dp2[i])
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def maximumSum(self, arr: List[int]) -> int:
        res = prev = cur = float("-inf")
        for x in arr:
            cur = max(prev, cur + x, x)
            res = max(res, cur)
            # 代表删x
            prev = max(prev + x, x)
        return res


@pytest.mark.parametrize("args,expected", [
    ([1, -2, 0, 3], 4),
    ([1, -2, -2, 3], 3),
    ([-1, -1, -1, -1], -1),
])
def test_solutions(args, expected):
    assert Solution().maximumSum(args) == expected
    # assert Solution1().maximumSum(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
