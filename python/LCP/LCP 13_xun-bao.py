#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-16 20:50:20
# @Last Modified : 2020-07-16 20:50:20
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。 
# 
#  迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），和唯一的宝藏地点（用 'T' 表示）。但是，宝藏被一些隐蔽的机关保护了起
# 来。在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。 
# 
#  要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），每个石堆都有无限个足够触发机关的重石。但是由于石头太重，我们一次只能搬一
# 个石头到指定地点。 
# 
#  迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 '.' 表示）。石堆、机关、起点和终点（无论是否能拿到宝藏）也是
# 可以通行的。 
# 
#  我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果
# 无法拿到宝藏，返回 -1 。 
# 
#  示例 1： 
# 
#  
#  输入： ["S#O", "M..", "M.T"] 
# 
#  输出：16 
# 
#  解释：最优路线为： S->O, cost = 4, 去搬石头 O->第二行的M, cost = 3, M机关触发 第二行的M->O, cost = 3, 
# 我们需要继续回去 O 搬石头。 O->第三行的M, cost = 4, 此时所有机关均触发 第三行的M->T, cost = 2，去T点拿宝藏。 总步数为16。
#  
#  
# 
#  示例 2： 
# 
#  
#  输入： ["S#O", "M.#", "M.T"] 
# 
#  输出：-1 
# 
#  解释：我们无法搬到石头触发机关 
#  
# 
#  示例 3： 
# 
#  
#  输入： ["S#O", "M.T", "M.."] 
# 
#  输出：17 
# 
#  解释：注意终点也是可以通行的。 
#  
# 
#  限制： 
# 
#  
#  1 <= maze.length <= 100 
#  1 <= maze[i].length <= 100 
#  maze[i].length == maze[j].length 
#  S 和 T 有且只有一个 
#  0 <= M的数量 <= 16 
#  0 <= O的数量 <= 40，题目保证当迷宫中存在 M 时，一定存在至少一个 O 。 
#  
#  👍 14 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
import queue


class Solution:

    def minimalSteps(self, maze: List[str]) -> int:
        """
        HARD
        链接：https://leetcode-cn.com/problems/xun-bao/solution/xun-bao-bfs-dp-by-leetcode-solution/
        解答成功: 执行耗时:9568 ms,击败了15.00% 的Python3用户
        由于本题的复杂度较高，使用 Python 等性能较差的语言实现时需要注意效率问题
        """
        n = len(maze)
        m = len(maze[0])
        p = []
        # 记录所有特殊点
        for i in range(n):
            for j in range(m):
                if maze[i][j] in ['S', 'T', 'M', 'O']:
                    p.append((i, j, maze[i][j]))
        dxs = [0, 1, 0, -1]
        dys = [1, 0, -1, 0]

        def bfs(x, y):
            q = queue.Queue()
            q.put((x, y))
            dis = [[10000 for i in range(m)] for j in range(n)]
            dis[x][y] = 0
            while not q.empty():
                x,y = q.get()
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or nx == n or ny < 0 or ny == m:
                        continue
                    if maze[nx][ny] == '#':
                        continue
                    if dis[nx][ny] > dis[x][y] + 1:
                        dis[nx][ny] = dis[x][y] + 1
                        q.put((nx, ny))
            res = []
            for i, j, _ in p:
                res.append(dis[i][j])
            return res

        # 计算特殊点之间的最短距离
        tag = {}
        dis = []
        for idx, (i, j, t) in enumerate(p):
            dis.append(bfs(i, j))
            if not t in tag:
                tag[t] = []
            tag[t].append(idx)
        sidx = tag['S'][0]
        tidx = tag['T'][0]

        # 特殊处理 M 不存在的情况
        if not 'M' in tag:
            ans = dis[sidx][tidx]
            if ans == 10000:
                ans = -1
            return ans

        # 计算 S 到所有 M 点之间的最短距离
        Mnum = len(tag['M'])
        Onum = len(tag['O'])
        dp = [[10000 for i in range(Mnum)] for i in range(1 << Mnum)]
        for i in range(Mnum):
            midx = tag['M'][i]
            s = 1 << i
            for j in range(Onum):
                oidx = tag['O'][j]
                dp[s][i] = min(dp[s][i], dis[sidx][oidx] + dis[oidx][midx])
            # 预处理 M 点之间的最短距离
        Mdis = [[10000 for i in range(Mnum)] for j in range(Mnum)]
        for i in range(Mnum):
            midx1 = tag['M'][i]
            for j in range(Mnum):
                midx2 = tag['M'][j]
                for k in range(Onum):
                    oidx = tag['O'][k]
                    Mdis[i][j] = min(Mdis[i][j], dis[midx1][oidx] + dis[oidx][midx2])

            # 状态压缩DP
        for s in range(1 << Mnum):
            for j in range(Mnum):
                if s & (1 << j) == 0:
                    continue
                for k in range(Mnum):
                    if s & (1 << k) != 0:
                        continue
                    ns = s | (1 << k)
                    dp[ns][k] = min(dp[ns][k], dp[s][j] + Mdis[j][k])

        # 统计结果
        ans = 10000
        fs = (1 << Mnum) - 1
        for j in range(Mnum):
            midx = tag['M'][j]
            ans = min(ans, dp[fs][j] + dis[midx][tidx])
        if ans == 10000:
            ans = -1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("args,expected", [
    (["S#O", "M..", "M.T"], 16),
    pytest.param(["S#O", "M.#", "M.T"], -1),
    pytest.param(["S#O", "M.T", "M.."], 17),
])
def test_solutions(args, expected):
    assert Solution().minimalSteps(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
