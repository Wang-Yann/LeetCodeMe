#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 16:11:15
# @Last Modified : 2020-07-10 16:11:15
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 arr 和一个整数 k 。现需要从数组中恰好移除 k 个元素，请找出移除后数组中不同整数的最少数目。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [5,5,4], k = 1
# 输出：1
# 解释：移除 1 个 4 ，数组中只剩下 5 一种整数。
#  
# 
#  示例 2： 
# 
#  输入：arr = [4,3,1,1,3,3,2], k = 3
# 输出：2
# 解释：先移除 4、2 ，然后再移除两个 1 中的任意 1 个或者三个 3 中的任意 1 个，最后剩下 1 和 3 两种整数。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  1 <= arr[i] <= 10^9 
#  0 <= k <= arr.length 
#  
#  Related Topics 排序 数组 
#  👍 10 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """AAC"""
        counter = collections.Counter(arr)
        for num, cnt in reversed(counter.most_common()):
            if k > cnt:
                k -= cnt
                counter[num] = 0
            else:
                counter[num] = cnt - k
                break
        # print(counter)
        return sum(v > 0 for v in counter.values())


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[5, 5, 4], k=1), 1],
    [dict(arr=[4, 3, 1, 1, 3, 3, 2], k=3), 2],
])
def test_solutions(kw, expected):
    assert Solution().findLeastNumOfUniqueInts(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
