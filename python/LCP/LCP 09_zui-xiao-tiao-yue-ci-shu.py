#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-16 10:07:05
# @Last Modified : 2020-07-16 10:07:05
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 为了给刷题的同学一些奖励，力扣团队引入了一个弹簧游戏机。游戏机由 N 个特殊弹簧排成一排，编号为 0 到 N-1。初始有一个小球在编号 0 的弹簧处。若小球
# 在编号为 i 的弹簧处，通过按动弹簧，可以选择把小球向右弹射 jump[i] 的距离，或者向左弹射到任意左侧弹簧的位置。也就是说，在编号为 i 弹簧处按动弹簧，
# 小球可以弹向 0 到 i-1 中任意弹簧或者 i+jump[i] 的弹簧（若 i+jump[i]>=N ，则表示小球弹出了机器）。小球位于编号 0 处的弹簧时不
# 能再向左弹。 
# 
#  为了获得奖励，你需要将小球弹出机器。请求出最少需要按动多少次弹簧，可以将小球从编号 0 弹簧弹出整个机器，即向右越过编号 N-1 的弹簧。 
# 
#  示例 1： 
# 
#  
#  输入：jump = [2, 5, 1, 1, 1, 1] 
# 
#  输出：3 
# 
#  解释：小 Z 最少需要按动 3 次弹簧，小球依次到达的顺序为 0 -> 2 -> 1 -> 6，最终小球弹出了机器。 
#  
# 
#  限制： 
# 
#  
#  1 <= jump.length <= 10^6 
#  1 <= jump[i] <= 10000 
#  
#  👍 32 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def minJump(self, jump):
        """
        记录一个最大的 far 值进行优化，用来表示当前从 [0, far-1] 均已被搜索到。
        """
        N = len(jump)
        visited = [False] * (N + 1)
        queue = [[0, 1]]
        visited[0] = True
        curr, far = 0, 1
        while curr < len(queue):
            idx, step = queue[curr]
            curr += 1
            if idx + jump[idx] >= N:
                return step
            if not visited[idx + jump[idx]]:
                queue.append([idx + jump[idx], step + 1])
                visited[idx + jump[idx]] = True
            for j in range(far, idx):
                if not visited[j]:
                    queue.append([j, step + 1])
                    visited[j] = True
            far = max(far, idx + 1)
        return -1


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def minJump(self, jump: List[int]) -> int:
        """
        某一个位置只需要 w 步可以跳到，那么这个位置之前的步数，最多只需要 w+1 步
        max_dis[w] 表示 w 步可以跳到的最远位置
        dp[i]往左跳到达 i 的最小操作数
        """
        res = N = len(jump)
        dp = [0] + [N] * N
        max_dis = [0] * (N + 1)
        cur_min_num = 0
        for i in range(N):
            if i > max_dis[cur_min_num]:
                cur_min_num += 1
            dp[i] = min(dp[i], cur_min_num + 1)

            jump_tmp = i + jump[i]
            if jump_tmp >= N:
                res = min(res, dp[i] + 1)
            else:
                dp[jump_tmp] = min(dp[jump_tmp], dp[i] + 1)
                max_dis[dp[i] + 1] = max(max_dis[dp[i] + 1], jump_tmp)
        # print(max_dis,dp)
        return res


@pytest.mark.parametrize("kw,expected", [
    [dict(jump=[2, 5, 1, 1, 1, 1]), 3],
])
def test_solutions(kw, expected):
    assert Solution().minJump(**kw) == expected
    assert Solution1().minJump(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
