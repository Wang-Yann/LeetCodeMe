//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(tt_isValid)
    {
        char s1[]= "()[]{}";
        char s2[]= "(]";
        char s3[] = "()";
        char s4[] = "([)]";
        char s5[] = "(]";
        ck_assert_uint_eq(isValid(s1), true);
        ck_assert_uint_eq(isValid(s2), false);
        ck_assert_uint_eq(isValid(s3), true);
        ck_assert_uint_eq(isValid(s4), false);
        ck_assert_uint_eq(isValid(s5), false);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("tt_isValid");       // 建立Suite
    TCase *tc_add = tcase_create("tt_isValid");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, tt_isValid);     // 测试用例加到测试集中
    return s;
}
