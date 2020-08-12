#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。 
# 
#  示例 1 : 
# 
#  
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#  
# 
#  说明 : 
# 
#  
#  数组的长度为 [1, 20,000]。 
#  数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。 
#  
#  Related Topics 数组 哈希表

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        TODO
        它用于存储所有可能的索引的累积总和以及相同累加和发生的次数。我们以以下形式存储数据：(sum_i,sum_i出现次数）

        """
        result = 0
        accumulated_sum = 0
        lookup = collections.defaultdict(int)
        lookup[0] += 1
        for num in nums:
            accumulated_sum += num
            result += lookup[accumulated_sum - k]
            lookup[accumulated_sum] += 1
        return result


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    """前缀和

    超时 TLE
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        length = len(nums)
        accumulated_sums = [0]
        for i in range(1, length + 1):
            accumulated_sums.append(accumulated_sums[i - 1] + nums[i - 1])
        for start in range(length):
            for end in range(start + 1, length + 1):
                if accumulated_sums[end] - accumulated_sums[start] == k:
                    cnt += 1
        return cnt


@pytest.mark.parametrize("kwargs,expected", [
    (dict(nums=[1, 1, 1], k=2), 2),
])
def test_solutions(kwargs, expected):
    assert Solution().subarraySum(**kwargs) == expected
    assert Solution1().subarraySum(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
