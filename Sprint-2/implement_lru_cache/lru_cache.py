class Node:
    __slots__ = ("key", "value", "next", "previous")

    # Create a building block for the cache
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    # Manages node ordering (head, tail, pushing, removing, and moving to head)
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
        return node

    def remove(self, node):
        if self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None
        elif node == self.tail:
            self.tail = self.tail.previous
            if self.tail is not None:
                self.tail.next = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous

        node.next = None
        node.previous = None

    def pop_tail(self):
        if self.tail is None:
            return None
        tail_node = self.tail
        self.remove(tail_node)
        return tail_node

    def move_to_head(self, node):
        if self.head == node:
            return
        self.remove(node)
        self.push_head(node)


class LruCache:
    # Initializes the cache with a maximum capacity
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Cache limit must be greater than zero.")
        self.limit = limit
        self.cache = {}  # Maps key -> Node for O(1) lookups
        self.order_list = DoublyLinkedList()  # Manages LRU order

    # Looks up a value and marks it as recently used
    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]
        self.order_list.move_to_head(node)
        return node.value

    # Add or update an item, evicting the oldest if full
    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.order_list.move_to_head(node)
            return

        if len(self.cache) >= self.limit:
            evicted_node = self.order_list.pop_tail()
            if evicted_node is not None:
                del self.cache[evicted_node.key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.order_list.push_head(new_node)
