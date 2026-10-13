class Node:
    # Create a building block for the cache
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LruCache:
    # Initializes the cache with a maximum capacity
    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("Cache limit must be greater than zero.")
        self.limit = limit
        self.cache = {}  # Maps key -> Node for O(1) lookups
        self.head = None  # Most recently used
        self.tail = None  # Least recently used

    # Looks up a value and marks it as recently used
    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    # Add or update an item, evicting the oldest if full
    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
            return

        if len(self.cache) >= self.limit:
            if self.tail is not None:
                del self.cache[self.tail.key]
                
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.previous
                    self.tail.next = None

        new_node = Node(key, value)
        self.cache[key] = new_node

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    # Internal helper to reposition a used node to the front
    def _move_to_head(self, node):
        if self.head == node:
            return

        if node == self.tail:
            self.tail = node.previous
            self.tail.next = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous

        node.next = self.head
        self.head.previous = node
        node.previous = None
        self.head = node