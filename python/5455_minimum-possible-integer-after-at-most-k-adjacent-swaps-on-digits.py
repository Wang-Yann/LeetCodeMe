#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-06 01:37:59
# @Last Modified : 2020-07-06 01:37:59
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个字符串 num 和一个整数 k 。其中，num 表示一个很大的整数，字符串中的每个字符依次对应整数上的各个 数位 。 
# 
#  你可以交换这个整数相邻数位的数字 最多 k 次。 
# 
#  请你返回你能得到的最小整数，并以字符串形式返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：num = "4321", k = 4
# 输出："1342"
# 解释：4321 通过 4 次交换相邻数位得到最小整数的步骤如上图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：num = "100", k = 1
# 输出："010"
# 解释：输出可以包含前导 0 ，但输入保证不会有前导 0 。
#  
# 
#  示例 3： 
# 
#  
# 输入：num = "36789", k = 1000
# 输出："36789"
# 解释：不需要做任何交换。
#  
# 
#  示例 4： 
# 
#  
# 输入：num = "22", k = 22
# 输出："22"
#  
# 
#  示例 5： 
# 
#  
# 输入：num = "9438957234785635408", k = 23
# 输出："0345989723478563548"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num.length <= 30000 
#  num 只包含 数字 且不含有 前导 0 。 
#  1 <= k <= 10^9 
#  
#  Related Topics 贪心算法 
#  👍 11 👎 0

"""
import collections
import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class BinaryTree:

    def __init__(self, N: int):
        self.B = [0] * (N + 1)

    def build(self, arr: List[int]):
        for i, v in enumerate(arr):
            self.update(i + 1, v)

    def low_bit(self, x):
        return x & (-x)

    def update(self, index: int, val: int):
        while index < len(self.B):
            self.B[index] += val
            index += self.low_bit(index)

    def get_sum(self, index: int):
        res = 0
        while index > 0:
            res += self.B[index]
            index -= self.low_bit(index)
        return res


class Solution:
    """
    树状数组
    """

    def minInteger(self, num: str, k: int) -> str:
        N = len(num)
        bt = BinaryTree(N)
        ans = ""
        visited = [False] * N
        record = collections.defaultdict(list)
        for i, digit in enumerate(num):
            record[digit].append(i)
        for j in range(N):
            if k == 0:
                break
            # 贪心逐个把最小的字符往最前面移动
            for i in range(10):
                digit = str(i)
                if digit not in record:
                    continue
                index = record[digit][0]
                # 当前位置需要移动index次，
                # 但是在该位置之前已经移动过bt.get_sum(index)个元素
                needed_k = index - bt.get_sum(index + 1)
                if needed_k > k:
                    continue
                record[digit].pop(0)
                if len(record[digit]) == 0:
                    record.pop(digit)
                bt.update(index + 1, 1)
                visited[index] = True
                ans += digit
                k -= needed_k
                break
        # print(record)
        for i in range(N):
            if not visited[i]:
                ans += num[i]
        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def minInteger(self, num: str, k: int) -> str:

        @functools.lru_cache(None)
        def dp(s, kk):
            if len(s) <= 1:
                return s

            if kk == 0:
                return s

            N = len(s)
            if kk > N * (N - 1) // 2:
                return ''.join(sorted(list(s)))

            min_idx = s.index(min(s[:kk + 1]))
            return s[min_idx] + dp(s[0:min_idx] + s[min_idx + 1:], kk - min_idx)

        return dp(num, k)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(num="4321", k=4), "1342"),
    pytest.param(dict(num="100", k=1), "010"),
    pytest.param(dict(num="36789", k=1000), "36789"),
    pytest.param(dict(num="22", k=22), "22"),
    pytest.param(dict(num="9438957234785635408", k=23), "0345989723478563548"),
])
def test_solutions(kwargs, expected):
    assert Solution().minInteger(**kwargs) == expected
    assert Solution1().minInteger(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
