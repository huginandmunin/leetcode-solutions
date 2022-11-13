from p295_find_median_from_data_stream import MedianFinder

def test_solution1():
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    expected = 1.5
    assert abs(obj.findMedian()-expected) <= 0.00001

def test_solution2():
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    obj.addNum(2)
    expected = 2.0
    assert abs(obj.findMedian()-expected) <= 0.00001
