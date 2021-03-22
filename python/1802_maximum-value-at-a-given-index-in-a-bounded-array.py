#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-22 03:28:30
# @Last Modified : 2021-03-22 03:28:30
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）： 
# 
#  
#  nums.length == n 
#  nums[i] 是 正整数 ，其中 0 <= i < n 
#  abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1 
#  nums 中所有元素之和不超过 maxSum 
#  nums[index] 的值被 最大化 
#  
# 
#  返回你所构造的数组中的 nums[index] 。 
# 
#  注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 4, index = 2,  maxSum = 6
# 输出：2
# 解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
#  
# 
#  示例 2： 
# 
#  输入：n = 6, index = 1,  maxSum = 10
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= maxSum <= 109 
#  0 <= index < n 
#  
#  Related Topics 贪心算法 二分查找 
#  👍 14 👎 0


import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def check(x):
            sum_val = x + n - 1
            left = min(index, x - 1)
            right = min(n - index - 1, x - 1)
            sum_val += ((x - left) + (x - 1)) * left // 2
            sum_val += ((x - 1) + (x - right)) * right // 2
            return sum_val - left - right <= maxSum

        lo, hi = 1, maxSum + 1
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=4, index=2, maxSum=6), 2],
    [dict(n=6, index=1, maxSum=10), 3],
    [dict(n=4, index=0, maxSum=4), 1],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().maxValue(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
