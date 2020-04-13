#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 20:15:50
# @Last Modified : 2020-04-12 20:15:50
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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
