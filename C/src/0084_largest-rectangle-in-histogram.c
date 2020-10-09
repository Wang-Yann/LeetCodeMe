//
/* Created by rock on 5/14/20.
*/
#include "leetcode_functions.h"
int largestRectangleArea(int* heights, int heightsSize){
    int top = -1;
    int area, i;
    int res = 0;
    int *stack = (int *) malloc(sizeof(int) * (heightsSize + 2));
    int *buf = (int *) malloc(sizeof(int) * (heightsSize + 2));

    //前后加哨兵
    buf[0] = 0;
    for (int i = 1; i < heightsSize+1; ++i) {
        buf[i] = heights[i - 1];
    }
    buf[heightsSize + 1] = 0;
    stack[++top] = 0;
    for (int i = 1; i < heightsSize + 2; ++i) {
        while (top>0  && buf[i]<buf[stack[top]]){
            area = (i - stack[top - 1] - 1) * buf[stack[top]];
            res = res > area ? res : area;
            top--;
        }
        stack[++top] = i;
    }
    return res;


}