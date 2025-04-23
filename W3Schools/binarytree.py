class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    
root = TreeNode("R")
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right= nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.right = nodeG

# print("root.right.left.data:", root.right.left.data)

# DFS: Pre-order Traversal
def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)
        
print("Pre-order Traversal", preOrderTraversal(root))

print(" ")

# DFS: In-order Traversal
def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)
    
print("Pre-order Traversal", inOrderTraversal(root))

print(" ")

# DFS: Post-order Traversal
def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")
    
print("Post-order Traversal", postOrderTraversal(root))