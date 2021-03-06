//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_mySqrt)
    {
        int n = 4;
        int res = mySqrt(n);
        ck_assert_uint_eq(res, 2);
    }

END_TEST

START_TEST(t_mySqrt1)
    {
        int n = 4;
        int res = mySqrt(n);
        ck_assert_uint_eq(res, 21);
    }

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_mySqrt");       // 建立Suite
    TCase *tc_add = tcase_create("t_mySqrt");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_mySqrt);     // 测试用例加到测试集中
    tcase_add_test(tc_add, t_mySqrt1);     // 测试用例加到测试集中
    return s;
}
