#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 02:19:16
# @Last Modified : 2020-08-09 02:19:16
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。 
# 
#  「超赞子字符串」需满足满足下述两个条件： 
# 
#  
#  该字符串是 s 的一个非空子字符串 
#  进行任意次数的字符交换重新排序后，该字符串可以变成一个回文字符串 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "3242415"
# 输出：5
# 解释："24241" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "24142"
#  
# 
#  示例 2： 
# 
#  输入：s = "12345678"
# 输出：1
#  
# 
#  示例 3： 
# 
#  输入：s = "213123"
# 输出：6
# 解释："213123" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "231132"
#  
# 
#  示例 4： 
# 
#  输入：s = "00"
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  s 仅由数字组成 
#  
#  Related Topics 位运算 字符串 
#  👍 1 👎 0
	 

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def longestAwesome(self, s: str) -> int:
        """
       看别人
       用10个bit表示从字符串开头到当前字符中，数量为奇数的数字；最多有1024个状态，记录状态的最左下标；
       对于当前下标i的状态，需要找之前是否有某个下标j能使得(j...i]形成回文串
       status&(1<<i)表示i出现的奇偶
       """
        status, res = 0, 0
        dic = {0: -1}
        for i in range(len(s)):
            status ^= (1 << int(s[i]))
            # //一个数字出现奇数次，其余出现偶数次
            for j in range(10):
                if status ^ (1 << j) in dic:
                    res = max(res, i - dic[status ^ (1 << j)])
            # //所有都出现了偶数次
            if status in dic:
                res = max(res, i - dic[status])
            else:
                dic[status] = i
        # print({bin(k)[2:]:v for k,v in  dic.items()})
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(s="3242415"), 5],

    pytest.param(dict(s="12345678"), 1),
    pytest.param(dict(s="213123"), 6),
    pytest.param(dict(s="00"), 2),
])
def test_solutions5471(kwargs, expected):
    assert Solution().longestAwesome(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
