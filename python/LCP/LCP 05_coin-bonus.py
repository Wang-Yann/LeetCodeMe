#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-15 23:52:10
# @Last Modified : 2020-07-15 23:52:10
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 力扣决定给一个刷题团队发LeetCoin作为奖励。同时，为了监控给大家发了多少LeetCoin，力扣有时候也会进行查询。 
# 
#  
# 
#  该刷题团队的管理模式可以用一棵树表示： 
# 
#  
#  团队只有一个负责人，编号为1。除了该负责人外，每个人有且仅有一个领导（负责人没有领导）； 
#  不存在循环管理的情况，如A管理B，B管理C，C管理A。 
#  
# 
#  
# 
#  力扣想进行的操作有以下三种： 
# 
#  
#  给团队的一个成员（也可以是负责人）发一定数量的LeetCoin； 
#  给团队的一个成员（也可以是负责人），以及他/她管理的所有人（即他/她的下属、他/她下属的下属，……），发一定数量的LeetCoin； 
#  查询某一个成员（也可以是负责人），以及他/她管理的所有人被发到的LeetCoin之和。 
#  
# 
#  
# 
#  输入： 
# 
#  
#  N表示团队成员的个数（编号为1～N，负责人为1）； 
#  leadership是大小为(N - 1) * 2的二维数组，其中每个元素[a, b]代表b是a的下属； 
#  operations是一个长度为Q的二维数组，代表以时间排序的操作，格式如下：
#  
#  operations[i][0] = 1: 代表第一种操作，operations[i][1]代表成员的编号，operations[i][2]代表LeetC
# oin的数量； 
#  operations[i][0] = 2: 代表第二种操作，operations[i][1]代表成员的编号，operations[i][2]代表LeetC
# oin的数量； 
#  operations[i][0] = 3: 代表第三种操作，operations[i][1]代表成员的编号； 
#  
#  
#  
# 
#  输出： 
# 
#  返回一个数组，数组里是每次查询的返回值（发LeetCoin的操作不需要任何返回值）。由于发的LeetCoin很多，请把每次查询的结果模1e9+7 (100
# 0000007)。 
# 
#  
# 
#  示例 1： 
# 
#  输入：N = 6, leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]], operations =
#  [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]
# 输出：[650, 665]
# 解释：团队的管理关系见下图。
# 第一次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 0;
# 第二次查询时，每个成员得到的LeetCoin的数量分别为（按编号顺序）：500, 50, 50, 0, 50, 15.
#  
# 
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= N <= 50000 
#  1 <= Q <= 50000 
#  operations[i][0] != 3 时，1 <= operations[i][2] <= 5000 
#  
#  👍 34 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    """
    https://leetcode-cn.com/problems/coin-bonus/solution/gen-ju-guan-xi-gou-zao-xian-duan-shu-qu-jian-geng-/
    线段树
    """

    def __init__(self):
        self.LEN = 50005
        self.G = [[] for _ in range(self.LEN)]
        self.cnt = 1
        self.L, self.R = [0 for _ in range(self.LEN)], [0 for _ in range(self.LEN)]
        self.sum = [0 for _ in range(self.LEN * 4)]
        self.add = [0 for _ in range(self.LEN * 4)]
        self.MOD = 10 ** 9 + 7

    def dfs(self, u):
        self.cnt += 1
        self.L[u] = self.cnt
        for v in self.G[u]:
            self.dfs(v)
        self.R[u] = self.cnt

    def mod(self, num):
        return num % self.MOD

    def push_up(self, rt: int):
        self.sum[rt] = self.sum[rt * 2] + self.sum[rt * 2 + 1]
        self.sum[rt] = self.mod(self.sum[rt])

    def push_down(self, rt: int, m: int):
        if self.add[rt] != 0:
            self.add[rt << 1] += self.add[rt]
            self.add[rt << 1] = self.mod(self.add[rt << 1])

            self.add[rt << 1 | 1] += self.add[rt]
            self.add[rt << 1 | 1] = self.mod(self.add[rt << 1 | 1])

            self.sum[rt << 1] += self.add[rt] * (m - (m >> 1))
            self.sum[rt << 1] = self.mod(self.sum[rt << 1])

            self.sum[rt << 1 | 1] += self.add[rt] * (m >> 1)
            self.sum[rt << 1 | 1] = self.mod(self.sum[rt << 1 | 1])
            self.add[rt] = 0

    def update_single(self, p: int, val: int, l: int, r: int, rt):
        if l == r:
            self.sum[rt] += val
            self.sum[rt] = self.mod(self.sum[rt])
            return
        self.push_down(rt, r - l + 1)
        m = (l + r) >> 1
        if p <= m:
            self.update_single(p, val, l, m, rt << 1)
        else:
            self.update_single(p, val, m + 1, r, rt << 1 | 1)
        self.push_up(rt)

    def update_range(self, L: int, R: int, c: int, l: int, r: int, rt: int):
        if L <= l <= r <= R:
            self.add[rt] += c
            self.add[rt] = self.mod(self.add[rt])
            self.sum[rt] += c * (r - l + 1)
            self.sum[rt] = self.mod(self.sum[rt])
            return
        self.push_down(rt, r - l + 1)
        m = (l + r) // 2
        if L <= m:
            self.update_range(L, R, c, l, m, rt << 1)
        if m < R:
            self.update_range(L, R, c, m + 1, r, rt << 1 | 1)
        self.push_up(rt)

    def query(self, L: int, R: int, l: int, r: int, rt: int):
        if L <= l <= r <= R:
            return self.sum[rt]
        self.push_down(rt, r - l + 1)
        m, ret = (l + r) // 2, 0
        if L <= m:
            ret += self.query(L, R, l, m, rt << 1)
            ret = self.mod(ret)
        if m < R:
            ret += self.query(L, R, m + 1, r, rt << 1 | 1)
            ret = self.mod(ret)
        return ret

    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        for l in leadership:
            self.G[l[0]].append(l[1])
        self.dfs(1)
        ans = []
        for op in operations:
            if op[0] == 1:
                self.update_single(self.L[op[1]], op[2], 1, self.cnt, 1)
            elif op[0] == 2:
                self.update_range(self.L[op[1]], self.R[op[1]], op[2], 1, self.cnt, 1)
            elif op[0] == 3:
                ans.append(self.query(self.L[op[1]], self.R[op[1]], 1, self.cnt, 1) % self.MOD)
                # print(ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=6, leadership=[[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]], operations=
    [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]), [650, 665]],

])
def test_solutions(kwargs, expected):
    assert Solution().bonus(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
