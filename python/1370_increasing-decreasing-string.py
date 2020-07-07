#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-07 22:28:22
# @Last Modified : 2020-07-07 22:28:22
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""

# 给你一个字符串 s ，请你根据下面的算法重新构造字符串： 
# 
#  
#  从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。 
#  从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。 
#  重复步骤 2 ，直到你没法从 s 中选择字符。 
#  从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。 
#  从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。 
#  重复步骤 5 ，直到你没法从 s 中选择字符。 
#  重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。 
#  
# 
#  在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。 
# 
#  请你返回将 s 中字符重新排序后的 结果字符串 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "aaaabbbbcccc"
# 输出："abccbaabccba"
# 解释：第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
# 第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
# 第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
# 第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
# 第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"
#  
# 
#  示例 2： 
# 
#  输入：s = "rat"
# 输出："art"
# 解释：单词 "rat" 在上述算法重排序以后变成 "art"
#  
# 
#  示例 3： 
# 
#  输入：s = "leetcode"
# 输出："cdelotee"
#  
# 
#  示例 4： 
# 
#  输入：s = "ggggggg"
# 输出："ggggggg"
#  
# 
#  示例 5： 
# 
#  输入：s = "spo"
# 输出："ops"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 500 
#  s 只包含小写英文字母。 
#  
#  Related Topics 排序 字符串 
#  👍 13 👎 0


"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def sortString(self, s: str) -> str:
        """桶"""
        result, count = [], [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        while len(result) != len(s):
            for c in range(len(count)):
                if not count[c]:
                    continue
                result.append(chr(ord('a') + c))
                count[c] -= 1
            for c in reversed(range(len(count))):
                if not count[c]:
                    continue
                result.append(chr(ord('a') + c))
                count[c] -= 1
        return "".join(result)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def sortString(self, s: str) -> str:
        sorted_s = sorted(s)
        ans = []
        while sorted_s:
            tmp = []
            for char in sorted_s:
                if not ans or ans[-1] != char:
                    ans.append(char)
                else:
                    tmp.append(char)
            ans.append("")
            sorted_s = tmp[::-1]
        return "".join(ans)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="aaaabbbbcccc"), "abccbaabccba"),
    pytest.param(dict(s="rat"), "art"),
    pytest.param(dict(s="leetcode"), "cdelotee"),
    pytest.param(dict(s="ggggggg"), "ggggggg"),
    pytest.param(dict(s="spo"), "ops"),
])
def test_solutions(kwargs, expected):
    assert Solution().sortString(**kwargs) == expected
    assert Solution1().sortString(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
