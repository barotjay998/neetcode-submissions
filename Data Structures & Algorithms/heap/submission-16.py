class MinHeap:
    
    def __init__(self):
        """
        InIt a heap, heap is implemented using arrays, 
        it is visualized as a complete Binary Tree with (Structure Property)
        parent at index i//2, left child at i*2 and right at i*2+1
        Every descendant is greater than parent (Order Property)
        To make the index jump math work, we do not use the 0th index of the array
        """
        self.heap = [0] # Empty hash is an array with single dummy value.
        

    def push(self, val: int) -> None:
        """ 
        Description: Pushes the value on to the heap.
        Method: Add to bottom (end of array), Structure property maintained.
        and percolate up, Order property maintained.
        """
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i // 2] > self.heap[i]:
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i = i // 2

    def pop(self) -> int:
        """
        Description: Removes the top root (min) from the heap.
        Method: Replace the top root with last value (Structure Property maintained)
        and percolate down (Order property maintained)
        """
        if len(self.heap) == 1:
            return -1
        
        elif len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1

        # Till there is a left child
        while i * 2 < len(self.heap):
            # Right child smaller than root & Left child
            if (i * 2 + 1 < len(self.heap) and
                self.heap[i * 2] > self.heap[i * 2 + 1] and
                self.heap[i] > self.heap[i * 2 + 1]):
                # Swap i (curr node) with right child (i * 2 + 1)
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                i = i * 2 + 1
            
            # Left child is smaller
            elif self.heap[i] > self.heap[i * 2]:
                # Swap i (curr node) with left child (i * 2)
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = i * 2
            
            # No swapping needed stop
            else:
                break

        return res


    def top(self) -> int:
        if len(self.heap) > 1:
            return self.heap[1]
        return -1
        

    def heapify(self, nums: List[int]) -> None:
        if len(nums) < 1:
            return 
        
        if len(nums) == 1:
            self.heap = [0]
            self.heap.append(nums[0])
            return 
            
        self.heap = nums
        self.heap.append(nums[0])

        # For half of the nodes (since only they have children) percolate down.
        curr = (len(self.heap) - 1) // 2

        while curr > 0:
            i = curr

            while i * 2 < len(self.heap):
                if (i*2+1 < len(self.heap) and
                    self.heap[i*2+1] < self.heap[i*2] and
                    self.heap[i] > self.heap[i*2+1]):
                    self.heap[i*2+1], self.heap[i] = self.heap[i], self.heap[i*2+1]
                    i = i*2+1
                
                elif self.heap[i] > self.heap[i*2]:
                    self.heap[i], self.heap[i*2] = self.heap[i*2], self.heap[i]
                    i = i*2
                
                else:
                    break
            
            curr -= 1
            


    
        
        