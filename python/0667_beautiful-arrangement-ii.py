#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个整数 n 和 k，你需要实现一个数组，这个数组包含从 1 到 n 的 n 个不同整数，同时满足以下条件： 
# 
#  ① 如果这个数组是 [a1, a2, a3, ... , an] ，那么数组 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... 
# , |an-1 - an|] 中应该有且仅有 k 个不同整数；. 
# 
#  ② 如果存在多种答案，你只需实现并返回其中任意一种. 
# 
#  示例 1: 
# 
#  
# 输入: n = 3, k = 1
# 输出: [1, 2, 3]
# 解释: [1, 2, 3] 包含 3 个范围在 1-3 的不同整数， 并且 [1, 1] 中有且仅有 1 个不同整数 : 1
#  
# 
#  
# 
#  示例 2: 
# 
#  
# 输入: n = 3, k = 2
# 输出: [1, 3, 2]
# 解释: [1, 3, 2] 包含 3 个范围在 1-3 的不同整数， 并且 [2, 1] 中有且仅有 2 个不同整数: 1 和 2
#  
# 
#  
# 
#  提示: 
# 
#  
#  n 和 k 满足条件 1 <= k < n <= 104. 
#  
# 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        """
        采用这样的放置方式：
        1 , 2 , 3 … … n − k − 1 , n − k , n , n − k + 1 , n − 1 , n − k + 2 , n − 2 …
        这样可以同时保证在原序列中1~n均出现一次，差值序列中1~k均出现一次。
        """
        array = []
        l, r = 1, n
        for i in range(k, 1, -1):
            if i % 2 == 1:
                array.append(l)
                l += 1
            else:
                array.append(r)
                r -= 1
        for i in range(l, r + 1):
            array.append(i)
        return array


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=3, k=1), ([1, 2, 3],)],
    [dict(n=3, k=2), ([1, 3, 2], [3, 1, 2])],
])
def test_solutions(kw, expected):
    assert Solution().constructArray(**kw) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
