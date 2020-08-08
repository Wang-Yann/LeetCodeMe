#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-08 17:35:50
# @Last Modified : 2020-08-08 17:35:50
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个只包含小写字母的字符串 s ，你需要找到 s 中最多数目的非空子字符串，满足如下条件： 
# 
#  
#  这些字符串之间互不重叠，也就是说对于任意两个子字符串 s[i..j] 和 s[k..l] ，要么 j < k 要么 i > l 。 
#  如果一个子字符串包含字符 char ，那么 s 中所有 char 字符都应该在这个子字符串中。 
#  
# 
#  请你找到满足上述条件的最多子字符串数目。如果有多个解法有相同的子字符串数目，请返回这些子字符串总长度最小的一个解。可以证明最小总长度解是唯一的。 
# 
#  请注意，你可以以 任意 顺序返回最优解的子字符串。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "adefaddaccc"
# 输出：["e","f","ccc"]
# 解释：下面为所有满足第二个条件的子字符串：
# [
#   "adefaddaccc"
#   "adefadda",
#   "ef",
#   "e",
#   "f",
#   "ccc",
# ]
# 如果我们选择第一个字符串，那么我们无法再选择其他任何字符串，所以答案为 1 。如果我们选择 "adefadda" ，剩下子字符串中我们只可以选择 "ccc"
#  ，它是唯一不重叠的子字符串，所以答案为 2 。同时我们可以发现，选择 "ef" 不是最优的，因为它可以被拆分成 2 个子字符串。所以最优解是选择 ["e","
# f","ccc"] ，答案为 3 。不存在别的相同数目子字符串解。
#  
# 
#  示例 2： 
# 
#  输入：s = "abbaccd"
# 输出：["d","bb","cc"]
# 解释：注意到解 ["d","abba","cc"] 答案也为 3 ，但它不是最优解，因为它的总长度更长。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  s 只包含小写英文字母。 
#  
#  Related Topics 贪心算法 
#  👍 26 👎 0
	 

"""

import pytest, traceback
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import TreeNode, ListNode
from sample_datas import BIG_CASE


# leetcode submit region begin(Prohibit modification and deletion)
class Seg:

    def __init__(self, left=-1, right=-1):
        self.left = left
        self.right = right

    def __lt__(self, rhs):
        if self.right == rhs.right:
            return self.left > rhs.left
        return self.right < rhs.right

    def __repr__(self):
        return "[{},{}]".format(self.left, self.right)


class Solution:

    def maxNumOfSubstrings(self, s: str) -> List[str]:
        """
        贪心问题怎么总想不出解答呢
        应该是hard
        https://leetcode-cn.com/problems/maximum-number-of-non-overlapping-substrings/solution/zui-duo-de-bu-zhong-die-zi-zi-fu-chuan-by-leetcode/
        """
        segs = [Seg() for _ in range(26)]
        # 预处理左右端点
        for i in range(len(s)):
            charIdx = ord(s[i]) - ord('a')
            if segs[charIdx].left == -1:
                segs[charIdx].left = segs[charIdx].right = i
            else:
                segs[charIdx].right = i

        for i in range(26):
            if segs[i].left != -1:
                j = segs[i].left
                while j <= segs[i].right:
                    charIdx = ord(s[j]) - ord('a')
                    if segs[i].left <= segs[charIdx].left and segs[charIdx].right <= segs[i].right:
                        pass
                    else:
                        segs[i].left = min(segs[i].left, segs[charIdx].left)
                        segs[i].right = max(segs[i].right, segs[charIdx].right)
                        j = segs[i].left
                    j += 1

        # print(segs)
        # 预处理完以后，我们将每个字符串的起始位置看作一个个线段 [li,ri]​，问题就转化成了有一个 [0, n-1]  的一维数轴，其中 n=s.length，
        # 我们需要用尽可能多的线段去覆盖这个数轴，且线段间互不相交，线段之和最小。这是一个很经典的贪心问题，
        # 我们只需要将得到的线段按右端点为第一关键字，长度为第二关键字排序，然后从前往后遍历线段，每次遇到可以加入答案的线段，就贪心地将其加入答案数组即可。

        # 贪心选取
        segs.sort()
        ans = list()
        end = -1
        for segment in segs:
            left, right = segment.left, segment.right
            if left == -1:
                continue
            if end == -1 or left > end:
                end = right
                ans.append(s[left:right + 1])

        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(s="adefaddaccc"), ["e", "f", "ccc"]],
    pytest.param(dict(s="abbaccd"), ["d", "bb", "cc"]),
])
def test_solutions(kwargs, expected):
    assert sorted(Solution().maxNumOfSubstrings(**kwargs)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
