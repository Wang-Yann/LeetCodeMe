#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连
# 接的结果和按升序排序后的原数组相同。 
# 
#  我们最多能将数组分成多少块？ 
# 
#  示例 1: 
# 
#  输入: arr = [4,3,2,1,0]
# 输出: 1
# 解释:
# 将数组分成2块或者更多块，都无法得到所需的结果。
# 例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
#  
# 
#  示例 2: 
# 
#  输入: arr = [1,0,2,3,4]
# 输出: 4
# 解释:
# 我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
# 然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
#  
# 
#  注意: 
# 
#  
#  arr 的长度在 [1, 10] 之间。 
#  arr[i]是 [0, 1, ..., arr.length - 1]的一种排列。 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        注意审题
        arr[i]是 [0, 1, ..., arr.length - 1]的一种排列

        如果前 k 个元素为 [0, 1, ..., k-1]，可以直接把他们分为一个块。当我们需要检查 [0, 1, ..., n-1]
        中前 k+1 个元素是不是 [0, 1, ..., k] 的时候，只需要检查其中最大的数是不是 k 就可以了。

        """
        ans, max_v = 0, 0
        for i, v in enumerate(arr):
            max_v = max(max_v, v)
            if max_v == i:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([4, 3, 2, 1, 0], 1),
    ([1, 0, 2, 3, 4], 4),
])
def test_solutions(args, expected):
    assert Solution().maxChunksToSorted(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
