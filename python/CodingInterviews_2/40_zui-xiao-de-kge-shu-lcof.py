#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 17:47:49
# @Last Modified : 2020-05-10 17:47:49
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#
#
#
#  示例 1：
#
#  输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#
#
#  示例 2：
#
#  输入：arr = [0,1,2,1], k = 1
# 输出：[0]
#
#
#
#  限制：
#
#
#  0 <= k <= arr.length <= 10000
#  0 <= arr[i] <= 10000
#
#  Related Topics 堆 分治算法
#  👍 107 👎 0

import heapq
from typing import List

import pytest


class Solution:

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        min_heap = [-x for x in arr[:k]]
        heapq.heapify(min_heap)
        # print(min_heap)
        for v in arr[k:]:
            if -min_heap[0] > v:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, -v)
        return [-x for x in min_heap]


@pytest.mark.parametrize("kwargs,expected", [
    (dict(arr=[3, 2, 1], k=2), [1, 2]),
    pytest.param(dict(arr=[0, 1, 2, 1], k=1), [0]),
])
def test_solutions(kwargs, expected):
    assert sorted(Solution().getLeastNumbers(**kwargs)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
