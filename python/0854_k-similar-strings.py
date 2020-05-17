#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 如果可以通过将 A 中的两个小写字母精确地交换位置 K 次得到与 B 相等的字符串，我们称字符串 A 和 B 的相似度为 K（K 为非负整数）。 
# 
#  给定两个字母异位词 A 和 B ，返回 A 和 B 的相似度 K 的最小值。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = "ab", B = "ba"
# 输出：1
#  
# 
#  示例 2： 
# 
#  输入：A = "abc", B = "bca"
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：A = "abac", B = "baca"
# 输出：2
#  
# 
#  示例 4： 
# 
#  输入：A = "aabc", B = "abca"
# 输出：2 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length == B.length <= 20 
#  A 和 B 只包含集合 {'a', 'b', 'c', 'd', 'e', 'f'} 中的小写字母。 
#  
#  Related Topics 广度优先搜索 图

"""
import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def kSimilarity(self, A: str, B: str) -> int:
        """
        TODO HARD
        BFS
        """

        def get_neighbors(S):
            for i, c in enumerate(S):
                if c != B[i]:
                    break
            T = list(S)
            for j in range(i + 1, len(S)):
                if S[j] == B[i]:
                    T[i], T[j] = T[j], T[i]
                    yield "".join(T)
                    T[j], T[i] = T[i], T[j]

        queue = collections.deque([A])
        seen = {A:0}
        while queue:
            node = queue.popleft()
            if node == B:
                return seen[node]
            for neighbor in get_neighbors(node):
                if neighbor not in seen:
                    seen[neighbor] = seen[node] + 1
                    queue.append(neighbor)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def kSimilarity(self, A: str, B: str) -> int:
        """
        BFS
        """
        if A == B:
            return 0
        vis = set()
        queue = collections.deque()
        vis.add(A)
        queue.append(A)
        res = 0
        while queue:
            res += 1
            size = len(queue)
            for i in range(size):
                s = queue.popleft()
                i = 0
                while s[i] == B[i]:
                    i += 1
                for j in range(i + 1, len(A)):
                    if s[j] == B[j] or s[i] != B[j]:
                        continue
                    ss = [c for c in s]
                    ss[i], ss[j] = s[j], s[i]
                    ss = "".join(ss)
                    if ss == B:
                        return res
                    if ss not in vis:
                        vis.add(ss)
                        queue.append(ss)
        return res


@pytest.mark.parametrize("kwargs,expected", [
    (dict(A="ab", B="ba"), 1),
    pytest.param(dict(A="abc", B="bca"), 2),
    pytest.param(dict(A="abac", B="baca"), 2),
    pytest.param(dict(A="aabc", B="abca"), 2),
])
def test_solutions(kwargs, expected):
    assert Solution().kSimilarity(**kwargs) == expected
    assert Solution1().kSimilarity(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
