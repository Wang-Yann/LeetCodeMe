#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在无限长的数轴（即 x 轴）上，我们根据给定的顺序放置对应的正方形方块。 
# 
#  第 i 个掉落的方块（positions[i] = (left, side_length)）是正方形，其中 left 表示该方块最左边的点位置(posit
# ions[i][0])，side_length 表示该方块的边长(positions[i][1])。 
# 
#  每个方块的底部边缘平行于数轴（即 x 轴），并且从一个比目前所有的落地方块更高的高度掉落而下。在上一个方块结束掉落，并保持静止后，才开始掉落新方块。 
# 
#  方块的底边具有非常大的粘性，并将保持固定在它们所接触的任何长度表面上（无论是数轴还是其他方块）。邻接掉落的边不会过早地粘合在一起，因为只有底边才具有粘性。
#  
# 
#  
# 
#  返回一个堆叠高度列表 ans 。每一个堆叠高度 ans[i] 表示在通过 positions[0], positions[1], ..., positio
# ns[i] 表示的方块掉落结束后，目前所有已经落稳的方块堆叠的最高高度。 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  输入: [[1, 2], [2, 3], [6, 1]]
# 输出: [2, 5, 5]
# 解释:
# 
# 第一个方块 positions[0] = [1, 2] 掉落：
# _aa
# _aa
# -------
# 方块最大高度为 2 。
# 
# 第二个方块 positions[1] = [2, 3] 掉落：
# __aaa
# __aaa
# __aaa
# _aa__
# _aa__
# --------------
# 方块最大高度为5。
# 大的方块保持在较小的方块的顶部，不论它的重心在哪里，因为方块的底部边缘有非常大的粘性。
# 
# 第三个方块 positions[1] = [6, 1] 掉落：
# __aaa
# __aaa
# __aaa
# _aa
# _aa___a
# -------------- 
# 方块最大高度为5。
# 
# 因此，我们返回结果[2, 5, 5]。
#  
# 
#  
# 
#  示例 2: 
# 
#  输入: [[100, 100], [200, 100]]
# 输出: [100, 100]
# 解释: 相邻的方块不会过早地卡住，只有它们的底部边缘才能粘在表面上。
#  
# 
#  
# 
#  注意: 
# 
#  
#  1 <= positions.length <= 1000. 
#  1 <= positions[i][0] <= 10^8. 
#  1 <= positions[i][1] <= 10^6. 
#  
# 
#  
#  Related Topics 线段树 Ordered Map

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        """
        Simple 模拟方块掉落
        思考“一个方块影响哪些位置的高度？”
        """
        length = len(positions)
        qans = [0] * length
        for i, (left, size) in enumerate(positions):
            right = left + size
            qans[i] += size
            for j in range(i + 1, length):
                left2, size2 = positions[j]
                right2 = left2 + size2
                # intersect
                if left2 < right and left < right2:
                    qans[j] = max(qans[j], qans[i])
        # print(qans)
        ans = []
        # 返回目前所有已经落稳的方块堆叠的最高高度
        for x in qans:
            ans.append(max(ans[-1], x) if ans else x)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SegmentTree(object):
    """线段树的数组实现"""
    def __init__(self, N, update_fn, query_fn):
        self.N = N
        self.H = 1
        while (1 << self.H) < N:
            self.H += 1

        self.update_fn = update_fn
        self.query_fn = query_fn
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N

    def _apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def _pull(self, x):
        while x > 1:
            x //= 2
            self.tree[x] = self.query_fn(self.tree[x * 2], self.tree[x * 2 + 1])
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

    def _push(self, x):
        for h in range(self.H, 0, -1):
            y = x >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2 + 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, L, R, h):
        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1:
                self._apply(L, h)
                L += 1
            if R & 1 == 0:
                self._apply(R, h)
                R -= 1
            L //= 2
            R //= 2
        self._pull(L0)
        self._pull(R0)

    def query(self, L, R):
        L += self.N
        R += self.N
        self._push(L)
        self._push(R)
        ans = 0
        while L <= R:
            if L & 1:
                ans = self.query_fn(ans, self.tree[L])
                L += 1
            if R & 1 == 0:
                ans = self.query_fn(ans, self.tree[R])
                R -= 1
            L //= 2
            R //= 2
        return ans


class Solution1(object):
    """
    # 官方　懒惰传播的线段树

    """

    def fallingSquares(self, positions):
        # Coordinate compression
        coords = set()
        for left, size in positions:
            coords.add(left)
            coords.add(left + size - 1)
        index = {x: i for i, x in enumerate(sorted(coords))}

        tree = SegmentTree(len(index), max, max)
        best = 0
        ans = []
        for left, size in positions:
            L, R = index[left], index[left + size - 1]
            h = tree.query(L, R) + size
            tree.update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans


@pytest.mark.parametrize("args,expected", [
    ([[1, 2], [2, 3], [6, 1]], [2, 5, 5]),
    ([[100, 100], [200, 100]], [100, 100]),
])
def test_solutions(args, expected):
    assert Solution().fallingSquares(args) == expected
    assert Solution1().fallingSquares(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
