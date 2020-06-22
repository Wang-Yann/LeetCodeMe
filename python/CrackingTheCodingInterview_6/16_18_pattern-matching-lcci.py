#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatg
# o"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相
# 同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。 
#  示例 1： 
#  输入： pattern = "abba", value = "dogcatcatdog"
# 输出： true
#  
#  示例 2： 
#  输入： pattern = "abba", value = "dogcatcatfish"
# 输出： false
#  
#  示例 3： 
#  输入： pattern = "aaaa", value = "dogcatcatdog"
# 输出： false
#  
#  示例 4： 
#  输入： pattern = "abba", value = "dogdogdogdog"
# 输出： true
# 解释： "a"="dogdog",b=""，反之也符合规则
#  
#  提示： 
#  
#  0 <= len(pattern) <= 1000 
#  0 <= len(value) <= 1000 
#  你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。 
#  
#  Related Topics 字符串

"""
import re

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        regex = ""
        a = b = ""
        group = 0
        for char in pattern:
            if char == "a":
                if a:
                    regex += a
                else:
                    regex += r"(\w*)"
                    group += 1
                    a = "\\" + str(group)
            elif char == "b":
                if b:
                    regex += b
                else:
                    regex += r"(\w*)"
                    group += 1
                    b = "\\" + str(group)
        regex = r"^{}$".format(regex)
        match = re.match(regex, value)
        # print(match, match.group(2) if match else "xx")
        return bool(match) and (len(match.groups()) < 2 or match.group(1) != match.group(2))


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    """边界情况太多"""

    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = sum(1 for char in pattern if char == "a")
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = "".join("a" if char == "b" else "b" for char in pattern)
        if not value:
            return count_b == 0
        if not pattern:
            return False
        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - count_a * len_a
            if (count_b == 0 and rest == 0) or (count_b != 0 and rest % count_b == 0):
                len_b = 0 if count_b == 0 else rest // count_b
                pos, correct = 0, True
                value_a, value_b = None, None
                for char in pattern:
                    if char == "a":
                        sub = value[pos:pos + len_a]
                        if not value_a:
                            value_a = sub
                        elif value_a != sub:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos:pos + len_b]
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:
                    return True
        return False


@pytest.mark.parametrize("kw,expected", [
    [dict(pattern="abba", value="dogcatcatdog"), True],
    [dict(pattern="abba", value="dogcatcatfish"), False],
    [dict(pattern="aaaa", value="dogcatcatdog"), False],
    [dict(pattern="abba", value="dogdogdogdog"), True],
    [dict(pattern="ab", value=""), False],
    [dict(pattern="", value=""), True],
])
def test_solutions(kw, expected):
    assert Solution().patternMatching(**kw) == expected
    # assert Solution1().patternMatching(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
