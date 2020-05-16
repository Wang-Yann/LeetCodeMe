//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(reverseKGroup, test1) {
    int n = 2;
    struct ListNode nodes[5];
    int i;
    int nums[5] = {1, 2, 3, 4, 5};
    int resNums[5] = {2, 1, 4, 3, 5};
    ListNode *head = initNodeList(nums, 5);
    ListNode *expected = initNodeList(resNums, 5);
    ListNode *res = reverseKGroup(head, n);
    ASSERT_TRUE(checkListEqual(res, expected));

}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
