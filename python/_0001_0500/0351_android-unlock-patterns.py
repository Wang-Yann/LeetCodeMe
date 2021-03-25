#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 17:53:45
# @Last Modified : 2020-07-27 17:53:45
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们都知道安卓有个手势解锁的界面，是一个 3 x 3 的点所绘制出来的网格。 
# 
#  给你两个整数，分别为 m 和 n，其中 1 ≤ m ≤ n ≤ 9，那么请你统计一下有多少种解锁手势，是至少需要经过 m 个点，但是最多经过不超过 n 个
# 点的。 
# 
#  
# 
#  先来了解下什么是一个有效的安卓解锁手势: 
# 
#  
#  每一个解锁手势必须至少经过 m 个点、最多经过 n 个点。 
#  解锁手势里不能设置经过重复的点。 
#  假如手势中有两个点是顺序经过的，那么这两个点的手势轨迹之间是绝对不能跨过任何未被经过的点。 
#  经过点的顺序不同则表示为不同的解锁手势。 
#  
# 
#  
# 
#  
# 
#  
# 
#  解释: 
# 
#  | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 | 
# 
#  无效手势：4 - 1 - 3 - 6 
# 连接点 1 和点 3 时经过了未被连接过的 2 号点。 
# 
#  无效手势：4 - 1 - 9 - 2 
# 连接点 1 和点 9 时经过了未被连接过的 5 号点。 
# 
#  有效手势：2 - 4 - 1 - 3 - 6 
# 连接点 1 和点 3 是有效的，因为虽然它经过了点 2 ，但是点 2 在该手势中之前已经被连过了。 
# 
#  有效手势：6 - 5 - 4 - 1 - 9 - 2 
# 连接点 1 和点 9 是有效的，因为虽然它经过了按键 5 ，但是点 5 在该手势中之前已经被连过了。 
# 
#  
# 
#  示例: 
# 
#  输入: m = 1，n = 1
# 输出: 9
#  
#  Related Topics 动态规划 回溯算法 
#  👍 45 👎 0

"""
import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        """
        TODO
        链接：https://leetcode-cn.com/problems/android-unlock-patterns/solution/dai-zhuang-tai-de-shen-du-you-xian-by-amchor/
        首先明确一下能够直达的位置：
            水平
            垂直
            对角线
            日子型（例如象棋中的马，数字1可以直接到6，8）
            因此，我们将当前数字不能到到的位置统计出来，如果想要到达，就必须经过某个点
        """
        graph = {
            1: {3: 2, 7: 4, 9: 5},
            2: {8: 5},
            3: {1: 2, 7: 5, 9: 6},
            4: {6: 5},
            5: {},
            6: {4: 5},
            7: {1: 4, 3: 5, 9: 8},
            8: {2: 5},
            9: {1: 5, 3: 6, 7: 8},
        }
        ans = 0

        @functools.lru_cache(None)
        def dfs(status, current, count):
            if count == n:
                return 1
            current_ans = 0 if count < m else 1
            for i in range(1, 10):
                if status & (1 << i) == 0:
                    if i not in graph[current] or ((1 << graph[current][i]) & status):
                        current_ans += dfs(status | (1 << i), i, count + 1)
            return current_ans

        # for cur in range(1, 10):
        # ans += dfs(1 << cur, cur, 1)

        # 由于从1，3，7，9出发的线路是同样的数量，从2，4，6，8也是，
        ans += 4 * dfs(1 << 1, 1, 1)
        ans += 4 * dfs(1 << 2, 2, 1)
        ans += dfs(1 << 5, 5, 1)

        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def numberOfPatterns(self, m: int, n: int) -> int:
        """
        为了计算一个合法手势，算法按照如下步骤进行：

        选择一个当前仍然未被使用的数字 i，这一步通过一个访问数组 used 实现，保存所有可用数字。
        我们需要记录上一个访问的数字 last。算法需要检查是否满足以下任一条件：
            1.从 last 到 i 之间是国际象棋中马的移动，或者 last 和 i 是同一行或列的相邻元素。这种情况下，两个数字之和应当为奇数。
            2.连接 last 和 i 的中间元素 mid 已经被访问过，比方说 last 和 i 选择的是对角线上的两点，那么中间点 mid = 5 应当已经选过。
            3.last 和 i 是对角线上的相邻元素。
        https://leetcode-cn.com/problems/android-unlock-patterns/solution/an-zhuo-xi-tong-shou-shi-jie-suo-by-leetcode/

        """

        def is_valid(idx, last, used):
            if used[idx]:
                return False
            # // first digit of the pattern
            if last == -1:
                return True
            # // knight moves or adjacent cells (in a row or in a column)
            if (idx + last) % 2 == 1:
                return True
            # // indexes are at both end of the diagonals for example 0,0, and 8,8
            mid = (idx + last) // 2
            if mid == 4:
                return used[mid]
            # // adjacent cells on diagonal  - for example 0,0 and 1,0 or 2,0 and //1,1
            if (idx % 3 != last % 3) and (idx // 3 != last // 3):
                return True
            # // all other cells which are not adjacent
            return used[mid]

        def calculate_patterns(last, length, used):
            if length == 0:
                return 1
            sum_val = 0
            for i in range(9):
                if is_valid(i, last, used):
                    used[i] = True
                    sum_val += calculate_patterns(i, length - 1, used)
                    used[i] = False
            return sum_val

        res = 0
        for l in range(m, n + 1):
            res += calculate_patterns(-1, l, [False] * 9)
        return res


@pytest.mark.parametrize("kw,expected", [
    [dict(m=1, n=1), 9],
    [dict(m=3, n=6), 35112],
])
def test_solutions(kw, expected):
    assert Solution().numberOfPatterns(**kw) == expected
    assert Solution1().numberOfPatterns(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
