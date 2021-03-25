#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10**8。 
# 
#  arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。
#  
# 
#  我们最多能将数组分成多少块？ 
# 
#  示例 1: 
# 
#  
# 输入: arr = [5,4,3,2,1]
# 输出: 1
# 解释:
# 将数组分成2块或者更多块，都无法得到所需的结果。
# 例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。 
#  
# 
#  示例 2: 
# 
#  
# 输入: arr = [2,1,3,4,4]
# 输出: 4
# 解释:
# 我们可以把它分成两块，例如 [2, 1], [3, 4, 4]。
# 然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。 
#  
# 
#  注意: 
# 
#  
#  arr的长度在[1, 2000]之间。 
#  arr[i]的大小在[0, 10**8]之间。 
#  
#  Related Topics 数组

"""

import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        def compare(i1, i2):
            return arr[i1] - arr[i2] if arr[i1] != arr[i2] else i1 - i2

        idxs = list(range(len(arr)))
        sorted_idxs = sorted(idxs, key=functools.cmp_to_key(compare))
        result, max_i = 0, 0
        # print(sorted_idxs)
        for i, v in enumerate(sorted_idxs):
            max_i = max(max_i, v)
            if max_i == i:
                result += 1
        return result


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    """
    GOOD
    单调栈
    https://leetcode-cn.com/problems/max-chunks-to-make-sorted-ii/solution/zui-duo-neng-wan-cheng-pai-xu-de-kuai-ii-deng-jie-/
    """

    def maxChunksToSorted(self, arr: [int]) -> int:
        stack = []
        for num in arr:
            if stack and num < stack[-1]:
                head = stack.pop()
                while stack and num < stack[-1]:
                    stack.pop()
                stack.append(head)
            else:
                stack.append(num)
        # print(stack)
        return len(stack)


@pytest.mark.parametrize("args,expected", [
    # ([5, 4, 3, 2, 1], 1),
    # ([2, 1, 3, 4, 4], 4),
    ([1, 1, 2, 1, 1, 3, 4, 5, 1, 6], 4),
    ([1, 2, 1, 3, 4, 7, 5, 6], 5),
])
def test_solutions(args, expected):
    assert Solution().maxChunksToSorted(args) == expected
    assert Solution1().maxChunksToSorted(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
