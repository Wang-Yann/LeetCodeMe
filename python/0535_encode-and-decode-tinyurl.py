#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 16:25:20
# @Last Modified : 2020-05-05 16:25:20
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时
# ，它将返回一个简化的URL http://tinyurl.com/4e9iAk.
#
#  要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可
# 以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。
#  Related Topics 哈希表 数学
#  👍 81 👎 0

"""
import hmac

import pytest


class Codec:

    def __init__(self):
        self._cache = {}
        self.url = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash_obj = hmac.new(b"secret", longUrl.encode(), digestmod="sha256")
        key = hash_obj.hexdigest()[0:6]
        self._cache[key] = longUrl
        # print(key)
        return self.url + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.replace(self.url, "")
        return self._cache[key]


def test_solution():
    codec = Codec()
    url = "https://leetcode-cn.com/problemset/all/?topicSlugs=math"
    res = codec.decode(codec.encode(url))
    assert res == url


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
