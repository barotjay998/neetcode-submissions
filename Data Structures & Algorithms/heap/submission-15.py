class MinHeap:
    
    def __init__(self):
        # Heap empty is an array with single dummy value
        self.heap = [0]
        

    def push(self, val: int) -> None:
        """ Pushes the value on to the heap """
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i // 2] > self.heap[i]:
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i = i // 2

    def pop(self) -> int:
        """ Removed the top element min from the heap """
        if len(self.heap) == 1:
            return -1
        
        elif len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1

        while i * 2 < len(self.heap):
            if (i * 2 + 1 < len(self.heap) and
                self.heap[i * 2] > self.heap[i * 2 + 1] and
                self.heap[i] > self.heap[i * 2 + 1]):
                # Swap i (curr node) with right child (i * 2 + 1)
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                i = i * 2 + 1
            
            elif self.heap[i] > self.heap[i * 2]:
                # Swap i (curr node) with left child (i * 2)
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = i * 2
            
            else:
                # No swapping needed stop
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
            


    
        
        