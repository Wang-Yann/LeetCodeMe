#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 10:52:47
# @Last Modified : 2020-04-30 10:52:47
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
#
#  说明:
# 最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。
#
#  示例:
#
#  输入: nums = [-2,5,-1], lower = -2, upper = 2,
# 输出: 3
# 解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。
#
#  Related Topics 排序 树状数组 线段树 二分查找 分治算法
#  👍 104 👎 0

"""
import bisect
from typing import List

import pytest


class Solution:
    """归并排序+前缀和"""

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def countAndMergeSort(sums, start, end):
            # 左闭右开
            # The size of range [start, end) less than 2 is always with count 0.
            if end - start <= 1:
                return 0
            mid = (start + end) >> 1
            count = countAndMergeSort(sums, start, mid) + \
                    countAndMergeSort(sums, mid, end)
            Upper, Lower, rPos = mid, mid, mid
            tmp = []
            l = start
            for i in range(l, mid):
                # Count the number of range sums that lie in [lower, upper].
                while Lower < end and sums[Lower] - sums[i] < lower:
                    Lower += 1
                while Upper < end and sums[Upper] - sums[i] <= upper:
                    Upper += 1
                count += Upper - Lower
                # Merge the two sorted arrays into tmp.
                while rPos < end and sums[rPos] < sums[i]:
                    tmp.append(sums[rPos])
                    rPos += 1
                tmp.append(sums[i])
            # Copy tmp back to sums.
            sums[start:start + len(tmp)] = tmp
            # print("tmp,sums",tmp,sums )
            return count

        sums = [0] * (len(nums) + 1)
        for idx in range(len(nums)):
            sums[idx + 1] = sums[idx] + nums[idx]
        return countAndMergeSort(sums, 0, len(sums))


class Solution1:

    def countRangeSum(self, nums, lower, upper):
        N = len(nums)
        Sum, BITree = [0] * (N + 1), [0] * (N + 2)

        def count(x):
            s = 0
            while x:
                s += BITree[x]
                x -= (x & -x)
            return s

        def update(x):
            while x <= N + 1:
                BITree[x] += 1
                x += (x & -x)

        for i in range(N):
            Sum[i + 1] = Sum[i] + nums[i]
        sortSum, res = sorted(Sum), 0
        for sum_j in Sum:
            sum_i_count = count(bisect.bisect_right(sortSum, sum_j - lower)) - count(bisect.bisect_left(sortSum, sum_j - upper))
            res += sum_i_count
            update(bisect.bisect_left(sortSum, sum_j) + 1)
        return res


@pytest.mark.parametrize("args,expected", [
    (([-2, 5, -1], -2, 2), 3)
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(args, expected, SolutionCLS):
    assert SolutionCLS().countRangeSum(*args) == expected


if __name__ == '__main__':
    # pytest -s            # disable all capturing
    # pytest --capture=sys # replace sys.stdout/stderr with in-mem files
    # pytest --capture=fd  # also point filedescriptors 1 and 2 to temp file
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
