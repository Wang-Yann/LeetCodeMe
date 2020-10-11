//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_isPalindrome)
{
    ck_assert(isPalindrome(121));
    ck_assert(!isPalindrome(123));
    ck_assert(!isPalindrome(-121));
    ck_assert(!isPalindrome(2147483647));
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_isPalindrome");       // 建立Suite
    TCase *tc_add = tcase_create("t_isPalindrome");  // 建立测试用例集
    tcase_add_test(tc_add, t_isPalindrome);     // 测试用例加到测试集中
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    return s;
}

