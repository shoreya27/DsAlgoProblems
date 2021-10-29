class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

newNode = TreeNode("drinks")
print(newNode)
left_child = TreeNode("Hot")
right_child = TreeNode("Cold")
newNode.left = left_child
newNode.right = right_child

tea = TreeNode("tea")
coffee = TreeNode("coffee")
left_child.left = tea
left_child.right = coffee

shake = TreeNode("shake")
right_child.left = shake

def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node.data)
    inorder_traversal(node.right)

inorder_traversal(newNode)

def preorder_traversal(node):
    if not node:
        return
    print(node.data)
    preorder_traversal(node.left)
    preorder_traversal(node.right)

# preorder_traversal(newNode)