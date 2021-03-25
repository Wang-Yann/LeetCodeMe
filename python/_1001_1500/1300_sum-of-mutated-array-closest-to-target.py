#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，数组的和
# 最接近 target （最接近表示两者之差的绝对值最小）。 
# 
#  如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。 
# 
#  请注意，答案不一定是 arr 中的数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [4,9,3], target = 10
# 输出：3
# 解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
#  
# 
#  示例 2： 
# 
#  输入：arr = [2,3,5], target = 10
# 输出：5
#  
# 
#  示例 3： 
# 
#  输入：arr = [60864,25176,27249,21296,20204], target = 56803
# 输出：11361
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^4 
#  1 <= arr[i], target <= 10^5 
#  
#  Related Topics 数组 二分查找

"""

import bisect
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        N = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
        r, ans, diff = arr[-1], 0, target
        for i in range(1, r + 1):
            it = bisect.bisect_left(arr, i)
            cur = prefix[it] + (N - it) * i
            if abs(cur - target) < diff:
                ans, diff = i, abs(cur - target)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        arr=[4, 9, 3], target=10
    ), 3),
    pytest.param(dict(arr=[2, 3, 5], target=10), 5),
    pytest.param(dict(arr=[60864, 25176, 27249, 21296, 20204], target=56803), 11361),
])
def test_solutions(kwargs, expected):
    assert Solution().findBestValue(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
