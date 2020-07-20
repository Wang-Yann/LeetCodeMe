#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 23:45:34
# @Last Modified : 2020-04-22 23:45:34
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
#
#
#
#  示例 1：
#
#  输入：s = "We are happy."
# 输出："We%20are%20happy."
#
#
#
#  限制：
#
#  0 <= s 的长度 <= 10000
#  👍 29 👎 0

class Solution:

    def replaceSpace(self, s: str) -> str:
        if not s:
            return s
        length = len(s)
        number_of_blank = 0
        for ch in s:
            if ch == " ":
                number_of_blank += 1
        new_length = length + number_of_blank * 2
        idx_of_origin = length - 1
        idx_of_new = new_length - 1
        s_chars = [ch for ch in s + " " * number_of_blank * 2]
        while idx_of_new > idx_of_origin >= 0:
            if s_chars[idx_of_origin] == " ":
                s_chars[idx_of_new] = "0"
                idx_of_new -= 1
                s_chars[idx_of_new] = "2"
                idx_of_new -= 1
                s_chars[idx_of_new] = "%"
                idx_of_new -= 1
            else:
                s_chars[idx_of_new] = s_chars[idx_of_origin]
                idx_of_new -= 1

            idx_of_origin -= 1
        return "".join(s_chars)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "We are happy.",
        "",
        " hello "
    ]
    res = [sol.replaceSpace(x) for x in samples]
    print(res)
