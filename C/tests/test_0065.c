//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_isNumber)
    {
        char s1[]= " -90e3   ";
        char s2[]= "e3";
        char s3[] = "53.5e93";
        char s4[] = "95a54e53";
        char s5[] = "99e2.5 ";
        ck_assert_uint_eq(isNumber(s1), true);
        ck_assert_uint_eq(isNumber(s2), false);
        ck_assert_uint_eq(isNumber(s3), true);
        ck_assert_uint_eq(isNumber(s4), false);
        ck_assert_uint_eq(isNumber(s5), false);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_isNumber");       // 建立Suite
    TCase *tc_add = tcase_create("t_isNumber");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_isNumber);     // 测试用例加到测试集中
    return s;
}

