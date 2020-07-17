#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-17 11:31:57
# @Last Modified : 2020-07-17 11:31:57
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个数字数组 arr 。 
# 
#  如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。 
# 
#  如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [3,5,1]
# 输出：true
# 解释：对数组重新排序得到 [1,3,5] 或者 [5,3,1] ，任意相邻两项的差分别为 2 或 -2 ，可以形成等差数列。
#  
# 
#  示例 2： 
# 
#  输入：arr = [1,2,4]
# 输出：false
# 解释：无法通过重新排序得到等差数列。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= arr.length <= 1000 
#  -10^6 <= arr[i] <= 10^6 
#  
#  Related Topics 排序 数组 
#  👍 0 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return len({arr[i + 1] - arr[i] for i in range(len(arr) - 1)}) == 1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[3, 5, 1]), True],
    [dict(arr=[1, 2, 4]), False],
])
def test_solutions(kw, expected):
    assert Solution().canMakeArithmeticProgression(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
