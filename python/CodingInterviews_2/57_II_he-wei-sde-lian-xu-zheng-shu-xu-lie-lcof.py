#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。 
# 
#  序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：target = 9
# 输出：[[2,3,4],[4,5]]
#  
# 
#  示例 2： 
# 
#  输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= target <= 10^5 
#  
# 
#  
# 

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """
        Sliding window
        """
        l, r = 1, 1
        sum = 0
        res = []
        while l <= target // 2:
            if sum < target:
                # 右边界向右移动
                sum += r
                r += 1
            elif sum > target:
                # 左边界向右移动
                sum -= l
                l += 1
            else:
                res.append(list(range(l, r)))
                sum -= l
                l += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (9, [[2, 3, 4], [4, 5]]),
    pytest.param(15, [[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]]),
])
def test_solutions(args, expected):
    assert Solution().findContinuousSequence(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
