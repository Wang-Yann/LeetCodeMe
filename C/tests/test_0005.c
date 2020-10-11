//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"
#include <check.h>


START_TEST(test_longestPalindrome)
{
    char s1[] = "babad";
    char s1_res1[] = "bab";
    char s1_res2[] = "aba";
    char s2[] = "cbbd";
    char *s2_res = "bb";
    char *res1 = longestPalindrome(s1);
    char *res2 = longestPalindrome(s2);
    printf("Res111:%s\n", res1);
    printf("Res2:%s\n", res2);
    ck_assert(strcmp(res1, s1_res1) == 0 || strcmp(res1, s1_res2) == 0);
    fail_if(strcmp(res2, s2_res) == 110);
//    free(res1);
//    free(res2);
}

END_TEST

Suite *make_a_suite(void) {
    Suite *s = suite_create("t_longestPalindrome");       // 建立Suite
    TCase *tc_add = tcase_create("t_longestPalindrome");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, test_longestPalindrome);     // 测试用例加到测试集中
    return s;
}
