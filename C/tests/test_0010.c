//
/* Created by rock on 4/28/20.
*/


#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_isMatch)
    {
        char s1[]= "mississippi";
        char p1[]= "mis*is*p*.";
        ck_assert_uint_eq(isMatch(s1,p1), false);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_isMatch");       // 建立Suite
    TCase *tc_add = tcase_create("t_isMatch");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_isMatch);     // 测试用例加到测试集中
    return s;
}

