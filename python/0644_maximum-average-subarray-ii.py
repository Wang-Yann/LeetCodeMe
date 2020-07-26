#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-24 11:19:41
# @Last Modified : 2020-07-24 11:19:41
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个包含 n 个整数的数组，找到最大平均值的连续子序列，且长度大于等于 k。并输出这个最大平均值。 
# 
#  样例 1: 
# 
#  输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释:
# 当长度为 5 的时候，最大平均值是 10.8，
# 当长度为 6 的时候，最大平均值是 9.16667。
# 所以返回值是 12.75。
#  
# 
#  
# 
#  注释 : 
# 
#  
#  1 <= k <= n <= 10,000。 
#  数组中的元素范围是 [-10,000, 10,000]。 
#  答案的计算误差小于 10-5 。 
#  
# 
#  
#  Related Topics 数组 二分查找 
#  👍 31 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def check_subarray(average):
            """
            GOOD
            求这个数组中，是否有长度 >= k 的 subarray，他的和超过 0
            """
            prefix_sum = [0]
            for num in nums:
                prefix_sum.append(prefix_sum[-1] + num - average)

            min_prefix_sum = 0
            for i in range(k, len(nums) + 1):
                if prefix_sum[i] - min_prefix_sum >= 0:
                    return True
                min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])

            return False

        if not nums:
            return 0
        start, end = min(nums), max(nums)
        while end - start > 1e-5:
            # 浮点数还能二分逼近...
            # print(start,end)
            mid = (start + end) / 2
            if check_subarray(mid):
                start = mid
            else:
                end = mid
        return start


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 12, -5, -6, 50, 3], k=4), 12.75],
])
def test_solutions(kw, expected):
    res = Solution().findMaxAverage(**kw)
    assert res == pytest.approx(expected, 1e-5)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
