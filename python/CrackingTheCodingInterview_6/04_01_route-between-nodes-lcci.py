#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 18:58:42
# @Last Modified : 2020-07-12 18:58:42
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。 
# 
#  示例1: 
# 
#   输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
#  输出：true
#  
# 
#  示例2: 
# 
#   输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [
# 1, 3], [2, 3], [3, 4]], start = 0, target = 4
#  输出 true
#  
# 
#  提示： 
# 
#  
#  节点数量n在[0, 1e5]范围内。 
#  节点编号大于等于 0 小于 n。 
#  图中可能存在自环和平行边。 
#  
#  Related Topics 图 
#  👍 10 👎 0


"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        G = collections.defaultdict(list)
        for s, e in graph:
            G[s].append(e)
        seen = {start}
        dq = collections.deque([start])
        while dq:
            node = dq.popleft()
            if node == target:
                return True
            for neighbor in G[node]:
                if neighbor not in seen:
                    dq.append(neighbor)
                    seen.add(neighbor)
        return False


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=3, graph=[[0, 1], [0, 2], [1, 2], [1, 2]],
          start=0, target=2), True],

    pytest.param(
        dict(n=5, graph=[[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]],
             start=0, target=4), True),
])
def test_solutions(kwargs, expected):
    assert Solution().findWhetherExistsPath(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
