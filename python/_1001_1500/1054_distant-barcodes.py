#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-30 08:00:00
# @Last Modified : 2020-06-30 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。 
# 
#  请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,1,1,2,2,2]
# 输出：[2,1,2,1,2,1]
#  
# 
#  示例 2： 
# 
#  输入：[1,1,1,1,2,2,3,3]
# 输出：[1,3,1,3,2,1,2,1] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= barcodes.length <= 10000 
#  1 <= barcodes[i] <= 10000 
#  
# 
#  
#  Related Topics 堆 排序

"""

import collections
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        N = len(barcodes)
        ans = [0] * N
        i = 0
        counters = collections.Counter(barcodes)
        for num, cnt in counters.most_common():
            for _ in range(cnt):
                ans[i] = num
                i += 2
                if i >= N:
                    i = 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution１:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        ans = []
        counters = collections.Counter(barcodes)
        min_heap = []
        for num, cnt in counters.items():
            min_heap.append((-cnt, num))
        heapq.heapify(min_heap)
        while len(min_heap):
            cnt1, num1 = heapq.heappop(min_heap)
            if ans and ans[-1] == num1:
                cnt2, num2 = heapq.heappop(min_heap)
                heapq.heappush(min_heap, (cnt1, num1))
                ans.append(num2)
                cnt2 += 1
                if cnt2 < 0:
                    heapq.heappush(min_heap, (cnt2, num2))
                continue
            ans.append(num1)
            cnt1 += 1
            if cnt1 < 0:
                heapq.heappush(min_heap, (cnt1, num1))
        return ans


@pytest.mark.parametrize("args,expected", [
    ([1, 1, 1, 2, 2, 2], [2, 1, 2, 1, 2, 1]),
    ([1, 1, 1, 1, 2, 2, 3, 3], [1, 3, 1, 3, 2, 1, 2, 1]),
])
def test_solutions(args, expected):
    res = Solution().rearrangeBarcodes(args)
    res1 = Solution().rearrangeBarcodes(args)
    for a, b in zip(res, res[1:]):
        assert a != b
    for a, b in zip(res1, res1[1:]):
        assert a != b


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
