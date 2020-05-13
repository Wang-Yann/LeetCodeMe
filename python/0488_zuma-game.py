#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 回忆一下祖玛游戏。现在桌上有一串球，颜色有红色(R)，黄色(Y)，蓝色(B)，绿色(G)，还有白色(W)。 现在你手里也有几个球。 
# 
#  每一次，你可以从手里的球选一个，然后把这个球插入到一串球中的某个位置上（包括最左端，最右端）。接着，如果有出现三个或者三个以上颜色相同的球相连的话，就把它
# 们移除掉。重复这一步骤直到桌上所有的球都被移除。 
# 
#  找到插入并可以移除掉桌上所有球所需的最少的球数。如果不能移除桌上所有的球，输出 -1 。 
# 
#  
# 示例:
# 输入: "WRRBBW", "RB" 
# 输出: -1 
# 解释: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW （翻译者标注：手上球已经用完，桌上还剩两个球无法消除，返回
# -1）
# 
# 输入: "WWRRBBWW", "WRBRW" 
# 输出: 2 
# 解释: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
# 
# 输入:"G", "GGGGG" 
# 输出: 2 
# 解释: G -> G[G] -> GG[G] -> empty 
# 
# 输入: "RBYYBBRRB", "YRBGB" 
# 输出: 3 
# 解释: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empt
# y 
#  
# 
#  标注: 
# 
#  
#  你可以假设桌上一开始的球中，不会有三个及三个以上颜色相同且连着的球。 
#  桌上的球不会超过20个，输入的数据中代表这些球的字符串的名字是 "board" 。 
#  你手中的球不会超过5个，输入的数据中代表这些球的字符串的名字是 "hand"。 
#  输入的两个字符串均为非空字符串，且只包含字符 'R','Y','B','G','W'。 
#  
#  Related Topics 深度优先搜索

"""

import collections
import itertools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        """HARD  TODO TODO
        贪心算法+回溯（选择可以消除地方）
        """
        owned_cnt = collections.Counter(hand)

        def dfs(board):
            # print(("DFS:",board))
            if not board:
                return 0
            res = float("inf")
            cur_loc = 0
            for char, item in itertools.groupby(board):
                n = len(list(item))
                need = max(3 - n, 0)  # 为了解决已经有的连接的球，并且球数可能大于3个
                if owned_cnt[char] >= need:
                    owned_cnt[char] -= need
                    res = min(res, need + dfs(board[:cur_loc] + board[cur_loc + n:]))
                    owned_cnt[char] += need
                cur_loc += n
            return res

        ans = dfs(board)
        return -1 if ans == float("inf") else ans


# leetcode submit region end(Prohibit modification and deletion)

# Time:  O((b+h) * h!*(b+h-1)!/(b-1)!)
# Space: O((b+h) * h!*(b+h-1)!/(b-1)!)
# brute force solution
class Solution_TLE_BUT_CORRECT(object):
    def findMinStep(self, board, hand):

        def shrink(s):  # Time: O(n), Space: O(n)
            stack = []
            start = 0
            for i in range(len(s) + 1):
                if i == len(s) or s[i] != s[start]:
                    if stack and stack[-1][0] == s[start]:
                        stack[-1][1] += i - start
                        if stack[-1][1] >= 3:
                            stack.pop()
                    elif s and i - start < 3:
                        stack += [s[start], i - start],
                    start = i
            result = []
            for p in stack:
                result += [p[0]] * p[1]
            return result

        def findMinStepHelper(board, hand, lookup):
            if not board: return 0
            if not hand: return float("inf")
            if tuple(hand) in lookup[tuple(board)]: return lookup[tuple(board)][tuple(hand)]

            result = float("inf")
            for i in range(len(hand)):
                for j in range(len(board) + 1):
                    next_board = shrink(board[0:j] + hand[i:i + 1] + board[j:])
                    next_hand = hand[0:i] + hand[i + 1:]
                    result = min(result, findMinStepHelper(next_board, next_hand, lookup) + 1)
            lookup[tuple(board)][tuple(hand)] = result
            return result

        lookup = collections.defaultdict(dict)
        board, hand = list(board), list(hand)
        result = findMinStepHelper(board, hand, lookup)
        return -1 if result == float("inf") else result


@pytest.mark.parametrize("board,hand,expected", [
    # ("WRRBBW", "RB", -1),
    ("WWRRBBWW", "WRBRW", 2),
    # ("RBYYBBRRB", "YRBGB", 3),
])
def test_solutions(board,hand, expected):
    assert Solution().findMinStep(board,hand) == expected
    assert Solution_TLE_BUT_CORRECT().findMinStep(board,hand) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
