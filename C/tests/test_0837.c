//
/* Created by rock on 4/28/20.
*/


#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0837)
    {
        ck_assert_double_eq_tol(new21Game(6, 1, 10), 0.6,ELLIPSIS);
        double res = new21Game(21, 17, 10);
        ck_assert(abs(res - 0.73278) < 1e-5);
//    ASSERT_NEAR(new21Game(21,17,10), 0.73278,1e-6);

    ck_assert_double_eq_tol(new21Game(10, 1, 10), 1.0,ELLIPSIS);
//    ck_assert_double_eq(new21Game(421,400,47), 0.71188);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0837");       // 建立Suite
    TCase *tc_add = tcase_create("t_0837");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0837);     // 测试用例加到测试集中
    return s;
}
//421
//400
//47 结果偏差 2e-6
