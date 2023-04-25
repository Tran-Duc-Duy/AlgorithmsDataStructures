from sys import stdin

# Định nghĩa class Vertex để biểu diễn một đỉnh trong cây splay
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        self.key = key
        self.sum = sum
        self.left = left
        self.right = right
        self.parent = parent

# Hàm update để cập nhật giá trị sum của đỉnh
def update(v):
    if v is None:
        return
    v.sum = v.key + (v.left.sum if v.left is not None else 0) + (v.right.sum if v.right is not None else 0)
    if v.left is not None:
        v.left.parent = v
    if v.right is not None:
        v.right.parent = v

# Hàm small_rotation để xoay đơn
def small_rotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = v
        else: 
            grandparent.right = v

# Hàm big_rotation để xoay kép
def big_rotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        small_rotation(v.parent)
        small_rotation(v)    
    else: 
        # Zig-zag
        small_rotation(v)
        small_rotation(v)

# Hàm splay để thực hiện phép splay trên đỉnh v
def splay(v):
    if v is None:
        return None
    while v.parent is not None:
        if v.parent.parent is None:
            small_rotation(v)
            break
        big_rotation(v)
    return v

# Hàm find để tìm kiếm đỉnh có giá trị key trong cây splay
def find(root, key): 
    v = root
    last = root
    next = None
    while v is not None:
        if v.key >= key and (next is None or v.key < next.key):
            next = v    
        last = v
        if v.key == key:
            break    
        if v.key < key:
            v = v.right
        else: 
            v = v.left      
    root = splay(last)
    return (next, root)

# Hàm split để tách cây splay thành 2 cây splay dựa trên giá trị key
def split(root, key):  
    (result, root) = find(root, key)  
    if result is None:    
        return (root, None)  
    right = splay(result)
    left = right.left
    right.left = None
    if left is not None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)

# Hàm merge để gộp 2 cây splay thành 1 cây splay
def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    while right.left is not None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right

root = None

# Hàm insert để chèn một đỉnh mới vào cây splay
def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right is None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)  
    root = merge(merge(left, new_vertex), right)

# Hàm erase để xóa một đỉnh khỏi cây splay
def erase(x): 
    global root
    (left, right) = split(root, x)
    (middle, right) = split(right, x + 1)
    root = merge(left, right)

# Hàm search để tìm kiếm một đỉnh có giá trị key trong cây splay
def search(x): 
    global root
    result, root = find(root, x)
    if result is None or result.key != x:
        return False
    return result.key == x

# Hàm sum để tính tổng các giá trị của các đỉnh trong đoạn [fr, to] của cây splay
def sum(fr, to): 
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    ans = 0
    if middle is None:
        ans = 0
        root = merge(left, right)
    else:
        ans = middle.sum
        root = merge(merge(left, middle), right)
    return ans

ML = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % ML)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % ML)
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % ML) else 'Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % ML, (r + last_sum_result) % ML)
        print(res)
        last_sum_result = res % ML