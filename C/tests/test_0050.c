//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_myPow)
    {
        int res = myPow(2.0,10);
        ck_assert_uint_eq(res, 1024.00000);
        ck_assert_double_eq_tol(myPow(2.10000,3), 9.26100,ELLIPSIS);
        ck_assert_double_eq_tol(myPow(2.00000, -2), 0.25000,ELLIPSIS);
        ck_assert_double_eq_tol(myPow(1.00000, -2147483648), 1,ELLIPSIS);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_myPow");       // 建立Suite
    TCase *tc_add = tcase_create("t_myPow");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_myPow);     // 测试用例加到测试集中
    return s;
}
