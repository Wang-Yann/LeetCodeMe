#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 15:45:22
# @Last Modified : 2020-07-10 15:45:22
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你有一个只支持单个标签页的 浏览器 ，最开始你浏览的网页是 homepage ，你可以访问其他的网站 url ，也可以在浏览历史中后退 steps 步或前进
#  steps 步。 
# 
#  请你实现 BrowserHistory 类： 
# 
#  
#  BrowserHistory(string homepage) ，用 homepage 初始化浏览器类。 
#  void visit(string url) 从当前页跳转访问 url 对应的页面 。执行此操作会把浏览历史前进的记录全部删除。 
#  string back(int steps) 在浏览历史中后退 steps 步。如果你只能在浏览历史中后退至多 x 步且 steps > x ，那么你只后
# 退 x 步。请返回后退 至多 steps 步以后的 url 。 
#  string forward(int steps) 在浏览历史中前进 steps 步。如果你只能在浏览历史中前进至多 x 步且 steps > x ，那么
# 你只前进 x 步。请返回前进 至多 steps步以后的 url 。 
#  
# 
#  
# 
#  示例： 
# 
#  输入：
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","for
# ward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],
# ["linkedin.com"],[2],[2],[7]]
# 输出：
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin
# .com","google.com","leetcode.com"]
# 
# 解释：
# BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
# browserHistory.visit("google.com");       // 你原本在浏览 "leetcode.com" 。访问 "google
# .com"
# browserHistory.visit("facebook.com");     // 你原本在浏览 "google.com" 。访问 "facebook
# .com"
# browserHistory.visit("youtube.com");      // 你原本在浏览 "facebook.com" 。访问 "youtub
# e.com"
# browserHistory.back(1);                   // 你原本在浏览 "youtube.com" ，后退到 "facebo
# ok.com" 并返回 "facebook.com"
# browserHistory.back(1);                   // 你原本在浏览 "facebook.com" ，后退到 "googl
# e.com" 并返回 "google.com"
# browserHistory.forward(1);                // 你原本在浏览 "google.com" ，前进到 "faceboo
# k.com" 并返回 "facebook.com"
# browserHistory.visit("linkedin.com");     // 你原本在浏览 "facebook.com" 。 访问 "linke
# din.com"
# browserHistory.forward(2);                // 你原本在浏览 "linkedin.com" ，你无法前进任何步数。
# 
# browserHistory.back(2);                   // 你原本在浏览 "linkedin.com" ，后退两步依次先到 "
# facebook.com" ，然后到 "google.com" ，并返回 "google.com"
# browserHistory.back(7);                   // 你原本在浏览 "google.com"， 你只能后退一步到 "le
# etcode.com" ，并返回 "leetcode.com"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= homepage.length <= 20 
#  1 <= url.length <= 20 
#  1 <= steps <= 100 
#  homepage 和 url 都只包含 '.' 或者小写英文字母。 
#  最多调用 5000 次 visit， back 和 forward 函数。 
#  
#  Related Topics 设计 
#  👍 13 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class BrowserHistory:
    """AC"""

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.homepage = homepage
        self.cur = 0

    def visit(self, url: str) -> None:
        self.history[self.cur + 1:] = []
        self.history.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        if self.cur - steps >= 0:
            self.cur -= steps
        else:
            self.cur = 0
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        N = len(self.history)
        if self.cur + steps <= N - 1:
            self.cur += steps
        else:
            self.cur = N - 1
        return self.history[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")  # 你原本在浏览 "leetcode.com" 。访问 "google
    browserHistory.visit("facebook.com")  # 你原本在浏览 "google.com" 。访问 "facebook
    browserHistory.visit("youtube.com")  # 你原本在浏览 "facebook.com" 。访问 "youtube
    assert browserHistory.back(1) == "facebook.com"  # 你原本在浏览 "youtube.com" ，后退到 "facebook
    assert browserHistory.back(1) == "google.com"  # 你原本在浏览 "facebook.com" ，后退到 "google
    assert browserHistory.forward(1) == "facebook.com"  # 你原本在浏览 "google.com" ，前进到 "facebook
    browserHistory.visit("linkedin.com")  # 你原本在浏览 "facebook.com" 。 访问 "linkedin
    assert browserHistory.forward(2) == "linkedin.com"  # 你原本在浏览 "linkedin.com" ，你无法前进任何步数。
    assert browserHistory.back(2) == "google.com"  # 你原本在浏览 "linkedin.com" ，后退两步依次先到 " facebook.com" ，然后到 "google.com" ，并返回 "google.com"
    assert browserHistory.back(7) == "leetcode.com"  # 你原本在浏览 "google.com"， 你只能后退一步到 "leetcode.com" ，并返回 "leetcode.com"


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
