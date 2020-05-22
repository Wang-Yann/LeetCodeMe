#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个非负整数数组 A，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为正方形数组。 
# 
#  返回 A 的正方形排列的数目。两个排列 A1 和 A2 不同的充要条件是存在某个索引 i，使得 A1[i] != A2[i]。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,17,8]
# 输出：2
# 解释：
# [1,8,17] 和 [17,8,1] 都是有效的排列。
#  
# 
#  示例 2： 
# 
#  输入：[2,2,2]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 12 
#  0 <= A[i] <= 1e9 
#  
#  Related Topics 图 数学 回溯算法

"""
import collections
import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numSquarefulPerms(self, A: List[int]) -> int:
        """
        构造一张图，包含所有的边 ii 到 jj ，如果满足 A[i] + A[j]A[i]+A[j] 是一个完全平方数。
        我们的目标就是求这张图的所有哈密顿路径，即经过图中所有点仅一次的路径
        我们使用 count 记录对于每一种值还有多少个节点等待被访问，与一个变量 todo 记录还剩多少个节点等待被访问

        """
        N = len(A)
        counter = collections.Counter(A)
        graph = {x:[] for x in counter}
        for x in counter:
            for y in counter:
                if math.sqrt(x + y).is_integer():
                    graph[x].append(y)

        def dfs(x, todo):
            counter[x] -= 1
            if todo == 0:
                ans = 1
            else:
                ans = 0
                for v in graph[x]:
                    if counter[v]:
                        ans += dfs(v, todo - 1)
            counter[x] += 1
            return ans

        res = 0
        for x in counter:
            res += dfs(x, N - 1)
        return res


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):

    def numSquarefulPerms(self, A):
        """
        """
        nums = A
        nums.sort()
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                # 去重
                if i and nums[i]==nums[i-1]:
                    continue
                # 剪枝
                if not tmp or math.sqrt(tmp[-1]+nums[i]).is_integer():
                    backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return len(res)


@pytest.mark.parametrize("args,expected", [
    ([1, 17, 8], 2),
    pytest.param([2, 2, 2], 1),
])
def test_solutions(args, expected):
    assert Solution().numSquarefulPerms(args) == expected
    assert Solution1().numSquarefulPerms(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
