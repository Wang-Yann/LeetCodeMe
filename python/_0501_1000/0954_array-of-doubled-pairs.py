#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个长度为偶数的整数数组 A，只有对 A 进行重组后可以满足 “对于每个 0 <= i < len(A) / 2，都有 A[2 * i + 1] = 2
#  * A[2 * i]” 时，返回 true；否则，返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[3,1,3,6]
# 输出：false
#  
# 
#  示例 2： 
# 
#  输入：[2,1,2,6]
# 输出：false
#  
# 
#  示例 3： 
# 
#  输入：[4,-2,2,-4]
# 输出：true
# 解释：我们可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4] 
# 
#  示例 4： 
# 
#  输入：[1,2,4,16,8,4]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= A.length <= 30000 
#  A.length 为偶数 
#  -100000 <= A[i] <= 100000 
#  
#  Related Topics 数组 哈希表

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        """
        GOOD
        """
        counter = collections.Counter(A)
        for x in sorted(counter, key=abs):
            if counter[x] > counter[2 * x]:
                return False
            counter[2 * x] -= counter[x]
        return True


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([0, 0], True),
    ([1, 2, 4, 5], False),
    ([3, 1, 3, 6], False),
    ([2, 1, 2, 6], False),
    ([4, -2, 2, -4], True),
    ([1, 2, 4, 16, 8, 4], False),
])
def test_solutions(args, expected):
    assert Solution().canReorderDoubled(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
