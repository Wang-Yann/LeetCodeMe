#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-26 21:50:21
# @Last Modified : 2021-02-26 21:50:21
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数 n ，请你找到满足下面条件的一个序列： 
# 
#  
#  整数 1 在序列中只出现一次。 
#  2 到 n 之间每个整数都恰好出现两次。 
#  对于每个 2 到 n 之间的整数 i ，两个 i 之间出现的距离恰好为 i 。 
#  
# 
#  序列里面两个数 a[i] 和 a[j] 之间的 距离 ，我们定义为它们下标绝对值之差 |j - i| 。 
# 
#  请你返回满足上述条件中 字典序最大 的序列。题目保证在给定限制条件下，一定存在解。 
# 
#  一个序列 a 被认为比序列 b （两者长度相同）字典序更大的条件是： a 和 b 中第一个不一样的数字处，a 序列的数字比 b 序列的数字大。比方说，[0
# ,1,9,0] 比 [0,1,5,6] 字典序更大，因为第一个不同的位置是第三个数字，且 9 比 5 大。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 3
# 输出：[3,1,2,3,2]
# 解释：[2,3,2,1,3] 也是一个可行的序列，但是 [3,1,2,3,2] 是字典序最大的序列。
#  
# 
#  示例 2： 
# 
#  输入：n = 5
# 输出：[5,3,1,4,3,5,2,4,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  
#  Related Topics 递归 回溯算法 
#  👍 16 👎 0
  

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def constructDistancedSequence(self, n: int) -> List[int]:
        """
        !!
        https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/discuss/1008948/Python-Greedy%2BBacktracking-or-Well-Explained-or-Comments
        """
        arr = [0] * (2 * n - 1)  # the array we want to put numbers. 0 means no number has been put here
        i = 0  # current index to put a number
        used = [False] * (n + 1)  # check if we have used that number

        # backtracking
        def dfs(arr, i, vi):
            # if we already fill the array successfully, return True
            if i >= (2 * n - 1):
                return True

            # try each number from n to 1
            for x in range(n, 0, -1):
                # two cases:
                # x > 1, we check two places. Mind index out of bound here.
                # x = 1, we only check one place
                # arr[i] == 0 means index i is not occupied
                if (x > 1
                    and ((
                                 not (arr[i] == 0 and (i + x < 2 * n - 1) and arr[i + x] == 0))
                         or vi[x]
                    )
                ) or (
                        x == 1 and (arr[i] != 0 or vi[x])
                ):
                    continue

                # if it can be placed, then place it
                if x > 1:
                    arr[i] = x
                    arr[i + x] = x
                else:
                    arr[i] = x
                vi[x] = True

                # find the next available place
                next_i = i + 1
                while next_i < 2 * n - 1 and arr[next_i]:
                    next_i += 1

                # place the next one
                if dfs(arr, next_i, vi):
                    # if it success, it is already the lexicographically largest one, we don't search anymore
                    return True

                # backtracking... restore the state
                if x > 1:
                    arr[i] = 0
                    arr[i + x] = 0
                else:
                    arr[i] = 0
                vi[x] = False

            # we could not find a solution, return False
            return False

        dfs(arr, i, used)
        return arr


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=3), [3, 1, 2, 3, 2]],
    [dict(n=5), [5, 3, 1, 4, 3, 5, 2, 4, 2]],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().constructDistancedSequence(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
