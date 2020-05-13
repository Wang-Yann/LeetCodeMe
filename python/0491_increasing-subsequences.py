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

from typing import List

import pytest


class Solution1:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        length = len(nums)
        if length < 2: return []

        def dfs(idx, cur_path):
            if len(cur_path) >= 2:
                res.add(tuple(cur_path))
            for i in range(idx + 1, length):
                if nums[i] >= nums[idx]:
                    dfs(i, cur_path + [nums[i]])

        for i in range(length - 1):
            dfs(i, [nums[i]])
        return [list(x) for x in res]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        回溯 　剪枝
        """
        ans = []
        length = len(nums)
        if length < 2: return []

        def dfs(pos, cur_path):
            if len(cur_path) >= 2:
                ans.append(list(cur_path))
            lookup = set()
            for i in range(pos, length):
                if (not cur_path
                    or nums[i] >= cur_path[-1]
                ) and nums[i] not in lookup:
                    lookup.add(nums[i])
                    cur_path.append(nums[i])
                    dfs(i + 1, cur_path)
                    cur_path.pop()

        dfs(0, [])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([4, 6, 7, 7], [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7, 7], [4, 7, 7]])
])
def test_solutions(args, expected):
    res = sorted(Solution().findSubsequences(args))
    res1 = sorted(Solution1().findSubsequences(args))
    assert res == sorted(expected)
    assert res1 == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
