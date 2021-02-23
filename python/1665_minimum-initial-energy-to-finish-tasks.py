#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 02:04:07
# @Last Modified : 2021-02-23 02:04:07
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个任务数组 tasks ，其中 tasks[i] = [actuali, minimumi] ： 
# 
#  
#  actuali 是完成第 i 个任务 需要耗费 的实际能量。 
#  minimumi 是开始第 i 个任务前需要达到的最低能量。 
#  
# 
#  比方说，如果任务为 [10, 12] 且你当前的能量为 11 ，那么你不能开始这个任务。如果你当前的能量为 13 ，你可以完成这个任务，且完成它后剩余能量
# 为 3 。 
# 
#  你可以按照 任意顺序 完成任务。 
# 
#  请你返回完成所有任务的 最少 初始能量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：tasks = [[1,2],[2,4],[4,8]]
# 输出：8
# 解释：
# 一开始有 8 能量，我们按照如下顺序完成任务：
#     - 完成第 3 个任务，剩余能量为 8 - 4 = 4 。
#     - 完成第 2 个任务，剩余能量为 4 - 2 = 2 。
#     - 完成第 1 个任务，剩余能量为 2 - 1 = 1 。
# 注意到尽管我们有能量剩余，但是如果一开始只有 7 能量是不能完成所有任务的，因为我们无法开始第 3 个任务。 
# 
#  示例 2： 
# 
#  输入：tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
# 输出：32
# 解释：
# 一开始有 32 能量，我们按照如下顺序完成任务：
#     - 完成第 1 个任务，剩余能量为 32 - 1 = 31 。
#     - 完成第 2 个任务，剩余能量为 31 - 2 = 29 。
#     - 完成第 3 个任务，剩余能量为 29 - 10 = 19 。
#     - 完成第 4 个任务，剩余能量为 19 - 10 = 9 。
#     - 完成第 5 个任务，剩余能量为 9 - 8 = 1 。 
# 
#  示例 3： 
# 
#  输入：tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
# 输出：27
# 解释：
# 一开始有 27 能量，我们按照如下顺序完成任务：
#     - 完成第 5 个任务，剩余能量为 27 - 5 = 22 。
#     - 完成第 2 个任务，剩余能量为 22 - 2 = 20 。
#     - 完成第 3 个任务，剩余能量为 20 - 3 = 17 。
#     - 完成第 1 个任务，剩余能量为 17 - 1 = 16 。
#     - 完成第 4 个任务，剩余能量为 16 - 4 = 12 。
#     - 完成第 6 个任务，剩余能量为 12 - 6 = 6 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= tasks.length <= 105 
#  1 <= actuali <= minimumi <= 104 
#  
#  Related Topics 贪心算法 
#  👍 25 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1])
        p = sum_a = 0
        for ai, mi in tasks:
            p = max(p, sum_a + mi)
            sum_a += ai
        return p


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(tasks=[[1, 2], [2, 4], [4, 8]]), 8],
    [dict(tasks=[[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]), 32],
    [dict(tasks=[[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]), 27],
])
def test_solutions(kw, expected):
    assert Solution().minimumEffort(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
