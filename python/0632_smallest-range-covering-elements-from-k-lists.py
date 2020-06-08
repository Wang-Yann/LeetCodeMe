#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。 
# 
#  我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。 
# 
#  示例 1: 
# 
#  
# 输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# 输出: [20,24]
# 解释: 
# 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
# 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
# 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
#  
# 
#  注意: 
# 
#  
#  给定的列表可能包含重复元素，所以在这里升序表示 >= 。 
#  1 <= k <= 3500 
#  -105 <= 元素的值 <= 105 
#  对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。 
#  
#  Related Topics 哈希表 双指针 字符串

"""
import heapq
import sys
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        GOOD
        """
        left, right = sys.maxsize, -sys.maxsize
        min_heap = []
        for row in nums:
            first = row.pop(0)
            left = min(left, first)
            right = max(right, first)
            # iterator = iter(row)
            # heapq.heappush(min_heap, (next(iterator, None), iterator))
            heapq.heappush(min_heap, (first, row))

        ans = [left, right]
        while min_heap:
            _, iterator = heapq.heappop(min_heap)
            if not iterator:
                break
            val = iterator.pop(0)
            heapq.heappush(min_heap, (val, iterator))
            left, right = min_heap[0][0], max(right, val)
            # print(left,right,val,min_heap)
            if right - left < ans[1] - ans[0]:
                ans = [left, right]
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], [20, 24]),
    ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], [1, 1])
])
def test_solutions(args, expected):
    assert Solution().smallestRange(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
