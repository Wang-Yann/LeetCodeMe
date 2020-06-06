#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal",
#  "Silver Medal", "Bronze Medal"）。 
# 
#  (注：分数越高的选手，排名越靠前。) 
# 
#  示例 1: 
# 
#  
# 输入: [5, 4, 3, 2, 1]
# 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# 解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and 
# "Bronze Medal").
# 余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。 
# 
#  提示: 
# 
#  
#  N 是一个正整数并且不会超过 10000。 
#  所有运动员的成绩都不相同。 
#  
# 

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        """排序好的数组"""

        sorted_list = sorted(nums, reverse=True)
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(nums) + 1)))
        ransk_map = dict(zip(sorted_list, ranks))
        return [ransk_map.get(x) for x in nums]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        sorted_list = sorted(nums, reverse=True)
        prev, rank = None, 0
        hash_map = {}
        for v in sorted_list:
            if v != prev:
                rank += 1
                prev = v
            hash_map[v] = rank
        ans = []
        for v in nums:
            rank = hash_map.get(v)
            if rank == 1:
                ans.append("Gold Medal")
            elif rank == 2:
                ans.append("Silver Medal")
            elif rank == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(rank))
        return ans


@pytest.mark.parametrize("args,expected", [
    ([5, 4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]),
    # ([5, 5, 3, 4, 1], ["Gold Medal", "Gold Medal", "Bronze Medal", "Silver Medal", "4"]),
])
def test_solutions(args, expected):
    assert Solution().findRelativeRanks(args) == expected
    assert Solution1().findRelativeRanks(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
