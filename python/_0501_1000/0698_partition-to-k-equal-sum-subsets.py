#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-28 10:57:24
# @Last Modified : 2020-04-28 10:57:24
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

"""

# 给定一个整数数组 nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
#
#  示例 1：
#
#  输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
#
#
#
#  提示：
#
#
#  1 <= k <= len(nums) <= 16
#  0 < nums[i] < 10000
#
#  Related Topics 递归 动态规划
#  👍 196 👎 0

"""

from typing import List

import pytest


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
            # DFS solution with pruning.
            剪枝
            注意审题:[题意文字描述有问题]
            1 <= k <= len(nums) <= 16
            0 < nums[i] < 10000
            对于 nums 中的每个数字，我们可以将其添加到 k 个子集中的一个，只要该子集的和不会超过目标值。对于每一个选择，
            我们都递归地用一个更小的数字进行搜索，以便在nums中考虑。如果我们成功地放置了每个数字，那么我们的搜索就成功了

        """

        def dfs(target, i, subset_sums):
            if i == len(nums):
                return True
            # print(subset_sums)
            for idx in range(k):
                if subset_sums[idx] + nums[i] > target:
                    continue
                subset_sums[idx] += nums[i]
                if dfs(target, i + 1, subset_sums):
                    return True
                subset_sums[idx] -= nums[i]
                # 可以确保每个 subset_sums 的所有 0 值都出现在数组 subset_sums 的末尾。
                # 这大大减少了重复的工作
                if subset_sums[idx] == 0:
                    break
            return False

        if not nums:
            return False
        total = sum(nums)
        quotient, remainder = divmod(total, k)
        if remainder:
            return False
        nums.sort(reverse=True)
        subset_sums = [0] * k
        return dfs(quotient, 0, subset_sums)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[4, 3, 2, 3, 5, 2, 1], k=4), True],
    [dict(nums=[1], k=1), True],
])
def test_solutions(kw, expected):
    assert Solution().canPartitionKSubsets(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
