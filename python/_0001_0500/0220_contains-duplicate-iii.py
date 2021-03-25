#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 21:05:04
# @Last Modified : 2020-05-01 21:05:04
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的
# 绝对值也小于等于 ķ 。
#
#  如果存在则返回 true，不存在返回 false。
#
#
#
#  示例 1:
#
#  输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true
#
#  示例 2:
#
#  输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true
#
#  示例 3:
#
#  输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false
#  Related Topics 排序 Ordered Map
#  👍 196 👎 0

"""

import collections
from typing import List

import pytest


class Solution:

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """Good"""
        if k < 0 or t < 0:
            return False
        window = collections.OrderedDict()
        for num in nums:
            if len(window) > k:
                # The popitem() method for ordered dictionaries returns and removes a (key, value) pair.
                # The pairs are returned in LIFO order if last is true or FIFO order if false.
                window.popitem(last=False)
            bucket = num if not t else num // t
            # print("bucket",bucket)
            for m in (window.get(bucket - 1), window.get(bucket), window.get(bucket + 1)):
                # print(m)
                if m is not None and abs(num - m) <= t:
                    return True
            window[bucket] = num
        return False


@pytest.mark.parametrize("kw,expected", [
    (dict(nums=[1, 2, 3, 1], k=3, t=0), True),
    pytest.param(dict(nums = [1,0,1,1], k = 1, t = 2),True),
    pytest.param(dict(nums = [1,5,9,1,5,9], k = 2, t = 3),False),
])
def test_solutions(kw, expected):
    assert Solution().containsNearbyAlmostDuplicate(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
