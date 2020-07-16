#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-16 23:52:30
# @Last Modified : 2020-07-16 23:52:30
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0


# 给你一个数组 nums ，它包含 n 个正整数。你需要计算所有非空连续子数组的和，并将它们按升序排序，得到一个新的包含 n * (n + 1) / 2 个数
# 字的数组。
#
#  请你返回在新数组中下标为 left 到 right （下标从 1 开始）的所有数字和（包括左右端点）。由于答案可能很大，请你将它对 10^9 + 7 取模
# 后返回。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,3,4], n = 4, left = 1, right = 5
# 输出：13
# 解释：所有的子数组和为 1, 3, 6, 10, 2, 5, 9, 3, 7, 4 。将它们升序排序后，我们得到新的数组 [1, 2, 3, 3, 4, 5
# , 6, 7, 9, 10] 。下标从 le = 1 到 ri = 5 的和为 1 + 2 + 3 + 3 + 4 = 13 。
#
#
#  示例 2：
#
#
# 输入：nums = [1,2,3,4], n = 4, left = 3, right = 4
# 输出：6
# 解释：给定数组与示例 1 一样，所以新数组为 [1, 2, 3, 3, 4, 5, 6, 7, 9, 10] 。下标从 le = 3 到 ri = 4 的和
# 为 3 + 3 = 6 。
#
#
#  示例 3：
#
#
# 输入：nums = [1,2,3,4], n = 4, left = 1, right = 10
# 输出：50
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10^3
#  nums.length == n
#  1 <= nums[i] <= 100
#  1 <= left <= right <= n * (n + 1) / 2
#
#  Related Topics 排序 数组
#  👍 4 👎 0
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """ TODO GOOD GOOD"""
        h = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(h)
        ans = 0
        for k in range(1, right + 1):
            x, i = heapq.heappop(h)
            if k >= left:
                ans += x
            if i + 1 < len(nums):
                heapq.heappush(h, (x + nums[i + 1], i + 1))
        return ans % 1_000_000_007


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    """暴力"""

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        for i in range(len(nums)):
            prefix = 0
            for ii in range(i, len(nums)):
                prefix += nums[ii]
                ans.append(prefix)
        ans.sort()
        return sum(ans[left - 1:right]) % 1_000_000_007


@pytest.mark.parametrize("kwargs,expected", [
    [dict(nums=[1, 2, 3, 4], n=4, left=1, right=5), 13],

    pytest.param(dict(nums=[1, 2, 3, 4], n=4, left=3, right=4), 6),
    pytest.param(dict(nums=[1, 2, 3, 4], n=4, left=1, right=10), 50),
])
def test_solutions(kwargs, expected):
    assert Solution().rangeSum(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
