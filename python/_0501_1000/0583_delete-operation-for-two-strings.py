#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。 
# 
#  
# 
#  示例： 
# 
#  输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定单词的长度不超过500。 
#  给定单词中的字符只含有小写字母。 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1, length2 = map(len, (word1, word2))
        if length1 * length2 == 0:
            return length1 or length2
        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]
        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return length1 + length2 - 2 * dp[length1][length2]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (["sea", "eat"], 2),
    (["sea", "tae"], 4)
])
def test_solutions(args, expected):
    assert Solution().minDistance(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
