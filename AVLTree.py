class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if not node:
        return 0
    return node.height

def update_height(node):
    if not node:
        return 0
    node.height = 1 + max(height(node.left), height(node.right))
    return node.height

def balance_factor(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    update_height(y)
    update_height(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    update_height(x)
    update_height(y)

    return y

def insert_avl(root, value):
    if not root:
        return AVLNode(value)

    if value < root.value:
        root.left = insert_avl(root.left, value)
    elif value > root.value:
        root.right = insert_avl(root.right, value)
    else:
        return root  # Duplicate values are not allowed

    update_height(root)

    balance = balance_factor(root)

    # Left Heavy
    if balance > 1:
        # Left Right Case
        if value > root.left.value:
            root.left = rotate_left(root.left)
        return rotate_right(root)

    # Right Heavy
    if balance < -1:
        # Right Left Case
        if value < root.right.value:
            root.right = rotate_right(root.right)
        return rotate_left(root)

    return root

def startsWith_AVL(root, first_substring):
    result = []

    def traverse(node):
        if node:
            # Check if the current node's value starts with the provided first_substring
            if node.value.startswith(first_substring):
                result.append(node.value)
            # Recursively traverse the left and right subtrees
            traverse(node.left)
            traverse(node.right)

    # Start the traversal from the root of the AVL tree
    traverse(root)
    print("HELLO")
    return result

def endWith_AVL(root, end_substring):
    result = []

    def traverse(node):
        if node:
            # Check if the current node's value ends with the provided end_substring
            if node.value.endswith(end_substring):
                result.append(node.value)
            # Recursively traverse the left and right subtrees
            traverse(node.left)
            traverse(node.right)

    # Start the traversal from the root of the AVL tree
    traverse(root)
    return result
def contains_AVL(root, substring):
    result = []

    def traverse(node):
        if node:
            # Iterate through the node's value string
            for i in range(len(node.value) - len(substring) + 1):
                # Check if the substring is present at the current position
                if node.value[i:i + len(substring)] == substring:
                    result.append(node.value)
                    break  # Break to avoid duplicates

            # Recursively traverse the left and right subtrees
            traverse(node.left)
            traverse(node.right)

    # Start the traversal from the root of the AVL tree
    traverse(root)
    return result