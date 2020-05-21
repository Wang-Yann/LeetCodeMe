//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
#include "test_common.cpp"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(longestPalindrome, test1) {
    char s1[]= "babad";
    char s1_res1[]= "bab";
    char s1_res2[]= "aba";
    char s2[] = "cbbd";
    char *s2_res = "bb";
    char *res1 = longestPalindrome(s1);
    char *res2= longestPalindrome(s2);
    printf("Res1:%s\n", res1);
    printf("Res2:%s\n", res2);
    ASSERT_TRUE(strcmp(res1,s1_res1)==0 || strcmp(res1,s1_res2)==0);
    ASSERT_TRUE(strcmp(res2, s2_res)==0);
//    free(res1);
//    free(res2);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}