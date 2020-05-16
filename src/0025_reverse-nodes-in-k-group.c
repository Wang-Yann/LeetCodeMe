//
/* Created by rock on 5/16/20.
*/

#include "leetcode_functions.h"
struct ListNode* reverseKGroup(struct ListNode* head, int k){
    struct ListNode* tmp=head,*keep;
    int counter = k;
    while (counter--) {
        if (tmp == NULL) {
            return head;
        }
        tmp = tmp->next;
    }
    counter = k;
    tmp = head;
    while (--counter) {
        keep = tmp->next;
        tmp->next = keep->next;
        keep->next = head;
        head = keep;
    }
    tmp->next = reverseKGroup(tmp->next, k);
    return head;



}