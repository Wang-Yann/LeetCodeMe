#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，
# 我们就称这个数组为一个优美的排列。条件： 
# 
#  
#  第 i 位的数字能被 i 整除 
#  i 能被第 i 位上的数字整除 
#  
# 
#  现在给定一个整数 N，请问可以构造多少个优美的排列？ 
# 
#  示例1: 
# 
#  
# 输入: 2
# 输出: 2
# 解释: 
# 
# 第 1 个优美的排列是 [1, 2]:
#   第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
#   第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除
# 
# 第 2 个优美的排列是 [2, 1]:
#   第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
#   第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
#  
# 
#  说明: 
# 
#  
#  N 是一个正整数，并且不会超过15。 
#  
#  Related Topics 回溯算法

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def countArrangement(self, N: int) -> int:
        def backtrack(pos, arr):
            if pos <= 0:
                return 1
            count = 0
            for i in range(pos):
                if arr[i] % pos == 0 or pos % arr[i] == 0:
                    arr[i], arr[pos - 1] = arr[pos - 1], arr[i]
                    count += backtrack(pos - 1, arr)
                    arr[i], arr[pos - 1] = arr[pos - 1], arr[i]
            return count

        return backtrack(N, list(range(1, N + 1)))


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        def dfs(pos, unused):
            if len(unused) == 0:
                return 1
            ret = 0
            for num in list(unused):
                if pos % num == 0 or num % pos == 0:
                    unused -= {num}
                    ret += dfs(pos + 1, unused)
                    unused |= {num}
            return ret

        return dfs(1, set([i for i in range(1, N + 1)]))
@pytest.mark.parametrize("args,expected", [
    (2, 2),
])
def test_solutions(args, expected):
    assert Solution().countArrangement(args) == expected
    assert Solution1().countArrangement(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
