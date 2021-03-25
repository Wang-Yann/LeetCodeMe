#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 23:29:52
# @Last Modified : 2021-02-25 23:29:52
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums 和一个整数 k 。 
# 
#  每一步操作中，你需要从数组中选出和为 k 的两个整数，并将它们移出数组。 
# 
#  返回你可以对数组执行的最大操作数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,4], k = 5
# 输出：2
# 解释：开始时 nums = [1,2,3,4]：
# - 移出 1 和 4 ，之后 nums = [2,3]
# - 移出 2 和 3 ，之后 nums = []
# 不再有和为 5 的数对，因此最多执行 2 次操作。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,1,3,4,3], k = 6
# 输出：1
# 解释：开始时 nums = [3,1,3,4,3]：
# - 移出前两个 3 ，之后nums = [1,4,3]
# 不再有和为 6 的数对，因此最多执行 1 次操作。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  1 <= nums[i] <= 109 
#  1 <= k <= 109 
#  
#  Related Topics 哈希表 
#  👍 13 👎 0
  

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        ME
        """
        counter = collections.Counter(nums)
        ans = 0
        if k % 2 == 0 and k // 2 in counter:
            ans += counter[k // 2] // 2
            counter.pop(k // 2)
        for num in counter:
            if counter[k - num]>0:
                ans += min(counter[num], counter[k - num])
                counter[num] = 0
                counter[k - num] = 0
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2, 3, 4], k=5), 2],
    [dict(nums=[3, 1, 3, 4, 3], k=6), 1],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().maxOperations(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
