#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。 
# 
#  现在，给定两个正整数 L 和 R （以字符串形式表示），返回包含在范围 [L, R] 中的超级回文数的数目。 
# 
#  
# 
#  示例： 
# 
#  输入：L = "4", R = "1000"
# 输出：4
# 解释：
# 4，9，121，以及 484 是超级回文数。
# 注意 676 不是一个超级回文数： 26 * 26 = 676，但是 26 不是回文数。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= len(L) <= 18 
#  1 <= len(R) <= 18 
#  L 和 R 是表示 [1, 10^18) 范围的整数的字符串。 
#  int(L) <= int(R) 
#  
# 
#  
#  Related Topics 数学

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def superpalindromesInRange(self, L: str, R: str) -> int:
        """
        https://leetcode-cn.com/problems/super-palindromes/solution/chao-ji-hui-wen-shu-by-leetcode/
        P<10**18
        R<10**9
        R=k||k1
        k<10**5
        """
        L, R = int(L), int(R)
        MAGIC = 10 ** 5

        def reverse(num):
            res = 0
            while num:
                res = 10 * res + num % 10
                num //= 10
            return res

        def is_palindrome(x):
            return  x==reverse(x)

        ans = 0
        # count odd length
        for k in range(MAGIC):
            s = str(k)  # Eg. s = '1234'
            t = s + s[-2::-1]  # t = '1234321'
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(v):
                ans += 1
        # count even length
        for k in range(MAGIC):
            s = str(k)  # Eg. s = '1234'
            t = s + s[::-1]  # t = '12344321'
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(v):
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(L="4", R="1000"), 4),
])
def test_solutions(kwargs, expected):
    # assert Solution1().superpalindromesInRange(**kwargs) == expected
    assert Solution().superpalindromesInRange(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
