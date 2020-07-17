#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-28 10:57:24
# @Last Modified : 2020-04-28 10:57:24
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

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
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
            # DFS solution with pruning.
            剪枝
            注意审题:[题意文字描述有问题]
            1 <= k <= len(nums) <= 16
            0 < nums[i] < 10000
        """

        def dfs(target, i, subset_sums):
            if i == len(nums):
                return True
            # print(subset_sums)
            for idx in range(len(subset_sums)):
                if subset_sums[idx] + nums[i] > target:
                    continue
                subset_sums[idx] += nums[i]
                if dfs(target, i + 1, subset_sums):
                    return True
                subset_sums[idx] -= nums[i]
                # 可以确保每个 subset_sums 的所有 0 值都出现在数组 subset_sums 的末尾。
                # 这大大减少了重复的工作
                if subset_sums[idx] == 0: break
            return False

        if not nums: return False
        total = sum(nums)
        quotient, remainder = divmod(total, k)
        if remainder:
            return False
        nums.sort(reverse=True)
        subset_sums = [0] * k
        return dfs(quotient, 0, subset_sums)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        dict(nums=[4, 3, 2, 3, 5, 2, 1], k=4),
        # dict(nums=[1], k=1)

    ]
    lists = [x for x in samples]
    res = [sol.canPartitionKSubsets(**x) for x in lists]
    print(res)
