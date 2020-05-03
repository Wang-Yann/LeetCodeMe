#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 22:41:48
# @Last Modified : 2020-05-03 22:41:48
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def countSubstrings(self, s: str) -> int:
        """马拉车算法Manacher’s Algorithm
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


@pytest.mark.parametrize("args,expected", [
    ("abc", 3),
    pytest.param("aaa", 6),
])
def test_solutions(args, expected):
    assert Solution().countSubstrings(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
