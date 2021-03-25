#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-06 10:47:22
# @Last Modified : 2020-08-06 10:47:22
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你有一大块巧克力，它由一些甜度不完全相同的小块组成。我们用数组 sweetness 来表示每一小块的甜度。 
# 
#  你打算和 K 名朋友一起分享这块巧克力，所以你需要将切割 K 次才能得到 K+1 块，每一块都由一些 连续 的小块组成。 
# 
#  为了表现出你的慷慨，你将会吃掉 总甜度最小 的一块，并将其余几块分给你的朋友们。 
# 
#  请找出一个最佳的切割策略，使得你所分得的巧克力 总甜度最大，并返回这个 最大总甜度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：sweetness = [1,2,3,4,5,6,7,8,9], K = 5
# 输出：6
# 解释：你可以把巧克力分成 [1,2,3], [4,5], [6], [7], [8], [9]。
#  
# 
#  示例 2： 
# 
#  输入：sweetness = [5,6,7,8,9,1,2,3,4], K = 8
# 输出：1
# 解释：只有一种办法可以把巧克力分成 9 块。
#  
# 
#  示例 3： 
# 
#  输入：sweetness = [1,2,2,1,2,2,1,2,2], K = 2
# 输出：5
# 解释：你可以把巧克力分成 [1,2,2], [1,2,2], [1,2,2]。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= K < sweetness.length <= 10^4 
#  1 <= sweetness[i] <= 10^5 
#  
#  Related Topics 贪心算法 二分查找 
#  👍 26 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        """二分查找猜答案"""
        def check(x):
            cur = cuts = 0
            for s in sweetness:
                cur += s
                if cur >= x:
                    cuts += 1
                    cur = 0
            return cuts >= (K + 1)

        l, r = min(sweetness), sum(sweetness) // (K + 1)
        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        # print(l,r)
        return r


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(sweetness=[1, 2, 3, 4, 5, 6, 7, 8, 9], K=5), 6],
    [dict(sweetness=[5, 6, 7, 8, 9, 1, 2, 3, 4], K=8), 1],
    [dict(sweetness=[1, 2, 2, 1, 2, 2, 1, 2, 2], K=2), 5],
])
def test_solutions(kw, expected):
    assert Solution().maximizeSweetness(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
