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
    print(node.data, end="-")
    inorder_traversal(node.right)

print("*******INORDER TRAVERSAL***********")
inorder_traversal(newNode)
print()
print("*********************************")

def preorder_traversal(node):
    if not node:
        return
    print(node.data, end="->")
    preorder_traversal(node.left)
    preorder_traversal(node.right)
print("----------POSTORDER------------------")
preorder_traversal(newNode)
print()
print("*********************************")


def postorder_traversal(node):
    if not node:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data)

print("*********************************")
postorder_traversal(newNode)