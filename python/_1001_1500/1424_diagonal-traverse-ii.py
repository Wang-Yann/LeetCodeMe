#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个列表 nums ，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回 nums 中对角线上的整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：nums = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,4,2,7,5,3,8,6,9]
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# 输出：[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
#  
# 
#  示例 3： 
# 
#  输入：nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
# 输出：[1,4,2,5,3,8,6,9,7,10,11]
#  
# 
#  示例 4： 
# 
#  输入：nums = [[1,2,3,4,5,6]]
# 输出：[1,2,3,4,5,6]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  1 <= nums[i].length <= 10^5 
#  1 <= nums[i][j] <= 10^9 
#  nums 中最多有 10^5 个数字。 
#  
#  Related Topics 排序 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        for r, row in enumerate(nums):
            for c, num in enumerate(row):
                if len(res) <= r + c:
                    res.append([])
                res[r + c].append(num)
        # print(res)
        return [num for row in res for num in reversed(row)]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 4, 2, 7, 5, 3, 8, 6, 9]],
    [dict(nums=[[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]),
     [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]],
    [dict(nums=[[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]]), [1, 4, 2, 5, 3, 8, 6, 9, 7, 10, 11]],
    [dict(nums=[[1, 2, 3, 4, 5, 6]]), [1, 2, 3, 4, 5, 6]],
])
def test_solutions(kw, expected):
    assert Solution().findDiagonalOrder(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
