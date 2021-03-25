#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。 
# 
# 
#  你可以 任意多次交换 在 pairs 中任意一对索引处的字符。 
# 
#  返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。 
# 
#  
# 
#  示例 1: 
# 
#  输入：s = "dcab", pairs = [[0,3],[1,2]]
# 输出："bacd"
# 解释： 
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[1] 和 s[2], s = "bacd"
#  
# 
#  示例 2： 
# 
#  输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# 输出："abcd"
# 解释：
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[0] 和 s[2], s = "acbd"
# 交换 s[1] 和 s[2], s = "abcd" 
# 
#  示例 3： 
# 
#  输入：s = "cba", pairs = [[0,1],[1,2]]
# 输出："abc"
# 解释：
# 交换 s[0] 和 s[1], s = "bca"
# 交换 s[1] 和 s[2], s = "bac"
# 交换 s[0] 和 s[1], s = "abc"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  0 <= pairs.length <= 10^5 
#  0 <= pairs[i][0], pairs[i][1] < s.length 
#  s 中只含有小写英文字母 
#  
#  Related Topics 并查集 数组

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        uf = UnionFind(N)
        for u, v in pairs:
            uf.union_set(u, v)
        res = list(s)
        groups = collections.defaultdict(list)
        for idx, root in enumerate([uf.find_set(x) for x in uf.set]):
            groups[root].append(idx)
        for vs in groups.values():
            chars = sorted([s[i] for i in vs])
            for i, char in zip(vs, chars):
                res[i] = char

        return "".join(res)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="dcab", pairs=[[0, 3], [1, 2]]), "bacd"],
    [dict(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]), "abcd"],
    [dict(s="cba", pairs=[[0, 1], [1, 2]]), "abc"],
])
def test_solutions(kw, expected):
    assert Solution().smallestStringWithSwaps(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
