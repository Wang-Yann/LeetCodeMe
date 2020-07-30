#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-30 14:06:59
# @Last Modified : 2020-07-30 14:06:59
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串列表，你可以将这些字符串连接成一个循环字符串，对于每个字符串，你可以选择是否翻转它。在所有可能的循环字符串中，你需要分割循环字符串（这将使循环
# 字符串变成一个常规的字符串），然后找到字典序最大的字符串。 
# 
#  具体来说，要找到字典序最大的字符串，你需要经历两个阶段： 
# 
#  
#  将所有字符串连接成一个循环字符串，你可以选择是否翻转某些字符串，并按照给定的顺序连接它们。 
#  在循环字符串的某个位置分割它，这将使循环字符串从分割点变成一个常规的字符串。 
#  
# 
#  你的工作是在所有可能的常规字符串中找到字典序最大的一个。 
# 
#  示例: 
# 
#  输入: "abc", "xyz"
# 输出: "zyxcba"
# 解释: 你可以得到循环字符串 "-abcxyz-", "-abczyx-", "-cbaxyz-", "-cbazyx-"，
# 其中 '-' 代表循环状态。 
# 答案字符串来自第四个循环字符串， 
# 你可以从中间字符 'a' 分割开然后得到 "zyxcba"。
#  
# 
#  
# 
#  注意: 
# 
#  
#  输入字符串只包含小写字母。 
#  所有字符串的总长度不会超过 1,000。 
#  
# 
#  
#  Related Topics 字符串 
#  👍 16 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        """读不明白题意"""
        strs = [s[::-1] if s[::-1] > s else s for s in strs]
        ans = "".join(strs)
        for i, s in enumerate(strs):
            other = "".join(strs[i + 1:]) + "".join(strs[:i])
            for j in range(len(s)):
                head = s[j:]
                tail = s[:j]
                ans = max(ans, head + other + tail, tail[::-1] + other + head[::-1])
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (["abc", "xyz"], "zyxcba"),
    (["lc", "evol", "cdy"], "ylclovecd"),
    (["acd", "dfg", "xayc"], "ycdcagfdxa")
])
def test_solutions(args, expected):
    assert Solution().splitLoopedString(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
