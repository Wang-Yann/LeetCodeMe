#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 23:25:22
# @Last Modified : 2020-07-22 23:25:22
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 给你一种规律 pattern 和一个字符串 str，请你判断 str 是否遵循其相同的规律。 
# 
#  这里我们指的是 完全遵循，例如 pattern 里的每个字母和字符串 str 中每个 非空 单词之间，存在着双向连接的对应规律。 
# 
#  
# 
#  示例1: 
# 
#  输入: pattern = "abab", str = "redblueredblue"
# 输出: true 
# 
#  示例2: 
# 
#  输入: pattern = "aaaa", str = "asdasdasdasd"
# 输出: true 
# 
#  示例2: 
# 
#  输入: pattern = "aabb", str = "xyzabcxzyabc"
# 输出: false 
# 
#  
# 
#  提示： 
# 
#  
#  你可以默认 pattern 和 str 都只会包含小写字母。 
#  
#  Related Topics 回溯算法 
#  👍 23 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        """TODO"""

        def is_match(pat, string, used):
            if not pat:
                return not string

            char = pat[0]
            if char in mapping:
                word = mapping[char]
                if not string.startswith(word):
                    return False
                return is_match(pat[1:], string[len(word):], used)

            for i in range(len(string)):
                word = string[:i + 1]
                if word in used:
                    continue

                used.add(word)
                mapping[char] = word

                if is_match(pat[1:], string[i + 1:], used):
                    return True

                mapping.pop(char)
                used.remove(word)

            return False

        mapping = {}
        return is_match(pattern, str, set())


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(pattern="abab", str="redblueredblue"), True],

    pytest.param(dict(pattern="aaaa", str="asdasdasdasd"), True),
    pytest.param(dict(pattern="aabb", str="xyzabcxzyabc"), False),
])
def test_solutions(kwargs, expected):
    assert Solution().wordPatternMatch(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
