#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。 
# 
#  示例 1: 
# 
#  输入: [4, 1, 8, 7]
# 输出: True
# 解释: (8-4) * (7-1) = 24
#  
# 
#  示例 2: 
# 
#  输入: [1, 2, 1, 2]
# 输出: False
#  
# 
#  注意: 
# 
#  
#  除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。 
#  每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允
# 许的。 
#  你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。 
#  
#  Related Topics 深度优先搜索

"""
import operator
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def judgePoint24(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 0:
            return False
        elif N == 1:
            return abs(nums[0] - 24) < 1e-6
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                next_nums = [nums[k] for k in range(N) if i != k != j]
                for op in [operator.add, operator.sub, operator.mul, operator.truediv]:
                    if ((op is operator.add or op is operator.mul) and j > i) \
                        or (op == operator.truediv and nums[j] == 0):
                        continue
                    next_nums.append(op(nums[i], nums[j]))
                    if self.judgePoint24(next_nums):
                        return True
                    next_nums.pop()
        return False


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def judgePoint24(self, nums):
        TARGET = 24
        EPSILON = 1e-6
        ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3

        def solve(nums_lst):
            if not nums_lst:
                return False
            if len(nums_lst) == 1:
                return abs(nums_lst[0] - TARGET) < EPSILON
            for i, x in enumerate(nums_lst):
                for j, y in enumerate(nums_lst):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums_lst):
                            if k != i and k != j:
                                newNums.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                continue
                            if k == ADD:
                                newNums.append(x + y)
                            elif k == MULTIPLY:
                                newNums.append(x * y)
                            elif k == SUBTRACT:
                                newNums.append(x - y)
                            elif k == DIVIDE:
                                if abs(y) < EPSILON:
                                    continue
                                newNums.append(x / y)
                            if solve(newNums):
                                return True
                            newNums.pop()
            return False

        return solve(nums)


class Solution2:

    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False

        def helper(arr):
            if len(arr) == 1:
                return abs(arr[0] - 24) < 1e-6
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    new_nums = [arr[k] for k in range(len(arr)) if i != k != j]
                    if helper(new_nums + [arr[i] + arr[j]]):
                        return True
                    if helper(new_nums + [arr[i] * arr[j]]):
                        return True
                    if helper(new_nums + [arr[i] - arr[j]]):
                        return True
                    if helper(new_nums + [arr[j] - arr[i]]):
                        return True
                    if arr[j] != 0 and helper(new_nums + [arr[i] / arr[j]]):
                        return True
                    if arr[i] != 0 and helper(new_nums + [arr[j] / arr[i]]):
                        return True
            return False

        return helper(nums)


@pytest.mark.parametrize("args,expected", [
    ([4, 1, 8, 7], True),
    pytest.param([1, 2, 1, 2], False),
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1, Solution2])
def test_solutions(args, expected, SolutionCLS):
    assert SolutionCLS().judgePoint24(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
