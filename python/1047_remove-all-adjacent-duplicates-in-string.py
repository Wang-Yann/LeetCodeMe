#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-30 08:00:00
# @Last Modified : 2020-06-30 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。 
# 
#  在 S 上反复执行重复项删除操作，直到无法继续删除。 
# 
#  在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。 
# 
#  
# 
#  示例： 
# 
#  输入："abbaca"
# 输出："ca"
# 解释：
# 例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又
# 只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= S.length <= 20000 
#  S 仅由小写英文字母组成。 
#  
#  Related Topics 栈

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    """注意审题　重复两个"""
    def removeDuplicates(self, S):
        result = []
        for c in S:
            if result and result[-1] == c:
                result.pop()
            else:
                result.append(c)
        return "".join(result)


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        S = list(S)
        while True:
            for char in S:
                if stack and stack[-1] == char:
                    while stack and stack[-1] == char:
                        stack.pop()
                else:
                    stack.append(char)
            if stack == S:
                break
            S = stack
            stack = []
        return "".join(S)


@pytest.mark.parametrize("args,expected", [
    ("abbaca", "ca")
])
def test_solutions(args, expected):
    assert Solution1().removeDuplicates(args) == expected
    assert Solution().removeDuplicates(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
