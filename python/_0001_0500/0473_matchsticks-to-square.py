#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴
# 都要用到。 
# 
#  输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。 
# 
#  示例 1: 
# 
#  
# 输入: [1,1,2,2,2]
# 输出: true
# 
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,3,3,3,4]
# 输出: false
# 
# 解释: 不能用所有火柴拼成一个正方形。
#  
# 
#  注意: 
# 
#  
#  给定的火柴长度和在 0 到 10^9之间。 
#  火柴数组的长度不超过15。 
#  
#  Related Topics 深度优先搜索

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        """DFS"""
        if not nums:
            return False
        length = len(nums)
        total_length = sum(nums)
        if total_length % 4:
            return False
        possible_side = total_length // 4
        nums.sort(reverse=True)
        # This array represents the 4 sides and their current lengths

        sums = [0 for _ in range(4)]

        def dfs(idx):
            if idx == length:
                return all(x == possible_side for x in sums)
            for i in range(4):
                if sums[i] + nums[idx] <= possible_side:
                    sums[i] += nums[idx]
                    if dfs(idx + 1):
                        return True
                    sums[i] -= nums[idx]
            return False

        return dfs(0)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([1, 1, 2, 2, 2], True),
    ([3, 3, 3, 3, 4], False),
])
def test_solutions(args, expected):
    assert Solution().makesquare(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
