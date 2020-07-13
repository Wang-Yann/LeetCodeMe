#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 10:42:00
# @Last Modified : 2020-07-13 10:42:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#   输入： nums = [1,2,3]
#  输出：
# [
#   [3],
#  [1],
#  [2],
#  [1,2,3],
#  [1,3],
#  [2,3],
#  [1,2],
#  []
# ]
#  
#  Related Topics 位运算 数组 回溯算法 
#  👍 22 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            ans += [x + [num] for x in ans]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2, 3]),
     [
         [3],
         [1],
         [2],
         [1, 2, 3],
         [1, 3],
         [2, 3],
         [1, 2],
         []
     ]
     ],
])
def test_solutions(kw, expected):
    assert sorted(Solution().subsets(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
