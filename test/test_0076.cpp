//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(minWindow, test1) {
    char S[] = "ADOBECODEBANC";
    char T[] = "ABC";
    char expect[] = "BANC";
    char *res = minWindow(S, T);
    printf("Res:%12s\n", res);
    ASSERT_TRUE(strcmp(expect, res) == 0);
}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
