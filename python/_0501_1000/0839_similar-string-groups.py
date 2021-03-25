#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 如果我们交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的
# 。 
# 
#  例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 "t
# ars"，"rats"，或 "arts" 相似。 
# 
#  总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同
# 一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。 
# 
#  我们给出了一个不包含重复的字符串列表 A。列表中的每个字符串都是 A 中其它所有字符串的一个字母异位词。请问 A 中有多少个相似字符串组？ 
# 
#  
# 
#  示例： 
# 
#  输入：["tars","rats","arts","star"]
# 输出：2 
# 
#  
# 
#  提示： 
# 
#  
#  A.length <= 2000 
#  A[i].length <= 1000 
#  A.length * A[i].length <= 20000 
#  A 中的所有单词都只包含小写字母。 
#  A 中的所有单词都具有相同的长度，且是彼此的字母异位词。 
#  此问题的判断限制时间已经延长。 
#  
# 
#  
# 
#  备注： 
# 
#  字母异位词[anagram]，一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。 
#  Related Topics 深度优先搜索 并查集 图

"""

import collections
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))

    def find(self, x):
        if self.set[x] != x:
            self.set[x] = self.find(self.set[x])
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root: return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True


class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        """
        官方解答
        """

        def similar(word1, word2):
            diff = 0
            for x, y in zip(word1, word2):
                if x != y:
                    diff += 1
                if diff > 2:
                    return False
            return True

        N, W = len(A), len(A[0])
        uf = UnionFind(N)
        # If few words, then check for pairwise similarity: O(N^2 W)
        if N < W * W:
            for (i1, word1), (i2, word2) in itertools.combinations(enumerate(A), 2):
                if similar(word1, word2):
                    uf.union_set(i1, i2)
        # If short words, check all neighbors: O(N W^3)
        else:
            buckets = collections.defaultdict(set)
            for i, word in enumerate(A):
                char_list = list(word)
                for j0, j1 in itertools.combinations(range(W), 2):
                    char_list[j0], char_list[j1] = char_list[j1], char_list[j0]
                    buckets["".join(char_list)].add(i)
                    char_list[j0], char_list[j1] = char_list[j1], char_list[j0]
            for i1, wd in enumerate(A):
                for i2 in buckets[wd]:
                    uf.union_set(i1, i2)
        return sum(idx == v for idx, v in enumerate(uf.set))


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        f = list(range(n))

        def find(x: int) -> int:
            if f[x] == x:
                return x
            f[x] = find(f[x])
            return f[x]

        def check(a: str, b: str) -> bool:
            num = 0
            for ac, bc in zip(a, b):
                if ac != bc:
                    num += 1
                    if num > 2:
                        return False
            return True

        for i in range(n):
            for j in range(i + 1, n):
                fi, fj = find(i), find(j)
                if fi == fj:
                    continue
                if check(strs[i], strs[j]):
                    f[fi] = fj

        ret = sum(1 for i in range(n) if f[i] == i)
        return ret


@pytest.mark.parametrize("args,expected", [
    (["tars", "rats", "arts", "star"], 2)
])
@pytest.mark.parametrize("SolutionCLS",[Solution,Solution1])
def test_solutions(args, expected, SolutionCLS):
    assert SolutionCLS().numSimilarGroups(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
