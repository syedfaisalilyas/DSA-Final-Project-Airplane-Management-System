# def startsWith( input_list, first_substring):
#     result = []
#     # Iterate through the list
#     for item in input_list:
#         # Check if the first part of the item matches the provided first_substring
#         if item.startswith(first_substring):
#             result.append(item)
#     print("HELLO")
#     return result
#
#
# def endWith( input_list, end_substring):
#     result = []
#     # Iterate through the list
#     for item in input_list:
#         # Check if the item ends with the provided end_substring
#         if item.endswith(end_substring):
#             result.append(item)
#     return result
#
#
# def contains(input_list, substring):
#     result = []
#     # Iterate through the list
#     for item in input_list:
#         # Iterate through the item string
#         for i in range(len(item) - len(substring) + 1):
#             # Check if the substring is present at the current position
#             if item[i:i + len(substring)] == substring:
#                 result.append(item)
#                 break  # Break to avoid duplicates
#
#     return result

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_bst(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    elif value > root.value:
        root.right = insert_bst(root.right, value)
    return root

def startsWith_BST(root, first_substring):
    result = []

    def traverse(node):
        if node:
            # Check if the current node's value starts with the provided first_substring
            if node.value.startswith(first_substring):
                result.append(node.value)
            # Recursively traverse the left and right subtrees
            traverse(node.left)
            traverse(node.right)

    # Start the traversal from the root of the BST
    traverse(root)
    # print("HELLO")
    return result

def endWith_BST(root, end_substring):
    result = []

    def traverse(node):
        if node:
            # Check if the current node's value ends with the provided end_substring
            if node.value.endswith(end_substring):
                result.append(node.value)
            # Recursively traverse the left and right subtrees
            traverse(node.left)
            traverse(node.right)

    # Start the traversal from the root of the BST
    traverse(root)
    return result
def contains_BST(root, substring):
    result = []

    def traverse(node):
        if node:
            # Check if the current node's value contains the provided substring
            if substring in node.value:
                result.append(node.value)
            # Recursively traverse the left and right subtrees
            traverse(node.left)
            traverse(node.right)

    # Start the traversal from the root of the BST
    traverse(root)
    return result

def bst_intersection(node, bst2, result):
    if node:
        if bst2.search(node.value):
            result.append(node.value)
        bst_intersection(node.left, bst2, result)
        bst_intersection(node.right, bst2, result)

def bst_union(node, bst2, result):
    if node:
        result.append(node.value)
        bst_union(node.left, bst2, result)
        bst_union(node.right, bst2, result)

    bst2_elements = []
    bst2.traverse_inorder(bst2.root, bst2_elements)
    for element in bst2_elements:
        if element not in result:
            result.append(element)

def bst_negation(node, bst2, result):
    if node:
        if not bst2.search(node.value):
            result.append(node.value)
        bst_negation(node.left, bst2, result)
        bst_negation(node.right, bst2, result)