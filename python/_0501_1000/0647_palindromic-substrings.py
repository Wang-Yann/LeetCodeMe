#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 22:41:48
# @Last Modified : 2020-05-03 22:41:48
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
#
#  示例 1:
#
#
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
#
#
#  示例 2:
#
#
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
#
#
#  注意:
#
#
#  输入的字符串长度不会超过1000。
#
#  Related Topics 字符串 动态规划
#  👍 282 👎 0

"""

import pytest


class Solution:

    def countSubstrings(self, s: str) -> int:
        """马拉车算法 Manacher’s Algorithm
        是用来查找一个字符串的最长回文子串的线性方法
        https://oi-wiki.org/string/manacher/
        """

        def manachers(s):
            """其中P[i]表示以 i 为中心的最长回文的半径
            # 设置两个变量，right 和 center 。right 代表以 id 为中心的最长回文的右边界，right = id + p[id]。
            ---
            设置两个变量，mx 和 id 。mx 代表以 id 为中心的最长回文的右边界，也就是mx = id + p[id]。
            int Init()
            {
                int len = strlen(s);
                s_new[0] = '$';
                s_new[1] = '#';
                int j = 2;
                for (int i = 0; i < len; i++)
                {
                    s_new[j++] = s[i];
                    s_new[j++] = '#';
                }
                s_new[j] = '\0';  // 别忘了哦
                return j;  // 返回 s_new 的长度
            }
            int Manacher()
            {
                int len = Init();  // 取得新字符串长度并完成向 s_new 的转换
                int max_len = -1;  // 最长回文长度
                int id;
                int mx = 0;
                for (int i = 1; i < len; i++)
                {
                    if (i < mx)
                        p[i] = min(p[2 * id - i], mx - i);  // 需搞清楚上面那张图含义, mx 和 2*id-i 的含义
                    else
                        p[i] = 1;
                    while (s_new[i - p[i]] == s_new[i + p[i]])  // 不需边界判断，因为左有'$',右有'\0'
                        p[i]++;
                    // 我们每走一步 i，都要和 mx 比较，我们希望 mx 尽可能的远，这样才能更有机会执行 if (i < mx)这句代码，从而提高效率
                    if (mx < i + p[i])
                    {
                        id = i;
                        mx = i + p[i];
                    }
                    max_len = max(max_len, p[i] - 1);
                }
                return max_len;
            }


            """

            s_new = "^#" + "#".join(s) + "#$"
            P = [0] * len(s_new)
            center, max_right = 0, 0
            for i in range(1, len(s_new) - 1):
                if i < max_right:
                    P[i] = min(max_right - i, P[2 * center - i])
                while s_new[i + P[i] + 1] == s_new[i - P[i] - 1]:
                    P[i] += 1
                if i + P[i] > max_right:
                    center, max_right = i, i + P[i]
            # print("s_new,P",s_new,P)
            return P

        return sum((v + 1) // 2 for v in manachers(s))


class Solution1:

    def countSubstrings(self, s):
        """
        考虑如果substring(i,j)如果是回文串，那么str[i]和str[j]一定相同，
        并且一定满足以下两个条件之一
        1.substring(i+1,j-1)也是回文串
        2.j-i<=2，即substring(i,j)长度<=2

        """
        N = len(s)
        dp = [[0] * N for _ in range(N)]
        ans = 0
        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1] )
                if dp[i][j]:
                    ans += 1
        return ans


class Solution2:

    def countSubstrings(self, s):
        N = len(s)
        self.ans = 0

        def helper(l, r):
            while l >= 0 and r <= N - 1 and s[l] == s[r]:
                l -= 1
                r += 1
                self.ans += 1

        if not s:
            return 0
        for i in range(N):
            helper(i, i)
            helper(i, i + 1)
        return self.ans


@pytest.mark.parametrize("args,expected", [
    ("abc", 3),
    pytest.param("aaa", 6),
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1, Solution2])
def test_solutions(args, expected, SolutionCLS):
    assert SolutionCLS().countSubstrings(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
