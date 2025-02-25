class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None # For double linked list

node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

# Signly Linked List
# node1.next = node2
# node2.next = node3
# node3.next = node4

# currentNode = node1

# while currentNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next
    
# print("Null")


# Doubly Linked List
# node1.next = node2

# node2.prev = node1
# node2.next = node3

# node3.prev = node2
# node3.next = node4

# node4.prev = node3

# print("Traversing backward")
# currentNode = node4
# while currentNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.prev

# print("Null")

# Circular Singly Linked List
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node1

# currentNode = node1
# startNode = node1
# print(currentNode.data, end=" -> ") 
# currentNode = currentNode.next 

# while currentNode != startNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next

# print("...")

# Circular Doubly Linked List
# node1.prev = node4
# node1.next = node2

# node2.prev = node1
# node2.next = node3

# node3.prev = node2
# node3.next = node4

# node4.prev = node3
# node4.next = node1

# print("Traversing backward")
# currentNode = node4
# startNode = node4
# print(currentNode.data, end=" -> ")
# currentNode = currentNode.prev

# while currentNode != startNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.prev
    
# print("...")