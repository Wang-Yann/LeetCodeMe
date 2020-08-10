#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-27 17:25:31
# @Last Modified : 2020-04-27 17:25:31
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务
# 都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
#
#  然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
#
#  你需要计算完成所有任务所需要的最短时间。
#
#
#
#  示例 ：
#
#  输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
#      在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。
#
#
#
#  提示：
#
#
#  任务的总个数为 [1, 10000]。
#  n 的取值范围为 [0, 100]。
#
#  Related Topics 贪心算法 队列 数组
#  👍 316 👎 0

import collections
from queue import PriorityQueue
from typing import List

import pytest


class Solution0:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        完成所有任务的最短时间取决于出现次数最多的任务数量。
        https://leetcode-cn.com/problems/task-scheduler/solution/python-xiang-jie-by-jalan/
        步骤:
            计算每个任务出现的次数
            找出出现次数最多的任务，假设出现次数为 x
            计算至少需要的时间 (x - 1) * (n + 1)，记为 min_time
            计算出现次数为 x 的任务总数 count，计算最终结果为 min_time + count


        """
        counter = collections.Counter(tasks)
        _, max_count = counter.most_common(1)[0]
        # 这个时间是除去执行最后一次调度的所需最少时间
        result = (max_count - 1) * (n + 1)
        # print(counter, max_count, result)
        for count in counter.values():
            if count == max_count:
                result += 1
        # 如果结果比任务数量少，则返回总任务数
        return max(result, len(tasks))


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # from queue import PriorityQueue
        counter = collections.Counter(tasks)
        q = PriorityQueue()
        # 优先　小值
        for k, v in counter.items():
            q.put((-v, v))
        time = 0
        while not q.empty():
            i = 0
            tmp = []
            while i <= n:
                if not q.empty():
                    _, cnt = q.get()
                    if cnt > 1:
                        tmp.append(cnt - 1)
                time += 1
                if q.empty() and not tmp:
                    break
                i += 1
            for v in tmp:
                q.put((-v, v))
        return time


@pytest.mark.parametrize("kw,expected", [
    [dict(tasks=["A", "A", "A", "B", "B", "B"], n=2), 8],
    [dict(tasks=["A", "A", "A", "B", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F"], n=2), 14],
])
def test_solutions(kw, expected):
    assert Solution().leastInterval(**kw) == expected
    assert Solution0().leastInterval(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
