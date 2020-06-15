#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，同时将子数组中的每个 0 更改为 1，而每个 1 更改为 0
# 。 
# 
#  返回所需的 K 位翻转的次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [0,1,0], K = 1
# 输出：2
# 解释：先翻转 A[0]，然后翻转 A[2]。
#  
# 
#  示例 2： 
# 
#  输入：A = [1,1,0], K = 2
# 输出：-1
# 解释：无论我们怎样翻转大小为 2 的子数组，我们都不能使数组变为 [1,1,1]。
#  
# 
#  示例 3： 
# 
#  输入：A = [0,0,0,1,0,1,1,0], K = 3
# 输出：3
# 解释：
# 翻转 A[0],A[1],A[2]: A变成 [1,1,1,1,0,1,1,0]
# 翻转 A[4],A[5],A[6]: A变成 [1,1,1,1,1,0,0,0]
# 翻转 A[5],A[6],A[7]: A变成 [1,1,1,1,1,1,1,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 30000 
#  1 <= K <= A.length 
#  
#  Related Topics 贪心算法 Sliding Window

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        """
        滑动窗口
        当处理A[i]时，它已经被翻转了多少次？只需要采用一个队列，将[i-K+1, i-1]这个窗口内所有被翻转的数字的下标加入到这个队列来。当我们处理A[i]时，只要看当前的队列长度，就知道A[i]被翻转的次数！
        https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips/solution/tan-xin-he-hua-dong-chuang-kou-liang-chong-jie-fa-/
        """
        ans = 0
        q = collections.deque()
        for i in range(len(A)):
            print(q)
            if q and q[0] + K == i:
                q.popleft()
            # len(q)翻转次数
            # 分奇偶讨论下都是需要反转的情况
            if len(q) % 2 == A[i]:
                if i + K > len(A):
                    return -1
                ans += 1
                q.append(i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    # [dict(A=[0, 1, 0], K=1), 2],
    # [dict(A=[1, 1, 0], K=2), -1],
    [dict(A=[0, 0, 0, 1, 0, 1, 1, 0], K=3), 3],
])
def test_solutions(kw, expected):
    assert Solution().minKBitFlips(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
