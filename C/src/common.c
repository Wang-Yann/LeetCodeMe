//
/* Created by rock on 5/16/20.
*/
#include "common.h"

ListNode *initNodeList(int *nums, int size) {
    struct ListNode *dummy, *cur;
    dummy = (ListNode *) malloc(sizeof(ListNode));
    dummy->next = NULL;
    cur = dummy;
    for (int i = 0; i < size; ++i) {
        ListNode *p = (ListNode *) malloc(sizeof(ListNode));
        p->val = *(nums + i);
        cur->next = p;
        cur = p;
    }
    return dummy->next;

};
bool checkListEqual(ListNode *res, ListNode *expected){
    while (expected != NULL && res != NULL) {
        if (res->val != expected->val){
            return false;
        }
        res = res->next;
        expected = expected->next;
    }
    if (res == NULL && expected == NULL){
        return true;
    }
    return false;



};

bool checkTreeEqual(TreeNode *rootA, TreeNode *rootB){
    if (rootA == NULL && rootB == NULL) {
        return true;
    }
    if (rootA == NULL || rootB == NULL) {
        return false;
    }
    return rootA->val == rootB->val && checkTreeEqual(rootA->left, rootB->left) &&
           checkTreeEqual(rootA->right, rootB->right);

};
