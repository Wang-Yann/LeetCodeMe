#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 20:48:12
# @Last Modified : 2020-07-13 20:48:12
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给定一个放有字符和数字的数组，找到最长的子数组，且包含的字符和数字的个数相同。 
# 
#  返回该子数组，若存在多个最长子数组，返回左端点最小的。若不存在这样的数组，返回一个空数组。 
# 
#  示例 1: 
# 
#  输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K",
# "L","M"]
# 
# 输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
#  
# 
#  示例 2: 
# 
#  输入: ["A","A"]
# 
# 输出: []
#  
# 
#  提示： 
# 
#  
#  array.length <= 100000 
#  
#  Related Topics 数组 
#  👍 17 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findLongestSubarray(self, array: List[str]) -> List[str]:
        """AC"""
        N = len(array)
        nums = [-1 if char.isdigit() else 1 for char in array]
        prefix = [0]
        for i in range(N):
            prefix.append(prefix[-1] + nums[i])
        lookup = {}
        l = r = 0
        for i, v in enumerate(prefix):
            if v in lookup:
                if i - lookup[v] > r - l:
                    l, r = lookup[v], i
            else:
                lookup[v] = i
        return array[l:r]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (["A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"]
     , ["A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7"]),
    pytest.param(["A", "A"], []),
    pytest.param(["A", "1"], ["A", "1"]),
])
def test_solutions(args, expected):
    assert Solution().findLongestSubarray(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
