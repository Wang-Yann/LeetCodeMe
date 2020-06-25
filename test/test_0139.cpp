//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(wordBreak, test1) {
    char s1[] = "leetcode";
    char *wordDict1[] = {"leet", "code"};
    bool result1 = wordBreak(s1, wordDict1,
                             sizeof(wordDict1) / sizeof(char *));
    ASSERT_TRUE(result1);

}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
