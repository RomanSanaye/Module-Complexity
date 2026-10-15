from typing import Any, Optional
# A "Node" is a single building block of our list.
# Each node holds a value and two pointers: 'next' (forward) and 'previous' (backward).
class Node:
    __slots__ = ("value", "next", "previous")
    def __init__(self, value: Any)-> None:
        self.value: Any = value
        self.next: Optional[Node] = None
        self.previous: Optional[Node] = None


# A Doubly Linked List keeps track of both ends (head and tail).
class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def push_head(self, value: Any):
        """Add a new item to the front of the list in O(1) time."""
        new_node = Node(value)

        # If the list is empty, head and tail both point to this new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Connect the new node to the current head
            new_node.next = self.head
            self.head.previous = new_node
            # Update the head pointer to be our new node
            self.head = new_node

        # We return the node itself so it can be used as a "handle" later
        return new_node

    def pop_tail(self) -> Any:
        """Remove and return the item from the end of the list in O(1) time."""
        # If the list is empty, there is nothing to remove
        if self.tail is None:
            return None

        # Save the value so we can return it at the end
        removed_value = self.tail.value

        # Delegate the actual removal logic to the general remove() method (DRY principle)
        self.remove(self.tail)

        return removed_value

    def remove(self, node: Node) -> None :
        """Remove a specific node from the list using its reference in O(1) time."""

        # Scenario 1: It's the only item in the list
        if self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None

        # Scenario 2: It's the first item (head)
        elif node == self.head:
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None

        # Scenario 3: It's the last item (tail)
        elif node == self.tail:
            self.tail = self.tail.previous
            if self.tail is not None:
                self.tail.next = None

        # Scenario 4: It's somewhere safely in the middle
        else:
            # Bypass the node by gluing its neighbors directly to each other
            node.previous.next = node.next
            node.next.previous = node.previous

        # Clean up the node's own pointers
        node.next = None
        node.previous = None
