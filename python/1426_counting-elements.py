#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 15:22:12
# @Last Modified : 2020-08-07 15:22:12
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 arr， 对于元素 x ，只有当 x + 1 也在数组 arr 里时，才能记为 1 个数。 
# 
#  如果数组 arr 里有重复的数，每个重复的数单独计算。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [1,2,3]
# 输出：2
# 解释：1 和 2 被计算次数因为 2 和 3 在数组 arr 里。 
# 
#  示例 2： 
# 
#  输入：arr = [1,1,3,3,5,5,7,7]
# 输出：0
# 解释：所有的数都不算, 因为数组里没有 2、4、6、8。
#  
# 
#  示例 3： 
# 
#  输入：arr = [1,3,2,3,5,0]
# 输出：3
# 解释：0、1、2 被计算了因为 1、2、3 在数组里。
#  
# 
#  示例 4： 
# 
#  输入：arr = [1,1,2,2]
# 输出：2
# 解释：两个 1 被计算了因为有 2 在数组里。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 1000 
#  0 <= arr[i] <= 1000 
#  
#  Related Topics 数组 
#  👍 4 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        ans = 0
        for v in arr:
            if counter[v + 1]:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[1, 2, 3]), 2],
    [dict(arr=[1, 1, 3, 3, 5, 5, 7, 7]), 0],
    [dict(arr=[1, 3, 2, 3, 5, 0]), 3],
    [dict(arr=[1, 1, 2, 2]), 2],
    [dict(arr=[1, 1, 2]), 2],
])
def test_solutions(kw, expected):
    assert Solution().countElements(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
