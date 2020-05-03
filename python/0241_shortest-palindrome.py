#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 20:02:15
# @Last Modified : 2020-05-03 20:02:15
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        rev = "".join(reversed(s))
        for i in range(length):
            if s[:length - i] == rev[i:]:
                return rev[:i] + s
        return ""


class Solution1:

    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        i = 0
        for j in range(length - 1, -1, -1):
            if s[i] == s[j]:
                i += 1
        if i == length:
            return s
        remain_rev = s[length - 1:i - 1:-1]
        return remain_rev + self.shortestPalindrome(s[:i]) + s[i:]


class Solution3:
    def shortestPalindrome(self, s: str) -> str:
        def get_table(p):
            """
            KMP
            生成部分匹配表的算法简单而直观，如下所示：

            f(0) = 0
            for(i = 1; i < n; i++)
            {
                t = f(i-1)
                while(t > 0 && b[i] != b[t])
                    t = f(t-1)
                if(b[i] == b[t]){
                    ++t
                f(i) = t
            }

            """
            table = [0] * len(p)
            i = 1
            j = 0
            while i < len(p):
                if p[i] == p[j]:
                    j += 1
                    table[i] = j
                    i += 1
                else:
                    if j > 0:
                        j = table[j - 1]
                    else:
                        i += 1
                        j = 0
            return table

        table = get_table(s + "#" + s[::-1])
        return s[table[-1]:][::-1] + s

class Solution2:
    """KMP"""

    def getPrefix(self, pattern):
        """
        每一个模式串P都有有一个固定的next数组，它记录着字符串匹配过程中失配情况下可以向前多跳几个字符
        next[j]的值（也就是k）表示，当P[j] != T[i]时，j指针的下一步移动位置。
        所有要与甲匹配的字符串（称之为模式串），必须先自身匹配：对每个子字符串 [0...i]，算出其「相匹配的真前缀与真后缀中，最长的字符串的长度」

        KMP算法的重点就是维护一个数组，保存match中每个字符在不匹配时，match应该滑动到什么位置，这个数组起名叫next。
        -----
        http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
        -----
        掌握这句话，f[i]是到i为止最长的既是前缀也是后缀的串的长度
        举个例子，字符串ABAAB

        当i=0时，字符串为"A"，，此时最左前缀为空，最右前缀也为空，next[0]==空；
        当i=1时，字符串为"AB"，，此时最左前缀为{A}，最右前缀为{B}，next[1]==0；
        当i=2时，字符串为"ABA"，，此时最左前缀为{A,AB}，最右前缀为A,BA}，next[2]==1；
        当i=3时，字符串为"ABAA"，，此时最左前缀为{A,AB,ABA}，最右前缀为{A,AA,BAA}，next[3]==1；
        当i=4时，字符串为"ABAAB"，，此时最左前缀为{A,AB,ABA,ABAA}，最右前缀为{B,AB,AAB,BAAB}，next[4]==2；

        """
        prefix = [-1] * len(pattern)
        t = -1
        for i in range(1, len(pattern)):
            while t > -1 and pattern[t + 1] != pattern[i]:
                t = prefix[t]
            if pattern[t + 1] == pattern[i]:
                t += 1
            prefix[i] = t
        # print("prefix", prefix, pattern)
        return prefix

    def shortestPalindrome(self, s: str) -> str:


        A = s + "#" +s[::-1]
        next_table = self.getPrefix(A)
        i = next_table[-1]
        # print("A,prefix,i",A,next_table,i)
        # return s[i+1:][::-1]+s
        return s[len(s) - 1:i:-1] + s



@pytest.mark.parametrize("args,expected", [
    ("aacecaaa", "aaacecaaa"),
    pytest.param("abcd", "dcbabcd"),
])
def test_solutions(args, expected):
    assert Solution().shortestPalindrome(args) == expected
    assert Solution1().shortestPalindrome(args) == expected
    assert Solution2().shortestPalindrome(args) == expected
    assert Solution3().shortestPalindrome(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
    # print(Solution2().getPrefix("cacacabc"))
    #[-1, -1, 0, 1, 2, 3, -1, 0]
