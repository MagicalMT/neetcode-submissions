class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.last = None
        self.head = None
    
    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        node = self.d[key]

        if node != self.last:
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next

            if node.next:
                node.next.prev = node.prev

            self.last.next = node
            node.prev = self.last
            node.next = None
            self.last = node

        return node.value

    def put(self, key: int, value: int) -> None:
        curr = Node(key, value)
        if self.head == None:
            self.head = curr    
            self.last = curr
            self.d[key] = curr
            return
        if key in self.d:
            temp = self.d[key]
            temp.value = value
            if temp.prev == None:
                self.head = temp.next
                if temp.next:
                    temp.next.prev = None
                self.last.next = temp
                temp.prev = self.last
                temp.next = None
                self.last = temp
            elif temp.next == None:
                return
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                self.last.next = temp
                temp.prev = self.last
                temp.next = None
                self.last = temp      
        else:
            if len(self.d) >= self.capacity:
                node = self.head
                self.head = node.next
                if self.head:
                    self.head.prev = None
                else:
                    self.last = None
                del self.d[node.key]
            if self.last:
                self.last.next = curr
                curr.prev = self.last
            else:
                self.head = curr
            self.last = curr
            self.d[key] = curr


            
