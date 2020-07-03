#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。 
# 
#  如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [1,2,2,1,1,3]
# 输出：true
# 解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。 
# 
#  示例 2： 
# 
#  输入：arr = [1,2]
# 输出：false
#  
# 
#  示例 3： 
# 
#  输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 1000 
#  -1000 <= arr[i] <= 1000 
#  
#  Related Topics 哈希表

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        return len(counter.keys()) == len(set(counter.values()))


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[1, 2, 2, 1, 1, 3]), True],
    [dict(arr=[1, 2]), False],
    [dict(arr=[3, 5, -2, -3, -6, -6]), False],
    [dict(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]), True],
])
def test_solutions(kw, expected):
    assert Solution().uniqueOccurrences(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
