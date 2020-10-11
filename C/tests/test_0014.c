//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_longestCommonPrefix)
    {
        char *s1 = (char *) "flower";
        char *s2 = (char *)"flow";
        char *s3 = (char *)"flight";
//    char* matrix[] = {s1, s2, s3};
        char *matrix[] = {"flower","flow","flight"};
        char expected[] = "fl";
        char * res = longestCommonPrefix(matrix, 3);
//    printf("Res:%s\n", *res);
        ck_assert(strcmp(expected,res)==0);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_longestCommonPrefix");       // 建立Suite
    TCase *tc_add = tcase_create("t_longestCommonPrefix");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_longestCommonPrefix);     // 测试用例加到测试集中
    return s;
}
