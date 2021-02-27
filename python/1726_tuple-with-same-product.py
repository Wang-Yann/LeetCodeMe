#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 11:51:12
# @Last Modified : 2021-02-27 11:51:12
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个由 不同 正整数组成的数组 nums ，请你返回满足 a * b = c * d 的元组 (a, b, c, d) 的数量。其中 a、b、c 和 d
#  都是 nums 中的元素，且 a != b != c != d 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,4,6]
# 输出：8
# 解释：存在 8 个满足题意的元组：
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,4,5,10]
# 输出：16
# 解释：存在 16 个满足题意的元组：
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [2,3,4,6,8,12]
# 输出：40
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [2,3,5,7]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  1 <= nums[i] <= 104 
#  nums 中的所有元素 互不相同 
#  
#  Related Topics 数组 哈希表 
#  👍 9 👎 0
  

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        从n组数对中任取2对进行组合C(n,2)
        最后，每个四元组内部有8种组合，所有最后再乘以8。

        """
        lookup = collections.Counter()
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                key = nums[i] * nums[j]
                lookup[key] += 1
        ans = 0
        for k, cnt in lookup.items():
            if cnt <= 1:
                continue
            ans += (cnt - 1) * cnt // 2 * 8

        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[2, 3, 4, 6]), 8],
    [dict(nums=[1, 2, 4, 5, 10]), 16],
    [dict(nums=[2, 3, 4, 6, 8, 12]), 40],
    [dict(nums=[2, 3, 5, 7]), 0]

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().tupleSameProduct(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
