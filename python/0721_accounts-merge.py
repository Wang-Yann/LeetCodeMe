#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其
# 余元素是 emails 表示该帐户的邮箱地址。 
# 
#  现在，我们想合并这些帐户。如果两个帐户都有一些共同的邮件地址，则两个帐户必定属于同一个人。请注意，即使两个帐户具有相同的名称，它们也可能属于不同的人，因为
# 人们可能具有相同的名称。一个人最初可以拥有任意数量的帐户，但其所有帐户都具有相同的名称。 
# 
#  合并帐户后，按以下格式返回帐户：每个帐户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。accounts 本身可以以任意顺序返回。 
# 
#  例子 1: 
# 
#  
# Input: 
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnn
# ybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Ma
# ry", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.
# com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation: 
#   第一个和第三个 John 是同一个人，因为他们有共同的电子邮件 "johnsmith@mail.com"。 
#   第二个 John 和 Mary 是不同的人，因为他们的电子邮件地址没有被其他帐户使用。
#   我们可以以任何顺序返回这些列表，例如答案[['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com'
# ]，
#   ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']]仍然会被
# 接受。
# 
#  
# 
#  注意： 
# 
#  
#  accounts的长度将在[1，1000]的范围内。 
#  accounts[i]的长度将在[1，10]的范围内。 
#  accounts[i][j]的长度将在[1，30]的范围内。 
#  
#  Related Topics 深度优先搜索 并查集

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):
    def __init__(self):
        self.set = list(range(10001))

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root != y_root:
            self.set[min(x_root, y_root)] = max(x_root, y_root)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email]=name
                if email not in em_to_id:
                    em_to_id[email]=i
                    i+=1
                uf.union_set(em_to_id[acc[1]],em_to_id[email])
        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[uf.find_set(em_to_id[email])].append(email)
        print(ans)
        return [[em_to_name[v[0]]]+sorted(v) for v in ans.values()]
            
            




# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (
            [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
             ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]],
            [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
             ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
    )
])
def test_solutions(args, expected):
    assert sorted(Solution().accountsMerge(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
