#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 07:40:34
# @Last Modified : 2021-02-23 07:40:34
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。 
# 
#  请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你
# 设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。 
# 
#  返回分配方案中尽可能 最小 的 最大工作时间 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：jobs = [3,2,3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：jobs = [1,2,4,7,8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）
# 最大工作时间是 11 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= jobs.length <= 12 
#  1 <= jobs[i] <= 107 
#  
#  Related Topics 递归 回溯算法 
#  👍 40 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/discuss/1009817/One-branch-cutting-trick-to-solve-three-LeetCode-questions
        """
        workers = [0] * k
        self.res = 0x7fffffff

        def dfs(curr):
            if curr == len(jobs):
                self.res = min(self.res, max(workers))
                return

            seen = set()  # record searched workload of workers
            for i in range(k):
                if workers[i] in seen:
                    continue  # if we have searched the workload of 5, skip it.
                if workers[i] + jobs[curr] >= self.res:
                    continue  # another branch cutting
                seen.add(workers[i])
                workers[i] += jobs[curr]
                dfs(curr + 1)
                workers[i] -= jobs[curr]

        dfs(0)
        return self.res


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        A = sorted(jobs, reverse=True)
        N = len(A)

        def dfs(i):
            if i == N:
                return True  # opt 3
            for j in range(k):
                if cap[j] >= A[i]:
                    cap[j] -= A[i]
                    if dfs(i + 1):
                        return True
                    cap[j] += A[i]
                if cap[j] == x:
                    break  # opt 2
            return False

        # binary search
        left, right = max(A), sum(A)
        while left < right:
            x = (left + right) // 2
            cap = [x] * k
            if dfs(0):
                right = x
            else:
                left = x + 1
        return left


@pytest.mark.parametrize("kw,expected", [
    [dict(jobs=[3, 2, 3], k=3), 3],
    [dict(jobs=[1, 2, 4, 7, 8], k=2), 11],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().minimumTimeRequired(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
