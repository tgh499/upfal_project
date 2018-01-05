#!/usr/bin/env python

# refer to upfal mitzenmacher "Probability and Computing" 5.8. An Exploratory
# Assignment. 

import math
import random
import numpy as np

# mark nodes upwards
def markItUp(a, tree):
    tree[a] = 1
    # if a is a left node
    if a % 2 == 0:
        # if sibling is 1
        if tree[a+1] == 1 and tree[a/2] != 1:
            tree[a/2] = 1
            markItUp((a/2), tree)
            #markItDown((a/2), tree)

        # if parent is 1
        if tree[a/2] == 1 and tree[a+1] != 1:
            tree[a+1] = 1
            markItDown((a+1), tree)
        markItDown(a, tree)
    # if a is right node
    else:
        if a == 1:
            markItDown(a, tree)
        else:
            # if sibling is 1
            if tree[a-1] == 1 and tree[(a-1)/2] != 1:
                tree[(a-1)/2] = 1
                markItUp(((a-1)/2), tree)
                #markItDown(((a-1)/2), tree)
            # if parent is 1
            if tree[(a-1)/2] == 1 and tree[a-1] != 1:
                tree[a-1] = 1
                markItDown((a-1), tree)
            markItDown(a,tree)

# mark nodes downwards
def markItDown(a, tree):
    tree[a] = 1
    if (a)< ((len(tree))/2):
        # left child
        if tree[2*a] == 1 and tree[2*a + 1] != 1:
            tree[2*a + 1] = 1
            markItDown((2*a + 1), tree)
        # right child
        if tree[2*a +1] == 1 and tree[2*a] != 1:
            tree[2*a] = 1
            markItDown(2*a, tree)
    else:
        if a % 2 ==0:
            if tree[a/2] == 1 and tree[a+1] != 1:
                tree[a+1] = 1
            if tree[a+1] == 1 and tree[a/2] != 1:
                tree[a/2] = 1
                markItUp(a/2, tree)
        else:
            if tree[(a-1)/2] == 1 and tree[a-1] != 1:
                tree[a-1] = 1
            if tree[a-1] == 1 and tree[(a-1)/2] != 1:
                tree[(a-1)/2] =1
                markItUp(((a-1)/2), tree)




# choose height of the binary tree
n = 11

lenN = math.pow(2,n) - 1
lenN = int(lenN)

# use this list to identify nodes of the binary tree; starts with 1
N = list(range(1, lenN+1))

#consider 0 as unmarked, and 1 as marked
tree = {}
for i in N:
    tree[i] = 0


count = 0
NodesSent = []
MarkedNodes = []


# the loop continues until all nodes have been marked as 1
while (sum(tree.values()) != len(N)):

    '''
    ### Process 1
    a = random.choice(N)
    markItUp(a, tree)
    count += 1
    '''

    '''
    ### Process 2
    a = random.choice(N)
    if a not in NodesSent:
        markItUp(a, tree)
        NodesSent.append(a)
        count += 1


    '''

    ### Process 3

    a = random.choice(N)
    if a not in MarkedNodes:

        markItUp(a, tree)
        count += 1
    for i in tree.keys():
        if tree[i] == 1:
            MarkedNodes.append(i)

#print(tree)
print(count)
