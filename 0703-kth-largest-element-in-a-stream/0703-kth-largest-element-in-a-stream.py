class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap) #convert array minHeap into heap

        # If the heap is larger than k, remove the smallest elements until it has exactly k elements
        while len(self.minHeap)>k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)

         # If after adding the new value, the heap has more than k elements, pop the smallest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # The smallest element in the heap is now the k-th largest element
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)