#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 16:25:18
# @Last Modified : 2020-07-31 16:25:18
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个列表 Aand B，并且 B 是 A 的变位（即 B 是由 A 中的元素随机排列后组成的新列表）。 
# 
#  我们希望找出一个从 A 到 B 的索引映射 P 。一个映射 P[i] = j 指的是列表 A 中的第 i 个元素出现于列表 B 中的第 j 个元素上。 
# 
#  列表 A 和 B 可能出现重复元素。如果有多于一种答案，输出任意一种。 
# 
#  例如，给定 
# 
#  A = [12, 28, 46, 32, 50]
# B = [50, 12, 32, 46, 28]
#  
# 
#  
# 
#  需要返回 
# 
#  [1, 4, 3, 2, 0]
#  
# 
#  P[0] = 1 ，因为 A 中的第 0 个元素出现于 B[1]，而且 P[1] = 4 因为 A 中第 1 个元素出现于 B[4]，以此类推。 
# 
#  
# 
#  注： 
# 
#  
#  A, B 有相同的长度，范围为 [1, 100]。 
#  A[i], B[i] 都是范围在 [0, 10^5] 的整数。 
#  
# 
#  
#  Related Topics 哈希表 
#  👍 18 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        lookup = {v: i for i, v in enumerate(B)}
        return [lookup[x] for x in A]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        A=[12, 28, 46, 32, 50],
        B=[50, 12, 32, 46, 28]
    ), [1, 4, 3, 2, 0]],
])
def test_solutions(kw, expected):
    assert Solution().anagramMappings(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
