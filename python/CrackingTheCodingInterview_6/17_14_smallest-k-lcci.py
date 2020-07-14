#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-14 21:58:26
# @Last Modified : 2020-07-14 21:58:26
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。 
# 
#  示例： 
# 
#  输入： arr = [1,3,5,7,2,4,6,8], k = 4
# 输出： [1,2,3,4]
#  
# 
#  提示： 
# 
#  
#  0 <= len(arr) <= 100000 
#  0 <= k <= min(100000, len(arr)) 
#  
#  Related Topics 堆 排序 分治算法 
#  👍 17 👎 0


"""

import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        max_heap = []
        for v in arr:
            if len(max_heap) == k:
                if -max_heap[0] > v:
                    heapq.heappop(max_heap)
                else:
                    continue
            heapq.heappush(max_heap, -v)
        return [-x for x in max_heap]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(arr=[1, 3, 5, 7, 2, 4, 6, 8], k=4), [1, 2, 3, 4]],

])
def test_solutions(kwargs, expected):
    assert sorted(Solution().smallestK(**kwargs)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
