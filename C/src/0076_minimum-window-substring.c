//
/* Created by rock on 5/2/20.
*/
#include "leetcode_functions.h"

//https://leetcode-cn.com/problems/minimum-window-substring/solution/shuang-100-cyu-yan-hua-dong-chuang-kou-by-xiao-xi-/


char *minWindow(char *s, char *t) {

    if (s == NULL || t == NULL) {
        return NULL;
    }
    int lens = (int) strlen(s);
    int lent = (int) strlen(t);
    char *out = (char *) malloc(lens + 1);
    if (out == NULL) {
        return NULL;
    }
    int outLen = 0;
    memset(out, 0, lens + 1);
    if (lens < lent || lent == 0) {
        return out;
    }
    int map_s[128] = {0};
    int map_t[128] = {0};
    int cnt = 0;
    for (int i = 0; i < lent; ++i) {
        map_t[t[i]]++;
        map_s[s[i]]++;
    }
    for (int i = 0; i < 128; ++i) {
        if (map_t[i] > 0) {
            /* 临界点，只要 <= 短串 就是有效计数, 再大就是多余的了 */
            cnt += min(map_t[i], map_s[i]);
        }

    }

    /* 2. 当计数等于短串长度就是满足条件了 */
    if (cnt == lent) {
        outLen = lent;
        memcpy(out, s, outLen);
        return out;
    }
    /* 3. 滑动窗口 */
    int l = 0;
    int r = lent;

    for (; r < lens; r++) {
        if (map_t[s[r]] == 0) {
            continue;
        }
        map_s[s[r]]++;
        if (map_s[s[r]] <= map_t[s[r]]) {
            /* 临界点，只要 <= 短串 就是有效计数, 再大就是多余的了 */

            cnt++;
        }
        if (cnt == lent) {
            /* 从左侧开始校验 找到临界点（map[s[l]] == mapt[s[l]]）删除多余数据 */
            while (map_t[s[l]] == 0 || map_s[s[l]] > map_t[s[l]]) {
                map_s[s[l++]]--;
            }
            int cpLen = r - l + 1;
            if (outLen == 0 || cpLen < outLen) {
                memset(out, 0, lens + 1);
                memcpy(out, s + l, cpLen);
                outLen = cpLen;
            }
            /* 临界点 */

            cnt--;
            map_s[s[l++]]--;

        }


    }
    return out;


}