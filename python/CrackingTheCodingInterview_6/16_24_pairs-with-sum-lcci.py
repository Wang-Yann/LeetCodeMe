#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 18:47:00
# @Last Modified : 2020-07-13 18:47:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。 
# 
#  示例 1: 
# 
#  输入: nums = [5,6,5], target = 11
# 输出: [[5,6]] 
# 
#  示例 2: 
# 
#  输入: nums = [5,6,5,6], target = 11
# 输出: [[5,6],[5,6]] 
# 
#  提示： 
# 
#  
#  nums.length <= 100000 
#  
#  Related Topics 数组 哈希表 
#  👍 7 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == target:
                res.append([nums[i], nums[j]])
                i += 1
                j -= 1
            elif (nums[i] + nums[j]) < target:
                i += 1
            else:
                j -= 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        counter = collections.Counter(nums)
        ans = []
        for k in sorted(counter.keys()):
            if counter[target - k]:
                cnt = min(counter[target - k], counter[k])
                if target != 2 * k:
                    for _ in range(cnt):
                        ans.append([k, target - k])
                    counter[k] -= cnt
                    counter[target - k] -= cnt
                else:
                    for _ in range(counter[k] // 2):
                        ans.append([k, k])

        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[5, 6, 5], target=11), [[5, 6]]],
    [dict(nums=[5, 6, 5, 6], target=11), [[5, 6], [5, 6]]],
])
def test_solutions(kw, expected):
    assert Solution().pairSums(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
