#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。 
# 
#  现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。 
# 
#  示例 1: 
# 
#  
# 输入: [1,3,2,2,5,2,3,7]
# 输出: 5
# 原因: 最长的和谐数组是：[3,2,2,2,3].
#  
# 
#  说明: 输入的数组长度最大不超过20,000. 
#  Related Topics 哈希表

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        ans = 0
        items = sorted(counter.most_common())
        for a, b in zip(items, items[1:]):
            if abs(a[0] - b[0]) == 1:
                ans = max(a[1] + b[1], ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    def findLHS(self, nums):
        lookup = collections.defaultdict(int)
        result = 0
        for num in nums:
            lookup[num] += 1
            for diff in [-1, 1]:
                if (num + diff) in lookup:
                    result = max(result, lookup[num] + lookup[num + diff])
        return result


@pytest.mark.parametrize("args,expected", [
    ([1, 3, 2, 2, 5, 2, 3, 7], 5),
    ([1, 1, 1, 1], 0)
])
def test_solutions(args, expected):
    assert Solution().findLHS(args) == expected
    assert Solution1().findLHS(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
