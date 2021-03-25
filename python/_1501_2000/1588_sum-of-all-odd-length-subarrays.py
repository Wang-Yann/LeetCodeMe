#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-24 06:58:45
# @Last Modified : 2021-02-24 06:58:45
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

# 给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。 
# 
#  子数组 定义为原数组中的一个连续子序列。 
# 
#  请你返回 arr 中 所有奇数长度子数组的和 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [1,4,2,5,3]
# 输出：58
# 解释：所有奇数长度子数组和它们的和为：
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# 我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58 
# 
#  示例 2： 
# 
#  输入：arr = [1,2]
# 输出：3
# 解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。 
# 
#  示例 3： 
# 
#  输入：arr = [10,11,12]
# 输出：66
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 100 
#  1 <= arr[i] <= 1000 
#  
#  Related Topics 数组 
#  👍 46 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """暴力就可以过"""
        res, n = 0, len(arr)
        for i, a in enumerate(arr):
            res += ((i + 1) * (n - i) + 1) // 2 * a
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[1, 4, 2, 5, 3]), 58],
    [dict(arr=[1, 2]), 3],
    [dict(arr=[10, 11, 12]), 66],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().sumOddLengthSubarrays(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
