//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(longestCommonPrefix, test1) {
    char *s1 = (char *) "flower";
    char *s2 = (char *)"flow";
    char *s3 = (char *)"flight";
//    char* matrix[] = {s1, s2, s3};
    char *matrix[] = {"flower","flow","flight"};
    char expected[] = "fl";
    char * res = longestCommonPrefix(matrix, 3);
//    printf("Res:%s\n", *res);
    ASSERT_TRUE(strcmp(expected,res)==0);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
