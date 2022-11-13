class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        self.nums.sort()
        middle = len(self.nums) // 2
        if len(self.nums) % 2 == 1:
            median = self.nums[middle] * 1.0
        else:
            median = (self.nums[middle] + self.nums[middle-1]) / 2
        return median
        
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



