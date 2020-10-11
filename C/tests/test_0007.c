//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_twoSum1)
{
//    ck_assert_uint_eq(reverse(123), 321);
//    ck_assert_uint_eq(reverse(-123), -3211);
//    ck_assert_uint_eq(reverse(2147483647), 0);
}

END_TEST

START_TEST(t_twoSum2) {
        assert(1 == 1);


//    ck_assert_int_eq(12,3);
    //    ck_assert_uint_eq(reverse(1200), 21);
//    ck_assert_uint_eq(reverse(120), 21);
//    ck_assert_uint_eq(reverse(10), 0);
    ck_assert_msg(reverse(10)==0,"xXXXXXXXXXXXXXX");
}
END_TEST
START_TEST(t_twoSum3) {
//    ck_assert_uint_eq(reverse(1200), 21);
//    ck_assert_uint_eq(reverse(120), 21);
//    ck_assert_uint_eq(reverse(0), 0);
}
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("2twoSum");       // 建立Suite
    TCase *tc_v1 = tcase_create("t_twoSum1");  // 建立测试用例集
    tcase_add_test(tc_v1, t_twoSum1);     // 测试用例加到测试集中
    suite_add_tcase(s, tc_v1);           // 将测试用例加到Suite中

    TCase *tc_two = tcase_create("t_twoSum2");  // 建立测试用例集
    tcase_add_test(tc_two, t_twoSum2);     // 测试用例加到测试集中
    tcase_add_test(tc_two, t_twoSum3);     // 测试用例加到测试集中
    suite_add_tcase(s, tc_two);           // 将测试用例加到Suite中
    return s;
}

