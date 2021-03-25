#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 12:53:27
# @Last Modified : 2020-07-05 12:53:27
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。 
# 
#  请返回所有可行解 s 中最长长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = ["un","iq","ue"]
# 输出：4
# 解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
#  
# 
#  示例 2： 
# 
#  输入：arr = ["cha","r","act","ers"]
# 输出：6
# 解释：可能的解答有 "chaers" 和 "acters"。
#  
# 
#  示例 3： 
# 
#  输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
# 输出：26
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 16 
#  1 <= arr[i].length <= 26 
#  arr[i] 中只含有小写英文字母 
#  
#  Related Topics 位运算 回溯算法 
#  👍 52 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for word in arr:
            if len(set(word)) < len(word):
                continue
            word = set(word)
            for component in dp:
                if word & component:
                    continue
                dp.append(word | component)
        return max(len(st) for st in dp)


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("kwargs,expected", [
    (dict(arr=["un", "iq", "ue"]), 4),
    pytest.param(dict(arr=["cha", "r", "act", "ers"]), 6),
    pytest.param(dict(arr=["abcdefghijklmnopqrstuvwxyz"]), 26),
])
def test_solutions(kwargs, expected):
    assert Solution().maxLength(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
