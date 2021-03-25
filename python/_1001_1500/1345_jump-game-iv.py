#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 19:48:01
# @Last Modified : 2020-07-05 19:48:01
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个整数数组 arr ，你一开始在数组的第一个元素处（下标为 0）。 
# 
#  每一步，你可以从下标 i 跳到下标： 
# 
#  
#  i + 1 满足：i + 1 < arr.length 
#  i - 1 满足：i - 1 >= 0 
#  j 满足：arr[i] == arr[j] 且 i != j 
#  
# 
#  请你返回到达数组最后一个元素的下标处所需的 最少操作次数 。 
# 
#  注意：任何时候你都不能跳到数组外面。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
# 输出：3
# 解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。
#  
# 
#  示例 2： 
# 
#  输入：arr = [7]
# 输出：0
# 解释：一开始就在最后一个元素处，所以你不需要跳跃。
#  
# 
#  示例 3： 
# 
#  输入：arr = [7,6,9,6,9,6,9,7]
# 输出：1
# 解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。
#  
# 
#  示例 4： 
# 
#  输入：arr = [6,1,9]
# 输出：2
#  
# 
#  示例 5： 
# 
#  输入：arr = [11,22,7,7,7,7,7,7,7,22,13]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 5 * 10^4 
#  -10^8 <= arr[i] <= 10^8 
#  
#  Related Topics 广度优先搜索 
#  👍 29 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minJumps(self, arr: List[int]) -> int:
        graph = collections.defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)
        q = collections.deque([(0, 0)])
        lookup = {0}
        step=0
        while q:
            pos, step = q.popleft()
            if pos == len(arr) - 1:
                break
            neighbors = set(graph[arr[pos]] + [pos - 1, pos + 1])
            graph[arr[pos]] = []
            for nei in neighbors:
                if 0 <= nei <= len(arr) - 1 and nei not in lookup:
                    lookup.add(nei)
                    q.append((nei, step + 1))
        return step

# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]), 3),
    pytest.param(dict(arr=[7]), 0),
    pytest.param(dict(arr=[7, 6, 9, 6, 9, 6, 9, 7]), 1),
    pytest.param(dict(arr=[6, 1, 9]), 2),
    pytest.param(dict(arr=[11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]), 3),
])
def test_solutions(kwargs, expected):
    assert Solution().minJumps(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
