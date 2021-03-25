#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-23 16:00:22
# @Last Modified : 2020-07-23 16:00:22
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个非空的字符串 s 和一个整数 k，你要将这个字符串中的字母进行重新排列，使得重排后的字符串中相同字母的位置间隔距离至少为 k。 
# 
#  所有输入的字符串都由小写字母组成，如果找不到距离至少为 k 的重排结果，请返回一个空字符串 ""。 
# 
#  示例 1： 
# 
#  输入: s = "aabbcc", k = 3
# 输出: "abcabc" 
# 解释: 相同的字母在新的字符串中间隔至少 3 个单位距离。
#  
# 
#  示例 2: 
# 
#  输入: s = "aaabc", k = 3
# 输出: "" 
# 解释: 没有办法找到可能的重排结果。
#  
# 
#  示例 3: 
# 
#  输入: s = "aaadbbcc", k = 2
# 输出: "abacabcd"
# 解释: 相同的字母在新的字符串中间隔至少 2 个单位距离。
#  
#  Related Topics 堆 贪心算法 哈希表 
#  👍 28 👎 0

"""

import collections
import heapq

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        """
        TODO
        """
        if k <= 1:
            return s
        counter = collections.Counter(s)
        max_heap = []
        for char, cnt in counter.items():
            heapq.heappush(max_heap, [-cnt, char])
        res = []
        while max_heap:
            used_cnt_chars = []
            for _ in range(min(k, len(s) - len(res))):
                if not max_heap:
                    return ""
                cnt_char = heapq.heappop(max_heap)
                res.append(cnt_char[1])
                cnt_char[0] += 1
                if cnt_char[0] < 0:
                    used_cnt_chars.append(cnt_char)
            for cnt_char in used_cnt_chars:
                heapq.heappush(max_heap, cnt_char)
        return "".join(res)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="aabbcc", k=3), "abcabc"],
    [dict(s="aaabc", k=3), ""],
    [dict(s="aaadbbcc", k=2), "abacabcd"],
])
def test_solutions(kw, expected):
    assert Solution().rearrangeString(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
