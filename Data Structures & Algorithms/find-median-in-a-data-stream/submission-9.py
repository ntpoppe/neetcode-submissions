class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        print(f"added {num}")

    def findMedian(self) -> float:
        if len(self.arr) % 2 == 0:
            mid = (len(self.arr) - 1) / 2
            print(f"even mid: {mid}")
            upper = self.arr[math.ceil(mid)]
            lower = self.arr[math.floor(mid)]
            print(f"upper: {upper} lower: {lower}")
            return (upper + lower) / 2
        else:
            mid = (len(self.arr) - 1) // 2
            print(f"odd mid: {mid}")
            print(f"from arr: {self.arr[mid]}")
            return self.arr[mid]

        