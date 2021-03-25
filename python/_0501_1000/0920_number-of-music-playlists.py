#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 你的音乐播放器里有 N 首不同的歌，在旅途中，你的旅伴想要听 L 首歌（不一定不同，即，允许歌曲重复）。请你为她按如下规则创建一个播放列表： 
# 
#  
#  每首歌至少播放一次。 
#  一首歌只有在其他 K 首歌播放完之后才能再次播放。 
#  
# 
#  返回可以满足要求的播放列表的数量。由于答案可能非常大，请返回它模 10^9 + 7 的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：N = 3, L = 3, K = 1
# 输出：6
# 解释：有 6 种可能的播放列表。[1, 2, 3]，[1, 3, 2]，[2, 1, 3]，[2, 3, 1]，[3, 1, 2]，[3, 2, 1].
#  
# 
#  示例 2： 
# 
#  输入：N = 2, L = 3, K = 0
# 输出：6
# 解释：有 6 种可能的播放列表。[1, 1, 2]，[1, 2, 1]，[2, 1, 1]，[2, 2, 1]，[2, 1, 2]，[1, 2, 2]
#  
# 
#  示例 3： 
# 
#  输入：N = 2, L = 3, K = 1
# 输出：2
# 解释：有 2 种可能的播放列表。[1, 2, 1]，[2, 1, 2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= K < N <= L <= 100 
#  
#  Related Topics 动态规划

"""
import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        """
        令 dp[i][j] 为播放列表长度为 i 包含恰好 j 首不同歌曲的数量
        考虑 dp[i][j]。最后一首歌，我们可以播放没有播放过的歌也可以是播放过的。如果未播放过的，那么就是 dp[i-1][j-1] * (N-j) 种选择方法。如果不是，那么就是选择之前的一首歌，dp[i-1][j] * max(j-K, 0)（j 首歌，最近的 K 首不可以播放）。

        """
        @functools.lru_cache(None)
        def dp(i, j):
            if i == 0:
                return +(j == 0)
            ans = dp(i - 1, j - 1) * (N - j + 1)
            ans += dp(i - 1, j) * max(j - K, 0)
            return ans % (10 ** 9 + 7)

        return dp(L, N)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        N=3, L=3, K=1
    ), 6),
    pytest.param(dict(N=2, L=3, K=0), 6),
    pytest.param(dict(N=2, L=3, K=1), 2),
])
def test_solutions(kwargs, expected):
    assert Solution().numMusicPlaylists(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
