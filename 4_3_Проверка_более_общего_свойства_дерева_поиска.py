import sys

sys.setrecursionlimit(10**6) # Set the recursion limit to a high value to avoid the RecursionError

# Reading input
n = int(input())
keys = []
left = []
right = []
if n == 0:
    print("CORRECT")
else:
    for i in range(n):
        a, b, c = map(int, input().split())
        keys.append(a)
        left.append(b)
        right.append(c)

    # Checking if the tree is a valid binary search tree
    prev = float('-inf') # Initializing prev with negative infinity
    def inOrder(node):
        global prev
        if node == -1:
            return
        if left[node] != -1 and keys[left[node]] == keys[node]:
            print("INCORRECT")
            exit()
        inOrder(left[node])
        if keys[node] < prev:
            print("INCORRECT")
            exit()
        prev = keys[node]
        inOrder(right[node])

    inOrder(0) # Starting with the root node
    print("CORRECT")
