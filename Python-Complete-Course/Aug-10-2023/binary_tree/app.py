from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(11))
tree.add(Node(515))


# left =  Node(5)
# head = Node(9)
# right = Node(13)

# head.left = left
# head.right = right 

print(tree.head)
print(tree.head.left)
print(tree.head.right)
print(tree.head.right.right)

tree.inorder()
