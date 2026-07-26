class LLNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,key,value):
        newNode = LLNode(key,value)
        newNode.next = self.head
        self.head = newNode

    def search(self,key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        return None

    def delete(self,key):
        curr = self.head
        prev = None
        while curr:
            if curr.key == key:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

class MyHashMap:

    def __init__(self):
        self.capacity = 1000
        self.size = 0
        self.buckets = self.__CreateBuckets(self.capacity)

    def __CreateBuckets(self,capacity):
        return [LinkedList() for _ in range(capacity)]

    def Hash(self,key):
        return abs(hash(key)) % self.capacity

    def Rehash(self):
        oldBuckets = self.buckets
        self.capacity = self.capacity * 2
        self.size = 0
        self.buckets = self.__CreateBuckets(self.capacity)
        for eachLLHead in oldBuckets:
            curr = eachLLHead.head
            while curr:
                self.put(curr.key,curr.value)
                curr = curr.next

    def put(self, key: int, value: int) -> None:
        bucketIndex = self.Hash(key)
        bucket = self.buckets[bucketIndex]
        node = bucket.search(key)
        if node is None:
            bucket.add(key,value)
            self.size += 1
        else:
            node.value = value
        loadFactor = self.size/self.capacity
        if loadFactor > 0.75:
            self.Rehash()

    def get(self, key: int) -> int:
        bucketIndex = self.Hash(key)
        bucket = self.buckets[bucketIndex]
        node = bucket.search(key)
        if node is not None:
            return node.value
        return -1
            

    def remove(self, key: int) -> None:
        bucketindex = self.Hash(key)
        bucket = self.buckets[bucketindex]
        removed = bucket.delete(key)
        if removed == True:
            self.size -= 1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)