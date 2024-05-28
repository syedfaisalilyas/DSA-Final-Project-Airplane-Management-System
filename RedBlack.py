class RBNode:
    def __init__(self, value, color='Red'):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = color  # 'Red' or 'Black'

class RBTree:
    def __init__(self):
        self.NIL = RBNode(value=None, color='Black')  # Sentinel node representing nil (used for leaf nodes)
        self.root = self.NIL

def left_rotate(tree, x):
    y = x.right
    x.right = y.left

    if y.left != tree.NIL:
        y.left.parent = x

    y.parent = x.parent

    if x.parent == tree.NIL:
        tree.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y

def right_rotate(tree, y):
    x = y.left
    y.left = x.right

    if x.right != tree.NIL:
        x.right.parent = y

    x.parent = y.parent

    if y.parent == tree.NIL:
        tree.root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x

    x.right = y
    y.parent = x

def insert_fixup(tree, z):
    while z.parent.color == 'Red':
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y.color == 'Red':
                z.parent.color = 'Black'
                y.color = 'Black'
                z.parent.parent.color = 'Red'
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    left_rotate(tree, z)

                z.parent.color = 'Black'
                z.parent.parent.color = 'Red'
                right_rotate(tree, z.parent.parent)
        else:
            y = z.parent.parent.left
            if y.color == 'Red':
                z.parent.color = 'Black'
                y.color = 'Black'
                z.parent.parent.color = 'Red'
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    right_rotate(tree, z)

                z.parent.color = 'Black'
                z.parent.parent.color = 'Red'
                left_rotate(tree, z.parent.parent)

    tree.root.color = 'Black'

def rb_insert(tree, value):
    z = RBNode(value)
    y = tree.NIL
    x = tree.root

    while x != tree.NIL:
        y = x
        if z.value < x.value:
            x = x.left
        else:
            x = x.right

    z.parent = y

    if y == tree.NIL:
        tree.root = z
    elif z.value < y.value:
        y.left = z
    else:
        y.right = z

    z.left = tree.NIL
    z.right = tree.NIL
    z.color = 'Red'

    insert_fixup(tree, z)

def contains_RB(tree, substring):
    result = []

    def traverse(node):
        if node != tree.NIL:
            # Iterate through the node's value string
            for i in range(len(node.value) - len(substring) + 1):
                # Check if the substring is present at the current position
                if node.value[i:i + len(substring)] == substring:
                    result.append(node.value)
                    break  # Break to avoid duplicates

            # Recursively traverse the left and right subtrees
            traverse(node.left)
            traverse(node.right)

    # Start the traversal from the root of the RB tree
    traverse(tree.root)
    return result

def startsWith_RB(tree, first_substring):
    result = []

    def traverse(node):
        if node != tree.NIL:
            # Check if the current node's value starts with the provided first_substring
            if node.value.startswith(first_substring):
                result.append(node.value)
            # Recursively traverse the left and right subtrees
            traverse(node.left)
            traverse(node.right)

    # Start the traversal from the root of the RB tree
    traverse(tree.root)

    return result
def endWith_RB(tree, end_substring):
    result = []

    def traverse(node):
        if node != tree.NIL:
            # Check if the current node's value ends with the provided end_substring
            if node.value.endswith(end_substring):
                result.append(node.value)
            # Recursively traverse the left and right subtrees
            traverse(node.left)
            traverse(node.right)

    # Start the traversal from the root of the RB tree
    traverse(tree.root)
    return result
