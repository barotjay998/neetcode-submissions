class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars.sort()

        fleet = []
        for c, s in cars:
            time2target = (target - c) / s

            # We only keep the leader car in the fleet list
            # we remove all the cars stack behind the leader car.
            while fleet and fleet[-1] <= time2target:
                # We pop all cars taht take less than or equal time to reach 
                # the target from the fleet than the current car, for those 
                # cars, the current car becomes the leader.
                fleet.pop()

            fleet.append(time2target)
        
        return len(fleet)
