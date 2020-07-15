#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-15 14:41:54
# @Last Modified : 2020-07-15 14:41:54
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个正整数和负整数组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。 
# 
#  返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满
# 足条件的子矩阵，返回任意一个均可。 
# 
#  注意：本题相对书上原题稍作改动 
# 
#  示例: 
# 
#  输入:
# [
#   [-1,0],
#   [0,-1]
# ]
# 输出: [0,1,0,1]
# 解释: 输入中标粗的元素即为输出所表示的矩阵 
# 
#  说明： 
# 
#  
#  1 <= matrix.length, matrix[0].length <= 200 
#  
#  Related Topics 动态规划 
#  👍 14 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        """GOOD TODO"""
        R, C = len(matrix), len(matrix[0])
        maxArea = float('-inf')  # 最大面积
        res = [0, 0, 0, 0]

        for left in range(C):  # 从左到右，从上到下，滚动遍历
            colSum = [0] * R  # 以left为左边界，每行的总和
            for right in range(left, C):  # 这一列每一位为右边界
                for i in range(R):  # 遍历列中每一位，计算前缀和
                    colSum[i] += matrix[i][right]

                startX, endX, maxAreaCur = self.getMax(colSum)  # 在left，right为边界下的矩阵中，前缀和colSum的最大值
                if maxAreaCur > maxArea:
                    res = [startX, left, endX, right]  # left是起点y轴坐标，right是终点y轴坐标
                    maxArea = maxAreaCur
        return res

    # 这一列中，找最大值，同时记录起点，终点
    # 因为传进来的是列的前缀和，所以返回的起点、终点代表的是行坐标
    def getMax(self, nums):
        N = len(nums)
        maxVal, curSum = nums[0], nums[0]  # 初始化最大值
        startIndex, end, start = 0, 0, 0  # 初始化临时起点，起点，终点
        for i in range(1, N):
            if curSum < 0:  # 前缀和小于0了，前面就不要了，从当前开始
                curSum = nums[i]
                startIndex = i  # 前面的前缀和小于0了，需要重置起点，从当前开始才有可能成为最大值
            else:
                curSum = curSum + nums[i]

            if curSum > maxVal:
                maxVal = curSum
                start, end = startIndex, i  # 记录下前面的起点，默认0，或者是curSum<0后，重新更新的起点, 终点是当前坐标
        return start, end, maxVal  # 起点，终点，最大前缀和（最大面积）


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (
            [
                [-1, 0],
                [0, -1]
            ], [[0, 1, 0, 1], [1, 0, 1, 0]]

    )
])
def test_solutions(args, expected):
    assert Solution().getMaxMatrix(args) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
