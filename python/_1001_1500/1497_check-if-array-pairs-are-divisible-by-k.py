#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 18:59:15
# @Last Modified : 2020-07-10 18:59:15
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 arr 和一个整数 k ，其中数组长度是偶数，值为 n 。 
# 
#  现在需要把数组恰好分成 n / 2 对，以使每对数字的和都能够被 k 整除。 
# 
#  如果存在这样的分法，请返回 True ；否则，返回 False 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# 输出：true
# 解释：划分后的数字对为 (1,9),(2,8),(3,7),(4,6) 以及 (5,10) 。
#  
# 
#  示例 2： 
# 
#  输入：arr = [1,2,3,4,5,6], k = 7
# 输出：true
# 解释：划分后的数字对为 (1,6),(2,5) 以及 (3,4) 。
#  
# 
#  示例 3： 
# 
#  输入：arr = [1,2,3,4,5,6], k = 10
# 输出：false
# 解释：无法在将数组中的数字分为三对的同时满足每对数字和能够被 10 整除的条件。
#  
# 
#  示例 4： 
# 
#  输入：arr = [-10,10], k = 2
# 输出：true
#  
# 
#  示例 5： 
# 
#  输入：arr = [-1,1,-2,2,-3,3,-4,4], k = 3
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  arr.length == n 
#  1 <= n <= 10^5 
#  n 为偶数 
#  -10^9 <= arr[i] <= 10^9 
#  1 <= k <= 10^5 
#  
#  Related Topics 贪心算法 数组 数学 
#  👍 15 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """AC"""
        counter = collections.Counter()
        for v in arr:
            counter[v % k] += 1
        # print(counter, "\n")
        for i in range(k // 2 + 1):
            if i == 0:
                if counter[i] % 2 == 1:
                    return False
            else:
                j = k - i
                if counter[i] != counter[j]:
                    return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5), True],
    [dict(arr=[1, 2, 3, 4, 5, 6], k=7), True],
    [dict(arr=[1, 2, 3, 4, 5, 6], k=10), False],
    [dict(arr=[-10, 10], k=2), True],
    [dict(arr=[-1, 1, -2, 2, -3, 3, -4, 4], k=3), True],
])
def test_solutions(kw, expected):
    assert Solution().canArrange(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
