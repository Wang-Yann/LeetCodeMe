#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。 
# 
#  示例: 
# 
#  
# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7
# ]] 
# 
#  说明: 
# 
#  
#  给定数组的长度不会超过15。 
#  数组中的整数范围是 [-100,100]。 
#  给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。 
#  
#  Related Topics 深度优先搜索

"""
import math
from typing import List

import pytest


class Solution1:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        N = len(nums)
        if N < 2: return []

        def dfs(idx, cur_path):
            if len(cur_path) >= 2:
                res.add(tuple(cur_path))
            for i in range(idx + 1, N):
                if nums[i] >= nums[idx]:
                    dfs(i, cur_path + [nums[i]])

        for i in range(N - 1):
            dfs(i, [nums[i]])
        return [list(x) for x in res]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        回溯 　剪枝
        """
        ans = []
        N = len(nums)
        if N < 2:
            return []

        def dfs(pos, cur_path):
            if len(cur_path) >= 2:
                ans.append(list(cur_path))
            lookup = set()
            for i in range(pos, N):
                if (not cur_path or nums[i] >= cur_path[-1]) and nums[i] not in lookup:
                    lookup.add(nums[i])
                    cur_path.append(nums[i])
                    dfs(i + 1, cur_path)
                    cur_path.pop()

        dfs(0, [])
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution2:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        N = len(nums)
        if N < 2:
            return []

        def dfs(pos, last, cur_path):
            if pos == N:
                if len(cur_path) >= 2:
                    ans.append(cur_path[:])
                return
            if nums[pos] >= last:
                cur_path.append(nums[pos])
                dfs(pos + 1, nums[pos], cur_path)
                cur_path.pop()
            if nums[pos] != last:
                dfs(pos + 1, last, cur_path)

        dfs(0, -math.inf, [])
        return ans


@pytest.mark.parametrize("args,expected", [
    ([4, 6, 7, 7], [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7, 7], [4, 7, 7]])
])
def test_solutions(args, expected):
    assert sorted(Solution().findSubsequences(args)) == sorted(expected)
    assert sorted(Solution1().findSubsequences(args)) == sorted(expected)
    assert sorted(Solution2().findSubsequences(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
