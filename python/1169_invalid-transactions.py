#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 如果出现下述两种情况，交易 可能无效： 
# 
#  
#  交易金额超过 ¥1000 
#  或者，它和另一个城市中同名的另一笔交易相隔不超过 60 分钟（包含 60 分钟整） 
#  
# 
#  每个交易字符串 transactions[i] 由一些用逗号分隔的值组成，这些值分别表示交易的名称，时间（以分钟计），金额以及城市。 
# 
#  给你一份交易清单 transactions，返回可能无效的交易列表。你可以按任何顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  输入：transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# 输出：["alice,20,800,mtv","alice,50,100,beijing"]
# 解释：第一笔交易是无效的，因为第二笔交易和它间隔不超过 60 分钟、名称相同且发生在不同的城市。同样，第二笔交易也是无效的。 
# 
#  示例 2： 
# 
#  输入：transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# 输出：["alice,50,1200,mtv"]
#  
# 
#  示例 3： 
# 
#  输入：transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
# 输出：["bob,50,1200,mtv"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  transactions.length <= 1000 
#  每笔交易 transactions[i] 按 "{name},{time},{amount},{city}" 的格式进行记录 
#  每个交易名称 {name} 和城市 {city} 都由小写英文字母组成，长度在 1 到 10 之间 
#  每个交易时间 {time} 由一些数字组成，表示一个 0 到 1000 之间的整数 
#  每笔交易金额 {amount} 由一些数字组成，表示一个 0 到 2000 之间的整数 
#  
#  Related Topics 数组 字符串

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def invalidTransactions(self, transactions):
        Transaction = collections.namedtuple("Transaction", "name,time,amount,city")
        res = set()
        new_transactions = []
        for s in transactions:
            name, t, amount, city = s.split(",")
            new_transactions.append(Transaction(name, int(t), int(amount), city))
        new_transactions.sort(key=lambda t: t.time)  # O(nlogn) time

        for i in range(len(new_transactions)):  # O(n^2) time
            t1 = new_transactions[i]
            if t1.amount > 1000:
                res.add("{},{},{},{}".format(t1.name, t1.time, t1.amount, t1.city))
            for j in range(i + 1, len(new_transactions)):
                t2 = new_transactions[j]
                if t2.name == t1.name and t2.time - t1.time <= 60 and t2.city != t1.city:
                    res.add("{},{},{},{}".format(t1.name, t1.time, t1.amount, t1.city))
                    res.add("{},{},{},{}".format(t2.name, t2.time, t2.amount, t2.city))

        res = list(res)  # O(n) time
        return res


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """一点不美观"""
        transactions_list = collections.defaultdict(list)
        ans = []
        for idx, s in enumerate(transactions):
            name, t, amount, city = s.split(",")
            transactions_list[name].append((int(t), city, int(amount), idx))
        for name, vs in transactions_list.items():
            l = len(vs)
            vs.sort()
            invalid = set()
            for i in range(0, l):
                t, city, amount, idx = vs[i]
                if amount > 1000:
                    invalid.add(idx)
                if i == 0:
                    continue
                for j in range(i - 1, -1, -1):
                    t1, city1, amount1, idx1 = vs[j]
                    if abs(t - t1) > 60:
                        break
                    elif city != city1 and abs(t1 - t) <= 60:
                        invalid.add(idx)
                        invalid.add(idx1)
            for idx in invalid:
                ans.append(transactions[idx])
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(transactions=["alice,20,800,mtv", "alice,50,100,beijing"]), ["alice,20,800,mtv", "alice,50,100,beijing"]],
    [dict(transactions=["alice,20,800,mtv", "alice,50,1200,mtv"]), ["alice,50,1200,mtv"]],
    [dict(transactions=["alice,20,800,mtv", "bob,50,1200,mtv"]), ["bob,50,1200,mtv"]],
    [dict(transactions=["bob,689,1910,barcelona", "alex,696,122,bangkok",
                        "bob,832,1726,barcelona", "bob,820,596,bangkok",
                        "chalicefy,217,669,barcelona", "bob,175,221,amsterdam"]),
     ["bob,689,1910,barcelona", "bob,832,1726,barcelona", "bob,820,596,bangkok"]],
])
def test_solutions(kw, expected):
    assert sorted(Solution().invalidTransactions(**kw)) == sorted(expected)
    assert sorted(Solution1().invalidTransactions(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
