#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-13 22:27:19
# @Last Modified : 2020-04-13 22:27:19
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


class Solution:
    """
    TODO 单调栈
    https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode/
    """

    def largestRectangleAreaS(self, heights: List[int]) -> int:
        A = heights
        result = 0
        stack = [] #stores increasing height

        i = 0
        while i < len(A) + 1:
            if not stack or (i < len(A) and A[i] > A[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                last_pos = stack.pop()
                if not stack:
                    result = max(result, A[last_pos] * i)
                else:
                    result = max(result, A[last_pos] * (i - stack[-1] - 1))

        return result



    def calculateArea(self, heights: List[int],start:int,end:int) -> int:
        if start>end:return 0
        min_index = start
        for i in range(start,end+1):
            if heights[min_index]>heights[i]:
                min_index = i
        return max(heights[min_index]*(end-start+1),
                   self.calculateArea(heights,start,min_index-1),
                   self.calculateArea(heights,min_index+1,end)
                   )

    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.calculateArea(heights, 0, len(heights)-1)

    def largestRectangleAreaSM(self, heights: List[int]) -> int:
        A = heights
        result = 0
        stack = [-1]

        for i in range(len(A)):
            while stack[-1]!=-1  and A[i] <= A[stack[-1]]:
                last_pos = stack.pop()
                result = max(result, A[last_pos] * (i - stack[-1] - 1))
            stack.append(i)
            # 当我们到达数组的尾部时，我们将栈中剩余元素全部弹出栈
        while stack and stack[-1]!=-1:
            last_pos = stack.pop()
            result = max(result, A[last_pos] * (len(A) - stack[-1] - 1))
        return result




if __name__ == '__main__':
    sol = Solution()
    samples = [
        [2, 1, 5, 6, 2, 3],
        [0],
        [],
        [1]
    ]
    # res = [sol.largestRectangleArea(x) for x in samples]
    # res1 = [sol.largestRectangleAreaS(x) for x in samples]
    # print(res,res1)
    res2 = [sol.largestRectangleAreaSM(x) for x in samples]
    print(res2)
