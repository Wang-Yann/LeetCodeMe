#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 20:15:50
# @Last Modified : 2020-04-12 20:15:50
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
#
#
# 示例:
# 输入: S = "a1b2"
# 输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# 输入: S = "3z4"
# 输出: ["3z4", "3Z4"]
#
# 输入: S = "12345"
# 输出: ["12345"]
#
#
#  注意：
#
#
#  S 的长度不超过12。
#  S 仅由数字和字母组成。
#
#  Related Topics 位运算 回溯算法
#  👍 186 👎 0

"""



from typing import List


class Solution:

    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(first, curr):
            if len(curr) == n:
                output.append(curr)
            for i in range(first, n):
                char = S[i]
                if char.isalpha():
                    backtrack(i + 1, curr + char.lower())
                    backtrack(i + 1, curr + char.upper())
                else:
                    backtrack(i + 1, curr + char)
        output = []
        n = len(S)
        backtrack(0, "")
        return output


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "a1b2",
        "3z4",
        "12345",
        ""
    ]
    res = [sol.letterCasePermutation(x) for x in samples]
    print(res)
