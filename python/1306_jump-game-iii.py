#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 这里有一个非负整数数组 arr，你最开始位于该数组的起始下标 start 处。当你位于下标 i 处时，你可以跳到 i + arr[i] 或者 i - arr
# [i]。 
# 
#  请你判断自己是否能够跳到对应元素值为 0 的 任一 下标处。 
# 
#  注意，不管是什么情况下，你都无法跳到数组之外。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [4,2,3,0,3,1,2], start = 5
# 输出：true
# 解释：
# 到达值为 0 的下标 3 有以下可能方案： 
# 下标 5 -> 下标 4 -> 下标 1 -> 下标 3 
# 下标 5 -> 下标 6 -> 下标 4 -> 下标 1 -> 下标 3 
#  
# 
#  示例 2： 
# 
#  输入：arr = [4,2,3,0,3,1,2], start = 0
# 输出：true 
# 解释：
# 到达值为 0 的下标 3 有以下可能方案： 
# 下标 0 -> 下标 4 -> 下标 1 -> 下标 3
#  
# 
#  示例 3： 
# 
#  输入：arr = [3,0,2,1,2], start = 2
# 输出：false
# 解释：无法到达值为 0 的下标 1 处。 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 5 * 10^4 
#  0 <= arr[i] < arr.length 
#  0 <= start < arr.length 
#  
#  Related Topics 广度优先搜索 图

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools
from common_utils import TreeNode, ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        BFS
        """
        N = len(arr)
        dq, lookup = collections.deque([start]), {start}
        while dq:
            idx = dq.popleft()
            if arr[idx] == 0:
                return True
            for ni in (idx + arr[idx], idx - arr[idx]):
                if 0 <= ni <= N - 1 and ni not in lookup:
                    dq.append(ni)
                    lookup.add(ni)
        return False


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[4, 2, 3, 0, 3, 1, 2], start=5), True],
    [dict(arr=[4, 2, 3, 0, 3, 1, 2], start=0), True],
    [dict(arr=[3, 0, 2, 1, 2], start=2), False],
])
def test_solutions(kw, expected):
    assert Solution().canReach(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
