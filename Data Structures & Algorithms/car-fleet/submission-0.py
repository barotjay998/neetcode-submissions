class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars.sort()
        print(cars)

        stack = []
        for c, s in cars:
            time2target = (target - c) / s
            while stack and stack[-1] <= time2target:
                stack.pop()

            stack.append(time2target)
        
        print(stack)
        return len(stack)
