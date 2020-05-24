#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。 
# 
#  返回符合要求的最少分割次数。 
# 
#  示例: 
# 
#  输入: "aab"
# 输出: 1
# 解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#  
#  Related Topics 动态规划

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minCut(self, s: str) -> int:
        """
        dp[i]：表示前缀子串 s[0:i] 分割成若干个回文子串所需要最小分割次数
        """
        def is_palindrome(left, right):
            return s[left:right + 1] == s[left:right + 1][::-1]

        size = len(s)
        if size < 2:
            return 0
        dp = [0]*size
        for i in range(1, size):
            if is_palindrome(0, i):
                dp[i] = 0
                continue
            dp[i] = min([dp[j] + 1 for j in range(i) if is_palindrome(j + 1, i )])
        return dp[size - 1]


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("args,expected", [
    ("aab", 1),
])
def test_solutions(args, expected):
    assert Solution().minCut(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
