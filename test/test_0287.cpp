//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(findDuplicate, test1) {
    int nums[] = {1,3,4,2,2};
    int result = findDuplicate(nums, sizeof(nums) / sizeof(int));

    ASSERT_EQ(2, result);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
