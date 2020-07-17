#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 4/4/20 10:35 PM
# @Last Modified : 4/4/20 10:35 PM
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
#  示例:
#
#  输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
#  进阶:
#
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#  Related Topics 数组 分治算法 动态规划
#  👍 2186 👎 0

"""


import collections
from typing import List

import pytest


class Solution:

    def maxSubArray0(self, nums: List[int]) -> int:
        """贪心算法"""
        temp = []
        max_sofar, max_result = float("-inf"), float("-inf")
        for v in nums:
            max_sofar = max(v, max_sofar + v)
            max_result = max(max_sofar, max_result)
            temp.append(max_result)
        print(temp)
        return max_result

    def maxSubArray(self, nums: List[int]) -> int:
        """动态规划"""
        length = len(nums)
        max_sum = nums[0]
        temp = [max_sum]
        for i in range(1, length):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)
            temp.append(max_sum)
        print(temp)
        return max_sum


class Solution1:

    def maxSubArray(self, nums: List[int]) -> int:
        res, cur = float("-inf"), float("-inf")
        for x in nums:
            cur = max(cur + x, x)
            res = max(cur, res)
        return res


class Solution2:

    def maxSubArray(self, nums: List[int]) -> int:
        """分治 复杂度略高"""
        length = len(nums)
        if length == 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[0:length // 2])
            max_right = self.maxSubArray(nums[length // 2:length])
        # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[length // 2 - 1]
        tmp = 0
        for i in range(length // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[length // 2]
        tmp = 0
        for i in range(length // 2, length):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        return max(max_left, max_right, max_l + max_r)


class Solution3:

    def maxSubArray(self, nums: List[int]) -> int:
        """分治
        这个分治方法类似于「线段树求解 LCIS 问题」的 pushUp 操作
        lSum 表示 [l, r] 内以 l 为左端点的最大子段和
        rSum 表示 [l, r] 内以 r 为右端点的最大子段和
        mSum 表示 [l, r] 内的最大子段和
        iSum 表示 [l, r] 的区间和

        """
        Status = collections.namedtuple("Status", ["lSum", "rSum", "mSum", "iSum"])
        length = len(nums)

        def pushUp(l, r):
            iSum = l.iSum + r.iSum
            lSum = max(l.lSum, l.iSum + r.lSum)
            rSum = max(r.rSum, r.iSum + l.rSum)
            mSum = max(l.mSum, r.mSum, l.rSum + r.lSum)
            return Status(lSum, rSum, mSum, iSum)

        def get(l, r):
            if l == r:
                return Status(*[nums[l] for _ in range(4)])
            mid = (l + r) >> 1
            lSub = get(l, mid)
            rSub = get(mid + 1, r)

            return pushUp(lSub, rSub)

        ret = get(0, length - 1)
        print(ret)
        return ret.mSum


@pytest.mark.parametrize("args,expected", [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
])
def test_solutions(args, expected):
    # assert Solution().maxSubArray(args) == expected
    # assert Solution().maxSubArray0(args) == expected
    # assert Solution1().maxSubArray(args) == expected
    assert Solution2().maxSubArray(args) == expected
    assert Solution3().maxSubArray(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
