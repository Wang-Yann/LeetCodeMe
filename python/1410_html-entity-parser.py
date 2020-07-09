#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 「HTML 实体解析器」 是一种特殊的解析器，它将 HTML 代码作为输入，并用字符本身替换掉所有这些特殊的字符实体。 
# 
#  HTML 里这些特殊字符和它们对应的字符实体包括： 
# 
#  
#  双引号：字符实体为 &quot; ，对应的字符是 " 。 
#  单引号：字符实体为 &apos; ，对应的字符是 ' 。 
#  与符号：字符实体为 &amp; ，对应对的字符是 & 。 
#  大于号：字符实体为 &gt; ，对应的字符是 > 。 
#  小于号：字符实体为 &lt; ，对应的字符是 < 。 
#  斜线号：字符实体为 &frasl; ，对应的字符是 / 。 
#  
# 
#  给你输入字符串 text ，请你实现一个 HTML 实体解析器，返回解析器解析后的结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：text = "&amp; is an HTML entity but &ambassador; is not."
# 输出："& is an HTML entity but &ambassador; is not."
# 解释：解析器把字符实体 &amp; 用 & 替换
#  
# 
#  示例 2： 
# 
#  
# 输入：text = "and I quote: &quot;...&quot;"
# 输出："and I quote: \"...\""
#  
# 
#  示例 3： 
# 
#  
# 输入：text = "Stay home! Practice on Leetcode :)"
# 输出："Stay home! Practice on Leetcode :)"
#  
# 
#  示例 4： 
# 
#  
# 输入：text = "x &gt; y &amp;&amp; x &lt; y is always false"
# 输出："x > y && x < y is always false"
#  
# 
#  示例 5： 
# 
#  
# 输入：text = "leetcode.com&frasl;problemset&frasl;all"
# 输出："leetcode.com/problemset/all"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text.length <= 10^5 
#  字符串可能包含 256 个ASCII 字符中的任意字符。 
#  
#  Related Topics 栈 字符串

"""

import pytest


#  双引号：字符实体为 &quot; ，对应的字符是 " 。
#  单引号：字符实体为 &apos; ，对应的字符是 ' 。
#  与符号：字符实体为 &amp; ，对应对的字符是 & 。
#  大于号：字符实体为 &gt; ，对应的字符是 > 。
#  小于号：字符实体为 &lt; ，对应的字符是 < 。
#  斜线号：字符实体为 &frasl; ，对应的字符是 / 。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def entityParser(self, text: str) -> str:
        return text.replace(
            "&quot;", '"'
        ).replace(
            "&apos;", "'"
        ).replace(
            "&gt;", ">"
        ).replace(
            "&lt;", "<"
        ).replace(
            "&frasl;", "/"
        ).replace(
            "&amp;", "&"
        )


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(text="&amp; is an HTML entity but &ambassador; is not."), "& is an HTML entity but &ambassador; is not."],
    [dict(text="and I quote: &quot;...&quot;"), "and I quote: \"...\""],
    [dict(text="&amp; is an HTML entity but &ambassador; is not."), "& is an HTML entity but &ambassador; is not."],
    [dict(text="&amp; is an HTML entity but &ambassador; is not."), "& is an HTML entity but &ambassador; is not."],
    [dict(text="&amp;gt;"), "&gt;"],
])
def test_solutions(kw, expected):
    assert Solution().entityParser(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
