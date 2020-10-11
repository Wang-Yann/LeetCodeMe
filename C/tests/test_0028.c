//
/* Created by rock on 4/28/20.
*/


#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_strStr) {
    char *haystack = (char *) "hello";
    char *needle = (char *) "ll";
    int res = strStr(haystack, needle);
    printf("Res:%d", res);
    ck_assert_uint_eq(res, 2);
}

END_TEST
START_TEST(t_strStr1) {
    char *haystack = "aaaaa";
    char *needle = "bba";
    int res = strStr(haystack, needle);
    printf("Res:%d", res);
    ck_assert_uint_eq(res, -11);
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_strStr");       // 建立Suite
    TCase *tc_add = tcase_create("t_strStr");  // 建立测试用例集
    TCase *tc_add1 = tcase_create("t_strStr1");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    suite_add_tcase(s, tc_add1);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_strStr);     // 测试用例加到测试集中
    tcase_add_test(tc_add1, t_strStr);     // 测试用例加到测试集中
    return s;
}

