#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接
# 成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。 
# 
#  求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。 
# 
#  说明: 请尽可能地优化你算法的时间和空间复杂度。 
# 
#  示例 1: 
# 
#  输入:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# 输出:
# [9, 8, 6, 5, 3] 
# 
#  示例 2: 
# 
#  输入:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# 输出:
# [6, 7, 6, 0, 4] 
# 
#  示例 3: 
# 
#  输入:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# 输出:
# [9, 8, 9] 
#  Related Topics 贪心算法 动态规划

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    总的思路为遍历所有从nums1里挑出i个数与nums2里挑出k-i个数的组合方案并取最大值
    子问题从nums里挑数需满足相对顺序不变的最大数
    子问题合并两个数组也需满足两个数组元素的相对顺序不变的最大数
    链接：https://leetcode-cn.com/problems/create-maximum-number/solution/pythonqing-xi-jian-duan-wen-ti-fen-jie-fa-by-yybet/

    """

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick(nums, k):  # 从nums里取出相对顺序不变的k个数构成的最大数
            if not k:
                return []
            res, _pop = [], len(nums) - k  # _pop为允许pop的个数
            while nums:
                num = nums.pop(0)
                while _pop and res and res[-1] < num:
                    _pop -= 1
                    res.pop()
                res.append(num)
            return res[:k]

        def merge(nums1, nums2):  # 将nums1和nums2各自元素的相对顺序不变合并能产生的最大数
            res = []
            while nums1 and nums2:
                res.append(nums1.pop(0)) if nums1 > nums2 else res.append(nums2.pop(0))
            res.extend(nums1 or nums2)
            return res

        _max = []
        for i in range(k + 1):  # 遍历所有组合方式，取最大的结果
            if i <= len(nums1) and k - i <= len(nums2):
                _max = max(_max, merge(pick(nums1.copy(), i), pick(nums2.copy(), k - i)))
        return _max


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def getMax(nums, t):
            ans = []
            size = len(nums)
            for x in range(size):
                while ans and len(ans) + size - x > t and ans[-1] < nums[x]:
                    ans.pop()
                if len(ans) < t:
                    ans.append(nums[x])
            return ans

        def merge(nums1, nums2):
            ans = []
            for _ in nums1 + nums2:
                ans.append(max(nums1, nums2).pop(0))
            return ans

        len1, len2 = len(nums1), len(nums2)
        res = []
        for x in range(max(0, k - len2), min(k, len1) + 1):
            tmp = merge(getMax(nums1, x), getMax(nums2, k - x))
            res = max(tmp, res)
        return res


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        nums1=[3, 4, 6, 5],
        nums2=[9, 1, 2, 5, 8, 3],
        k=5
    ), [9, 8, 6, 5, 3]),
    pytest.param(dict(
        nums1=[6, 7],
        nums2=[6, 0, 4],
        k=5

    ), [6, 7, 6, 0, 4]),
    (dict(
        nums1=[3, 9],
        nums2=[8, 9],
        k=3
    ), [9, 8, 9]),
])
def test_solutions(kwargs, expected):
    assert Solution().maxNumber(**kwargs) == expected
    assert Solution1().maxNumber(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
