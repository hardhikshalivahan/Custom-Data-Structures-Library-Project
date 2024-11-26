from stack import Stack
from queue import Queue
from linked_list import LinkedList
from graph import Graph
from bst import BinarySearchTree

# Stack
stack = Stack()
stack.push(10)
stack.push(20)
print("Stack Top:", stack.peek())
stack.pop()
print("Stack Size:", stack.size())

# Queue
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print("Queue Front:", queue.peek())
queue.dequeue()
print("Queue Size:", queue.size())

# Linked List
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.display()
linked_list.delete(10)
linked_list.display()

# Graph
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_edge("A", "B")
graph.display()

# Binary Search Tree
bst = BinarySearchTree()
bst.insert(15)
bst.insert(10)
bst.insert(20)
print("BST Inorder Traversal:")
bst.inorder()
