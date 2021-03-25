#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 10:55:25
# @Last Modified : 2020-08-05 10:55:25
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们定制了一款特殊的力扣键盘，所有的键都排列在一行上。 
# 
#  我们可以按从左到右的顺序，用一个长度为 26 的字符串 keyboard （索引从 0 开始，到 25 结束）来表示该键盘的键位布局。 
# 
#  现在需要测试这个键盘是否能够有效工作，那么我们就需要个机械手来测试这个键盘。 
# 
#  最初的时候，机械手位于左边起第一个键（也就是索引为 0 的键）的上方。当机械手移动到某一字符所在的键位时，就会在终端上输出该字符。 
# 
#  机械手从索引 i 移动到索引 j 所需要的时间是 |i - j|。 
# 
#  当前测试需要你使用机械手输出指定的单词 word，请你编写一个函数来计算机械手输出该单词所需的时间。 
# 
#  
# 
#  示例 1： 
# 
#  输入：keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
# 输出：4
# 解释：
# 机械手从 0 号键移动到 2 号键来输出 'c'，又移动到 1 号键来输出 'b'，接着移动到 0 号键来输出 'a'。
# 总用时 = 2 + 1 + 1 = 4. 
#  
# 
#  示例 2： 
# 
#  输入：keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
# 输出：73
#  
# 
#  
# 
#  提示： 
# 
#  
#  keyboard.length == 26 
#  keyboard 按某种特定顺序排列，并包含每个小写英文字母一次。 
#  1 <= word.length <= 10^4 
#  word[i] 是一个小写英文字母 
#  
#  Related Topics 字符串 
#  👍 7 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        lookup = {char: i for i, char in enumerate(keyboard)}
        pos = ans = 0
        for char in word:
            new_pos = lookup[char]
            ans += abs(new_pos - pos)
            pos = new_pos
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(keyboard="abcdefghijklmnopqrstuvwxyz", word="cba"), 4],
    [dict(keyboard="pqrstuvwxyzabcdefghijklmno", word="leetcode"), 73],
])
def test_solutions(kw, expected):
    assert Solution().calculateTime(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
