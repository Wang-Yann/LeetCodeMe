#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-22 09:18:46
# @Last Modified : 2021-02-22 09:18:46
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有 n 座城市，编号从 1 到 n 。编号为 x 和 y 的两座城市直接连通的前提是： x 和 y 的公因数中，至少有一个 严格大于 某个阈值 thresh
# old 。更正式地说，如果存在整数 z ，且满足以下所有条件，则编号 x 和 y 的城市之间有一条道路： 
# 
#  
#  x % z == 0 
#  y % z == 0 
#  z > threshold 
#  
# 
#  给你两个整数 n 和 threshold ，以及一个待查询数组，请你判断每个查询 queries[i] = [ai, bi] 指向的城市 ai 和 bi 
# 是否连通（即，它们之间是否存在一条路径）。 
# 
#  返回数组 answer ，其中answer.length == queries.length 。如果第 i 个查询中指向的城市 ai 和 bi 连通，则 
# answer[i] 为 true ；如果不连通，则 answer[i] 为 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 
#  
# 输入：n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]
# 输出：[false,false,true]
# 解释：每个数的因数如下：
# 1:   1
# 2:   1, 2
# 3:   1, 3
# 4:   1, 2, 4
# 5:   1, 5
# 6:   1, 2, 3, 6
# 所有大于阈值的的因数已经加粗标识，只有城市 3 和 6 共享公约数 3 ，因此结果是： 
# [1,4]   1 与 4 不连通
# [2,5]   2 与 5 不连通
# [3,6]   3 与 6 连通，存在路径 3--6
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 
#  
# 输入：n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]
# 输出：[true,true,true,true,true]
# 解释：每个数的因数与上一个例子相同。但是，由于阈值为 0 ，所有的因数都大于阈值。因为所有的数字共享公因数 1 ，所以所有的城市都互相连通。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 
#  
# 输入：n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]
# 输出：[false,false,false,false,false]
# 解释：只有城市 2 和 4 共享的公约数 2 严格大于阈值 1 ，所以只有这两座城市是连通的。
# 注意，同一对节点 [x, y] 可以有多个查询，并且查询 [x，y] 等同于查询 [y，x] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 104 
#  0 <= threshold <= n 
#  1 <= queries.length <= 105 
#  queries[i].length == 2 
#  1 <= ai, bi <= cities 
#  ai != bi 
#  
#  Related Topics 并查集 数学 
#  👍 27 👎 0

"""

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
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n + 1)
        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):  # step by i
                if i > threshold:
                    uf.union_set(i, j)
        ans = []
        for q in queries:
            pa = uf.find_set(q[0])
            pb = uf.find_set(q[1])
            ans.append(pa == pb)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=6, threshold=2, queries=[[1, 4], [2, 5], [3, 6]]), [False, False, True]],
    [dict(n=6, threshold=0, queries=[[4, 5], [3, 4], [3, 2], [2, 6], [1, 3]]), [True, True, True, True, True]],
    [dict(n=5, threshold=1, queries=[[4, 5], [4, 5], [3, 2], [2, 3], [3, 4]]), [False, False, False, False, False]],
])
def test_solutions(kw, expected):
    assert Solution().areConnected(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
