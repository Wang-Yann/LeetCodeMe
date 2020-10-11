//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0125)
    {
        char s1[]= "A man, a plan, a canal: Panama ";
        char s2[]= "race a car";
        char s3[]= "0P";
        ck_assert_uint_eq(isPalindrome1(s1), true);
        ck_assert_uint_eq(isPalindrome1(s2), false);
        ck_assert(!isPalindrome1(s3));
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0125");       // 建立Suite
    TCase *tc_add = tcase_create("t_0125");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0125);     // 测试用例加到测试集中
    return s;
}
