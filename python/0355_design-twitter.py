#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-13 21:02:00
# @Last Modified : 2020-04-13 21:02:00
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个
# 功能：
#
#
#  postTweet(userId, tweetId): 创建一条新的推文
#  getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
#
#  follow(followerId, followeeId): 关注一个用户
#  unfollow(followerId, followeeId): 取消关注一个用户
#
#
#  示例:
#
#
# Twitter twitter = new Twitter();
#
# // 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
# twitter.postTweet(1, 5);
#
# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# twitter.getNewsFeed(1);
#
# // 用户1关注了用户2.
# twitter.follow(1, 2);
#
# // 用户2发送了一个新推文 (推文id = 6).
# twitter.postTweet(2, 6);
#
# // 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
# // 推文id6应当在推文id5之前，因为它是在5之后发送的.
# twitter.getNewsFeed(1);
#
# // 用户1取消关注了用户2.
# twitter.unfollow(1, 2);
#
# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# // 因为用户1已经不再关注用户2.
# twitter.getNewsFeed(1);
#
#  Related Topics 堆 设计 哈希表
#  👍 144 👎 0

"""

import collections
import heapq
from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # userId-> List[twitterIds]
        self.__user_tweet_map = collections.defaultdict(list)
        # userId-> Set[flowerIds]
        self.__user_followers_map = collections.defaultdict(set)
        # userId-> List[twitterIds]
        self.__time = 0
        self.__cnt_of_recent_tweets = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.__time += 1
        self.__user_tweet_map[userId].append((self.__time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        max_heap = []
        limit = self.__cnt_of_recent_tweets
        if self.__user_tweet_map[userId]:
            for times, t_id in self.__user_tweet_map[userId][-limit:]:
                heapq.heappush(max_heap, (-times, userId, t_id))
        for uid in self.__user_followers_map[userId]:
            if self.__user_tweet_map[uid]:
                for times, t_id in self.__user_tweet_map[uid][-limit:]:
                    heapq.heappush(max_heap, (-times, uid, t_id))
        result = []
        while max_heap and len(result) < limit:
            times, uid, t_id = heapq.heappop(max_heap)
            result.append(t_id)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.__user_followers_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.__user_followers_map[followerId].discard(followeeId)

    def __str__(self) -> str:
        return "Tweeter: {}\nFollows: {}\n".format(
            self.__user_tweet_map,
            self.__user_followers_map,
        )


if __name__ == '__main__':
    twitter = Twitter()
    print(None)
    print(twitter.postTweet(1, 1))
    print(twitter.getNewsFeed(1))
    print(twitter.follow(2, 1))
    # print(twitter)
    print(twitter.getNewsFeed(2))
    print(twitter.unfollow(2, 1))
    print(twitter.getNewsFeed(2))
