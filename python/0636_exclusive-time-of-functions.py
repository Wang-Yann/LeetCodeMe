#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 18:02:58
# @Last Modified : 2020-04-26 18:02:58
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        在遇到一条包含 start 的日志时，我们将对应的函数 id 入栈；
        在遇到一条包含 end 的日志时，我们将对应的函数 id 出栈
        https://leetcode-cn.com/problems/exclusive-time-of-functions/solution/han-shu-de-du-zhan-shi-jian-by-leetcode/
        """
        result = [0] * n
        stack, prev = [], 0
        for log in logs:
            function_id, start_or_end, timestamp = log.split(":")
            if start_or_end == "start":
                if stack:
                    result[stack[-1]] += int(timestamp) - prev
                stack.append(int(function_id))
                prev = int(timestamp)
            else:
                result[stack.pop()] += int(timestamp) - prev + 1
                prev = int(timestamp) + 1
        return result


if __name__ == '__main__':
    sol = Solution()
    samples = [
        dict(n=2, logs=["0:start:0",
                        "1:start:2",
                        "1:end:5",
                        "0:end:6"])

    ]
    lists = [x for x in samples]
    res = [sol.exclusiveTime(**x) for x in lists]
    print(res)
