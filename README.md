# -Doubly-Linked-List-Implementation-in-Python
This repository contains a Python implementation of a Doubly Linked List with basic operations.

## Features

- **Append**: Add a new node at the end of the list.
- **Prepend**: Add a new node at the beginning of the list.
- **Insert After**: Insert a new node after a specific node in the list.
- **Delete First**: Delete the first node in the list.
- **Delete After**: Delete the node after a specific node in the list.
- **Delete Last**: Delete the last node in the list.
- **Delete by Value**: Delete the first occurrence of a node with a specific value.

## Usage

```python
# Example Usage
from doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)

dll.display()  # Display the list
dll.prepend(0)
dll.display()  # Display the list after prepend
dll.insert_after(1, 1.5)
dll.display()  # Display the list after insert_after

# Perform other operations...

dll.delete_first()
dll.display()  # Display the list after delete_first
dll.delete_after(dll.head)
dll.display()  # Display the list after delete_after
dll.delete_last()
dll.display()  # Display the list after delete_last
