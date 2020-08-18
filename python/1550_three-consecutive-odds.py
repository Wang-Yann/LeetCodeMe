#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-18 23:19:25
# @Last Modified : 2020-08-18 23:19:25
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [2,6,4,1]
# 输出：false
# 解释：不存在连续三个元素都是奇数的情况。
#  
# 
#  示例 2： 
# 
#  输入：arr = [1,2,34,3,4,5,7,23,12]
# 输出：true
# 解释：存在连续三个元素都是奇数的情况，即 [5,7,23] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 1000 
#  1 <= arr[i] <= 1000 
#  
#  Related Topics 数组 
#  👍 0 👎 0
	 

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        N = len(arr)
        for i in range(1, N - 1):
            if arr[i] % 2 and arr[i - 1] % 2 and arr[i + 1] % 2:
                return True
        return False


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(arr=[2, 6, 4, 1]), False],
    [dict(arr=[1, 3, 2]), False],
    [dict(arr=[1, 3, 3]), True],

    pytest.param(dict(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12]), True),
])
def test_solutions(kwargs, expected):
    assert Solution().threeConsecutiveOdds(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
