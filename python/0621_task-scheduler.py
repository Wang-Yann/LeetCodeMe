#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-27 17:25:31
# @Last Modified : 2020-04-27 17:25:31
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import collections
from queue import PriorityQueue
from typing import List


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
        #优先　小值
        for k, v in counter.items():
            q.put((-v,v))
        time = 0
        while not q.empty():
            i = 0
            tmp = []
            while i <= n:
                if not q.empty():
                    _,cnt = q.get()
                    if cnt > 1:
                        tmp.append(cnt-1)
                time += 1
                if q.empty() and not tmp:
                    break
                i += 1
            for v in tmp:
                q.put((-v,v))
        return time


if __name__ == '__main__':
    sol = Solution()
    samples = [
        dict(tasks = ["A","A","A","B","B","B"], n = 2 ) ,
        dict(tasks=["A", "A", "A", "B", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F"], n=2)
    ]
    lists = [x for x in samples]
    res = [sol.leastInterval(**x) for x in lists]
    print(res)
