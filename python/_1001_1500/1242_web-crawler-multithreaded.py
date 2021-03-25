#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 17:17:17
# @Last Modified : 2020-08-09 17:17:17
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个初始地址 startUrl 和一个 HTML 解析器接口 HtmlParser，请你实现一个 多线程的网页爬虫，用于获取与 startUrl 有 相
# 同主机名 的所有链接。 
# 
#  以 任意 顺序返回爬虫获取的路径。 
# 
#  爬虫应该遵循： 
# 
#  
#  从 startUrl 开始 
#  调用 HtmlParser.getUrls(url) 从指定网页路径获得的所有路径。 
#  不要抓取相同的链接两次。 
#  仅浏览与 startUrl 相同主机名 的链接。 
#  
# 
#  
# 
#  如上图所示，主机名是 example.org 。简单起见，你可以假设所有链接都采用 http 协议，并且没有指定 端口号。举个例子，链接 http://l
# eetcode.com/problems 和链接 http://leetcode.com/contest 属于同一个 主机名， 而 http://example
# .org/test 与 http://example.com/abc 并不属于同一个 主机名。 
# 
#  HtmlParser 的接口定义如下： 
# 
#  
# interface HtmlParser {
#   // Return a list of all urls from a webpage of given url.
#   // This is a blocking call, that means it will do HTTP request and return wh
# en this request is finished.
#   public List<String> getUrls(String url);
# } 
# 
#  注意一点，getUrls(String url) 模拟执行一个HTTP的请求。 你可以将它当做一个阻塞式的方法，直到请求结束。 getUrls(Strin
# g url) 保证会在 15ms 内返回所有的路径。 单线程的方案会超过时间限制，你能用多线程方案做的更好吗？ 
# 
#  对于问题所需的功能，下面提供了两个例子。为了方便自定义测试，你可以声明三个变量 urls，edges 和 startUrl。但要注意你只能在代码中访问 s
# tartUrl，并不能直接访问 urls 和 edges。 
# 
#  
# 
#  拓展问题： 
# 
#  
#  假设我们要要抓取 10000 个节点和 10 亿个路径。并且在每个节点部署相同的的软件。软件可以发现所有的节点。我们必须尽可能减少机器之间的通讯，并确保每
# 个节点负载均衡。你将如何设计这个网页爬虫？ 
#  如果有一个节点发生故障不工作该怎么办？ 
#  如何确认爬虫任务已经完成？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：
# urls = [
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.google.com",
#   "http://news.yahoo.com/us"
# ]
# edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
# startUrl = "http://news.yahoo.com/news/topics/"
# 输出：[
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.yahoo.com/us"
# ]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：
# urls = [
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.google.com"
# ]
# edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
# startUrl = "http://news.google.com"
# 输出：["http://news.google.com"]
# 解释：startUrl 链接与其他页面不共享一个主机名。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= urls.length <= 1000 
#  1 <= urls[i].length <= 300 
#  startUrl 是 urls 中的一个。 
#  主机名的长度必须为 1 到 63 个字符（包括点 . 在内），只能包含从 “a” 到 “z” 的 ASCII 字母和 “0” 到 “9” 的数字，以及中划
# 线 “-”。 
#  主机名开头和结尾不能是中划线 “-”。 
#  参考资料：https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_hostnames 
#  你可以假设路径都是不重复的。 
#  
#  Related Topics 深度优先搜索 广度优先搜索 
#  👍 12 👎 0
	 

"""

import collections
from typing import List

import pytest


class HtmlParser(object):

    def getUrls(self, url):

        idx = urls.index(url)
        if idx == -1:
            return []
        neighbors = [t for f, t in edges if f == idx]
        return [urls[i] for i in neighbors]


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
import threading
from urllib import parse
import queue


class Solution:
    NUMBER_OF_WORKERS = 8

    def __init__(self):
        self.__cv = threading.Condition()
        self.__q = collections.deque()
        self.__working_count = 0

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def hostname(url):
            domain_parts = parse.urlparse(url)
            return "{}://{}".format(domain_parts.scheme, domain_parts.netloc)

        def worker(htmlParser, lookup):
            while True:
                from_url = self.__q.get()
                if from_url is None:
                    break
                name = hostname(from_url)
                for to_url in htmlParser.getUrls(from_url):
                    if name != hostname(to_url):
                        continue
                    with self.__cv:
                        if to_url not in lookup:
                            lookup.add(to_url)
                            self.__q.put(to_url)
                self.__q.task_done()

        workers = []
        self.__q = queue.Queue()
        self.__q.put(startUrl)
        lookup = {startUrl}
        for i in range(self.NUMBER_OF_WORKERS):
            t = threading.Thread(target=worker, args=(htmlParser, lookup))
            t.start()
            workers.append(t)
        self.__q.join()
        for t in workers:
            self.__q.put(None)
        for t in workers:
            t.join()
        return list(lookup)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        urls=[
            "http://news.yahoo.com",
            "http://news.yahoo.com/news",
            "http://news.yahoo.com/news/topics/",
            "http://news.google.com",
            "http://news.yahoo.com/us"
        ],
        edges=[[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]],
        startUrl="http://news.yahoo.com/news/topics/"

    ),
        [
            "http://news.yahoo.com",
            "http://news.yahoo.com/news",
            "http://news.yahoo.com/news/topics/",
            "http://news.yahoo.com/us"
        ]
    ],
    [dict(
        urls=[
            "http://news.yahoo.com",
            "http://news.yahoo.com/news",
            "http://news.yahoo.com/news/topics/",
            "http://news.google.com"
        ],
        edges=[[0, 2], [2, 1], [3, 2], [3, 1], [3, 0]],
        startUrl="http://news.google.com"

    ),
        ["http://news.google.com"]
    ],

])
def test_solutions(kw, expected):
    global urls, edges
    urls = kw.pop("urls")
    edges = kw.pop("edges")
    kw["htmlParser"] = HtmlParser()
    ans = Solution().crawl(**kw)
    print(ans)
    assert ans == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
