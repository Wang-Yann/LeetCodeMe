#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums 和一个正整数 k，请你判断是否可以把这个数组划分成一些由 k 个连续数字组成的集合。 
# 如果可以，请返回 True；否则，返回 False。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,3,3,4,4,5,6], k = 4
# 输出：true
# 解释：数组可以分成 [1,2,3,4] 和 [3,4,5,6]。
#  
# 
#  示例 2： 
# 
#  输入：nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# 输出：true
# 解释：数组可以分成 [1,2,3] , [2,3,4] , [3,4,5] 和 [9,10,11]。
#  
# 
#  示例 3： 
# 
#  输入：nums = [3,3,2,2,1,1], k = 3
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：nums = [1,2,3,4], k = 3
# 输出：false
# 解释：数组不能分成几个大小为 3 的子数组。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  1 <= nums[i] <= 10^9 
#  1 <= k <= nums.length 
#  
#  Related Topics 贪心算法 数组

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = collections.Counter(nums)
        for num in sorted(counter.keys()):
            cnt = counter[num]
            if cnt == 0:
                continue
            for v in range(num, num + k):
                if counter[v] < cnt:
                    return False
                counter[v] -= cnt
        # print(counter)
        return True


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2, 3, 3, 4, 4, 5, 6], k=4), True],
    [dict(nums=[3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], k=3), True],
    [dict(nums=[3, 3, 2, 2, 1, 1], k=3), True],
    [dict(nums=[1, 2, 3, 4], k=3), False],
])
def test_solutions(kw, expected):
    assert Solution().isPossibleDivide(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
