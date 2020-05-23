#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。 
# 
#  如果不存在最后一个单词，请返回 0 。 
# 
#  说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。 
# 
#  
# 
#  示例: 
# 
#  输入: "Hello World"
# 输出: 5
#  
#  Related Topics 字符串

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        ans = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i].isspace():
                if ans:
                    break
            else:
                ans = s[i] + ans
        return len(ans)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("Hello World", 5),
    (" ", 0),
])
def test_solutions(args, expected):
    assert Solution().lengthOfLastWord(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
