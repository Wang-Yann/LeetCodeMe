#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-19 07:03:56
# @Last Modified : 2021-03-19 07:03:56
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个整数数组 nums （下标从 0 开始）和一个整数 k 。 
# 
#  一个子数组 (i, j) 的 分数 定义为 min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1) 。一个
#  好 子数组的两个端点下标需要满足 i <= k <= j 。 
# 
#  请你返回 好 子数组的最大可能 分数 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,4,3,7,4,5], k = 3
# 输出：15
# 解释：最优子数组的左右端点下标是 (1, 5) ，分数为 min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [5,5,4,5,4,1,1,1], k = 0
# 输出：20
# 解释：最优子数组的左右端点下标是 (0, 4) ，分数为 min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  1 <= nums[i] <= 2 * 104 
#  0 <= k < nums.length 
#  
#  Related Topics 贪心算法 
#  👍 25 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = mini = nums[k]
        i = j = k
        while i > 0 or j < N - 1:
            l = nums[i - 1] if i else 0
            r = nums[j + 1] if j < N - 1 else 0
            if l < r:
                j += 1
            else:
                i -= 1
            mini = min(mini, nums[i], nums[j])
            res = max(res, mini * (j - i + 1))
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 4, 3, 7, 4, 5], k=3), 15],
    [dict(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0), 20],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().maximumScore(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
