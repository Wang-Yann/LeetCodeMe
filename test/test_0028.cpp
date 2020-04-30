//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(strStrTest, test) {
    char * haystack = (char *)"hello";
    char *  needle =  (char *)"ll";
    int res = strStr(haystack, needle);
    printf("Res:%d", res);
    ASSERT_EQ(res, 2);
}



TEST(strStrTest1, test2) {
    char * haystack = "aaaaa";
    char * needle = "bba";
    int res = strStr(haystack, needle);
    printf("Res:%d", res);
    ASSERT_EQ(res, -1);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}