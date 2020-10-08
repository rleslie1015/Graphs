from collections import deque
"""
U given an adjacency list and an int represting a family member find their earliest ancestor 
    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''
    input :  
        test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)] 
        family id = 1
    output :
        10
P 
    initialize visited as a set sets dont allow dupes
    visited = set()
    initialize a stack
    add the starting node to stack
    while len of stack > 0
        currentNode = stack.pop
        if currentNode not in visited:
            add to visited



ER
"""
def earliest_ancestor(ancestors, starting_node):
    visited = set()
    stack = deque()
    stack.append(starting_node)
    while len(stack) > 0:
        currNode = stack.pop
        if currNode[0] not in visited:
            visited.add(currNode[0])
            stack.append(currNode[1])
            # visited.add(currNode[0])
            # print(currNode)

            for neighbor in ancestors:
                if neighbor[0] not in visited:
                    stack.append(neighbor[1])
            #     if neighbor[1] == starting_node:
            #         return neighbor[0] 
             
            #     if neighbor[0] == currNode:
            #         stack.append(neighbor[0])
                    # return neighbor[0]
    return -1
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)] 
family_id = 3

print(earliest_ancestor(test_ancestors, family_id))