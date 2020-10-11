//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_minWindow)
    {
        char S[] = "ADOBECODEBANC";
        char T[] = "ABC";
        char expect[] = "BANC";
        char *res = minWindow(S, T);
        printf("Res:%12s\n", res);
        ck_assert(strcmp(expect, res) == 0);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_minWindow");       // 建立Suite
    TCase *tc_add = tcase_create("t_minWindow");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_minWindow);     // 测试用例加到测试集中
    return s;
}
