//
/* Created by rock on 6/8/20.
*/
#include "leetcode_functions.h"

#define MaxSize 26
struct SetType {
    int Data;
    int Parent;
};

typedef struct SetType SetType;

int Find(SetType S[], int X) {
    int i;
    for ( i = 0; i < MaxSize && S[i].Data != X; i++);
    if (i >= MaxSize) {
        return -1;
    }
    while (S[i].Parent >= 0) {
        i = S[i].Parent;
    }
    return i;

}

void Union(SetType S[], int X1, int X2) {
    int root1, root2;
    root1 = Find(S, X1);
    root2 = Find(S, X2);
    if (root1 != root2) {
        S[root2].Parent = root1;
    }

}

bool equationsPossible(char **equations, int equationsSize) {
    SetType *S = (SetType *) calloc(MaxSize, sizeof(SetType));
    for (int i = 0; i < MaxSize; ++i) {
        S[i].Data = i;
        S[i].Parent = -(i + 1);
    }
    for (int i = 0; i < equationsSize; ++i) {
        if (equations[i][1] == '=') {
            Union(S, equations[i][0] - 'a', equations[i][3] - 'a');
        }
    }
    for (int i = 0; i < equationsSize; ++i) {
        if (equations[i][1] == '!') {
            int pos1 = Find(S, equations[i][0] - 'a');
            int pos2 = Find(S, equations[i][3] - 'a');
            if (pos1 == pos2) {
                return false;
            }
        }
    }
    free(S);
    return true;

}