#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 18:49:04
# @Last Modified : 2020-04-26 18:49:04
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List


class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for val in asteroids:
            stack.append(val)
            while len(stack) >= 2 and stack[-1] < 0 < stack[-2]:
                last = stack.pop()
                second_last = stack.pop()
                if abs(last) < abs(second_last):
                    stack.append(second_last)
                elif abs(last) > abs(second_last):
                    stack.append(last)
        return stack


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [5, 10, -5],
        [8, -8],
        [10, 2, -5],
        [-2, -1, 1, 2]

    ]
    lists = [x for x in samples]
    res = [sol.asteroidCollision(x) for x in lists]
    print(res)
