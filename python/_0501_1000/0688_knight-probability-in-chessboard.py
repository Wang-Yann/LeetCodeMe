#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 已知一个 NxN 的国际象棋棋盘，棋盘的行号和列号都是从 0 开始。即最左上角的格子记为 (0, 0)，最右下角的记为 (N-1, N-1)。 
# 
#  现有一个 “马”（也译作 “骑士”）位于 (r, c) ，并打算进行 K 次移动。 
# 
#  如下图所示，国际象棋的 “马” 每一步先沿水平或垂直方向移动 2 个格子，然后向与之相垂直的方向再移动 1 个格子，共有 8 个可选的位置。 
# 
#  
# 
#  
# 
#  
# 
#  现在 “马” 每一步都从可选的位置（包括棋盘外部的）中独立随机地选择一个进行移动，直到移动了 K 次或跳到了棋盘外面。 
# 
#  求移动结束后，“马” 仍留在棋盘上的概率。 
# 
#  
# 
#  示例： 
# 
#  输入: 3, 2, 0, 0
# 输出: 0.0625
# 解释: 
# 输入的数据依次为 N, K, r, c
# 第 1 步时，有且只有 2 种走法令 “马” 可以留在棋盘上（跳到（1,2）或（2,1））。对于以上的两种情况，各自在第2步均有且只有2种走法令 “马” 仍
# 然留在棋盘上。
# 所以 “马” 在结束后仍在棋盘上的概率为 0.0625。
#  
# 
#  
# 
#  注意： 
# 
#  
#  N 的取值范围为 [1, 25] 
#  K 的取值范围为 [0, 100] 
#  开始时，“马” 总是位于棋盘上 
#  
#  Related Topics 动态规划

"""
import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    模拟
    """
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1.0
        pre_pos = {(r, c): 1.0}
        cur_pos = {}
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        DNUM = 8
        for _ in range(K):
            cur_pos = collections.defaultdict(int)
            for (x0, y0), p0 in list(pre_pos.items()):
                for i, j in directions:
                    r, c = x0 + i, y0 + j
                    if not (0 <= r <= N - 1 and 0 <= c <= N - 1):
                        continue
                    cur_pos[(r, c)] += p0 / DNUM
            pre_pos = cur_pos
        return sum(cur_pos.values())


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("args,expected", [
    ([3, 2, 0, 0], 0.0625),
    ([1, 0, 0, 0], 1.0)
])
def test_solutions(args, expected):
    assert Solution().knightProbability(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
