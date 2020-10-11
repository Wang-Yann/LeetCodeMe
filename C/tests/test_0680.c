//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0680)
    {
        char s1[] = "abcd";
        char s2[] = "abb";
        char * s3 = "deeee";
        char s4[] = "eeccccbebaeeabebccceea";
        ck_assert(!validPalindrome(s1));
        ck_assert(!validPalindrome(s4));
        ck_assert(validPalindrome(s2));
        ck_assert(validPalindrome(s3));
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0680");       // 建立Suite
    TCase *tc_add = tcase_create("t_0680");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0680);     // 测试用例加到测试集中
    return s;
}
