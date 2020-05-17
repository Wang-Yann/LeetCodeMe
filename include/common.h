#pragma  once
#ifndef LEETCODE_COMMON_H
#define LEETCODE_COMMON_H

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdarg.h>
#include <assert.h>
#include <ctype.h>
#include <time.h>
#include <float.h>
#include <errno.h>
#include <limits.h>


#define max(a, b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a > _b ? _a : _b; });


#define min(a, b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a < _b ? _a : _b; })

#define MIN(a, b, c) ((a)<(b)?( (a)<(c)?(a):(c) ):( (b)<(c)?(b):(c) ))



typedef struct ListNode ListNode;
typedef struct TreeNode TreeNode;
typedef struct Queue Queue;

struct ListNode {
    int val;
    struct ListNode *next;
};


#define INIT    (-1)
#define VOS_OK  0
#define VOS_NOK (-1)
struct Queue{
    int head;
    int tail;
    int size;
    int *queue;
};

ListNode *initNodeList(int *nums, int size);

bool checkListEqual(ListNode *res, ListNode *expected);


struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};


#endif //LEETCODE_COMMON_H
