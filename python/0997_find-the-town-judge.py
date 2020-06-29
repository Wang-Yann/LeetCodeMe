#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。 
# 
#  如果小镇的法官真的存在，那么： 
# 
#  
#  小镇的法官不相信任何人。 
#  每个人（除了小镇法官外）都信任小镇的法官。 
#  只有一个人同时满足属性 1 和属性 2 。 
#  
# 
#  给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。 
# 
#  如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：N = 2, trust = [[1,2]]
# 输出：2
#  
# 
#  示例 2： 
# 
#  输入：N = 3, trust = [[1,3],[2,3]]
# 输出：3
#  
# 
#  示例 3： 
# 
#  输入：N = 3, trust = [[1,3],[2,3],[3,1]]
# 输出：-1
#  
# 
#  示例 4： 
# 
#  输入：N = 3, trust = [[1,2],[2,3]]
# 输出：-1
#  
# 
#  示例 5： 
# 
#  输入：N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# 输出：3 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 1000 
#  trust.length <= 10000 
#  trust[i] 是完全不同的 
#  trust[i][0] != trust[i][1] 
#  1 <= trust[i][0], trust[i][1] <= N 
#  
#  Related Topics 图

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        degrees = [0] * N
        for start, end in trust:
            degrees[start - 1] -= 1
            degrees[end - 1] += 1
        for i, v in enumerate(degrees):
            if degrees[i] == N - 1:
                return i + 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if N == 1 else -1
        graph = collections.defaultdict(list)
        for start, end in trust:
            graph[end].append(start)
        target, from_list = max(graph.items(), key=lambda x:len(x[1]))
        if len(from_list) != N - 1:
            return -1
        for k, vs in graph.items():
            if target in vs:
                return -1
        return target


@pytest.mark.parametrize("kwargs,expected", [
    (dict(N=1, trust=[]), 1),
    (dict(N=2, trust=[[1, 2]]), 2),
    pytest.param(dict(N=3, trust=[[1, 3], [2, 3]]), 3),
    pytest.param(dict(N=3, trust=[[1, 3], [2, 3], [3, 1]]), -1),
    pytest.param(dict(N=3, trust=[[1, 2], [2, 3]]), -1),
    pytest.param(dict(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]), 3),
])
def test_solutions(kwargs, expected):
    assert Solution1().findJudge(**kwargs) == expected
    assert Solution().findJudge(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
