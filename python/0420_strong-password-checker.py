#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

# 一个强密码应满足以下所有条件：
#
#
#  由至少6个，至多20个字符组成。
#  至少包含一个小写字母，一个大写字母，和一个数字。
#  同一字符不能连续出现三次 (比如 "...aaa..." 是不允许的, 但是 "...aa...a..." 是可以的)。
#
#
#  编写函数 strongPasswordChecker(s)，s 代表输入字符串，如果 s 已经符合强密码条件，则返回0；否则返回要将 s 修改为满足强密码
# 条件的字符串所需要进行修改的最小步数。
#
#  插入、删除、替换任一字符都算作一次修改。
#
import string

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
       TODO  HARD HARD
       https://leetcode-cn.com/problems/strong-password-checker/solution/shi-jian-onkong-jian-o10mssi-lu-by-jriver/
    """

    def strongPasswordChecker(self, s: str) -> int:
        complexBal = 3
        if any(c in string.ascii_lowercase for c in s):
            complexBal -= 1
        if any(c in string.ascii_uppercase for c in s):
            complexBal -= 1
        if any(c.isdigit() for c in s):
            complexBal -= 1

        one = 0
        two = 0
        p = 2
        replace = 0
        while p < len(s):
            if s[p] == s[p - 1] == s[p - 2]:
                length = 2
                while p < len(s) and s[p] == s[p - 1]:
                    p += 1
                    length += 1
                replace += length // 3
                if length % 3 == 0:
                    one += 1
                if length % 3 == 1:
                    two += 1
            else:
                p += 1

        if len(s) < 6:
            return max(complexBal, 6 - len(s))
        elif len(s) <= 20:
            return max(complexBal, replace)
        else:
            redundant = len(s) - 20
            replace -= min(redundant, one)
            replace -= min(max(redundant - one, 0), two * 2) // 2
            replace -= max(redundant - one - two * 2, 0) // 3
            return redundant + max(complexBal, replace)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("", 6),
    ("1234567890123456Baaaa", 2),
])
def test_solutions(args, expected):
    assert Solution().strongPasswordChecker(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
