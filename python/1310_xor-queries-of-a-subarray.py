#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有一个正整数数组 arr，现给你一个对应的查询数组 queries，其中 queries[i] = [Li, Ri]。 
# 
#  对于每个查询 i，请你计算从 Li 到 Ri 的 XOR 值（即 arr[Li] xor arr[Li+1] xor ... xor arr[Ri]）作为
# 本次查询的结果。 
# 
#  并返回一个包含给定查询 queries 所有结果的数组。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
# 输出：[2,7,14,8] 
# 解释：
# 数组中元素的二进制表示形式是：
# 1 = 0001 
# 3 = 0011 
# 4 = 0100 
# 8 = 1000 
# 查询的 XOR 值为：
# [0,1] = 1 xor 3 = 2 
# [1,2] = 3 xor 4 = 7 
# [0,3] = 1 xor 3 xor 4 xor 8 = 14 
# [3,3] = 8
#  
# 
#  示例 2： 
# 
#  输入：arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
# 输出：[8,0,4,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 3 * 10^4 
#  1 <= arr[i] <= 10^9 
#  1 <= queries.length <= 3 * 10^4 
#  queries[i].length == 2 
#  0 <= queries[i][0] <= queries[i][1] < arr.length 
#  
#  Related Topics 位运算

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools
from common_utils import TreeNode, ListNode


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """类似前缀和"""
        prefix = [0]
        for v in arr:
            prefix.append(prefix[-1] ^ v)
        print(prefix)
        ans = list()
        for x, y in queries:
            ans.append(prefix[x] ^ prefix[y + 1])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]), [2, 7, 14, 8]],
    [dict(arr=[4, 8, 2, 10], queries=[[2, 3], [1, 3], [0, 0], [0, 3]]), [8, 0, 4, 4]],
])
def test_solutions(kw, expected):
    assert Solution().xorQueries(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
