#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-19 06:31:11
# @Last Modified : 2021-03-19 06:31:11
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


import heapq
# 一所学校里有一些班级，每个班级里有一些学生，现在每个班都会进行一场期末考试。给你一个二维数组 classes ，其中 classes[i] = [passi
# , totali] ，表示你提前知道了第 i 个班级总共有 totali 个学生，其中只有 passi 个学生可以通过考试。
#
#  给你一个整数 extraStudents ，表示额外有 extraStudents 个聪明的学生，他们 一定 能通过任何班级的期末考。你需要给这 extr
# aStudents 个学生每人都安排一个班级，使得 所有 班级的 平均 通过率 最大 。
#
#  一个班级的 通过率 等于这个班级通过考试的学生人数除以这个班级的总人数。平均通过率 是所有班级的通过率之和除以班级数目。
#
#  请你返回在安排这 extraStudents 个学生去对应班级后的 最大 平均通过率。与标准答案误差范围在 10-5 以内的结果都会视为正确结果。
#
#
#
#  示例 1：
#
#
# 输入：classes = [[1,2],[3,5],[2,2]], extraStudents = 2
# 输出：0.78333
# 解释：你可以将额外的两个学生都安排到第一个班级，平均通过率为 (3/4 + 3/5 + 2/2) / 3 = 0.78333 。
#
#
#  示例 2：
#
#
# 输入：classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
# 输出：0.53485
#
#
#
#
#  提示：
#
#
#  1 <= classes.length <= 105
#  classes[i].length == 2
#  1 <= passi <= totali <= 105
#  1 <= extraStudents <= 105
#
#  Related Topics 堆
#  👍 26 👎 0
import statistics
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """AC"""
        def delta(ca, cb):
            return (ca / cb) - ((ca + 1) / (cb + 1))

        heap = [(delta(ca, cb), ca, cb) for ca, cb in classes]
        heapq.heapify(heap)
        for i in range(extraStudents):
            _, ca, cb = heapq.heappop(heap)
            heapq.heappush(heap, (delta(ca + 1, cb + 1), ca + 1, cb + 1))
        return statistics.mean(x[1] / x[2] for x in heap)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2), 0.78333],
    [dict(classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4), 0.53485],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().maxAverageRatio(**kw) == pytest.approx(expected, rel=1e-5)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
