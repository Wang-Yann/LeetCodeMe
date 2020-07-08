#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个以二进制形式表示的数字 s 。请你返回按下述规则将其减少到 1 所需要的步骤数： 
# 
#  
#  
#  如果当前数字为偶数，则将其除以 2 。 
#  
#  
#  如果当前数字为奇数，则将其加上 1 。 
#  
#  
# 
#  题目保证你总是可以按上述规则将测试用例变为 1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "1101"
# 输出：6
# 解释："1101" 表示十进制数 13 。
# Step 1) 13 是奇数，加 1 得到 14 
# Step 2) 14 是偶数，除 2 得到 7
# Step 3) 7  是奇数，加 1 得到 8
# Step 4) 8  是偶数，除 2 得到 4  
# Step 5) 4  是偶数，除 2 得到 2 
# Step 6) 2  是偶数，除 2 得到 1  
#  
# 
#  示例 2： 
# 
#  输入：s = "10"
# 输出：1
# 解释："10" 表示十进制数 2 。
# Step 1) 2 是偶数，除 2 得到 1 
#  
# 
#  示例 3： 
# 
#  输入：s = "1"
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 500 
#  s 由字符 '0' 或 '1' 组成。 
#  s[0] == '1' 
#  
#  Related Topics 位运算 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSteps(self, s: str) -> int:
        """
        太Trick了
        """
        n, ans = len(s), 0
        # meet1 记录我们有没有遇见过字符 1
        meet1 = False
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                # 如果当前字符为 0，分为两种情况
                # (1) 还没有遇见过字符 1，那么这个 0 是字符串低位的 0，需要一次除二操作
                # (2) 遇见过字符 1，那么这个 0 会因为它右侧的某次加一操作变为 1，因此它需要一次加一和一次除二操作
                ans += (2 if meet1 else 1)
            else:
                # 如果当前字符为 1，分为两种情况
                # (1) 还没有遇见过字符 1，那么这个 1 需要一次加一和一次除二操作
                #     这里需要考虑一种特殊情况，就是这个 1 是字符串最左侧的 1，它并不需要任何操作
                # (2) 遇见过字符 1，那么这个 1 会因为它右侧的某次加一操作变为 0，因此它只需要一次除二操作
                if not meet1:
                    if i != 0:
                        ans += 2
                    meet1 = True
                else:
                    ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def numSteps(self, s: str) -> int:
        chars = list(s)
        ans = 0
        while len(chars) > 1:
            if chars[-1] == "0":
                chars.pop()
            else:
                for i in range(len(chars) - 1, -1, -1):
                    if chars[i] == "1":
                        chars[i] = "0"
                    else:
                        chars[i] = "1"
                        break
                if i == 0:
                    chars.insert(0, "1")
            ans += 1
        if chars[0] == "0":
            ans += 1
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(s="1101"), 6],
    [dict(s="10"), 1],
    [dict(s="1"), 0],
])
def test_solutions(kw, expected):
    assert Solution().numSteps(**kw) == expected
    assert Solution1().numSteps(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
