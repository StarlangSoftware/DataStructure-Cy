import unittest
from random import randrange

from DataStructure.CounterHashMap import CounterHashMap


class MyTestCase(unittest.TestCase):

    def test_Put1(self):
        
        counterHashMap = CounterHashMap()
        counterHashMap.put("item1")
        counterHashMap.put("item2")
        counterHashMap.put("item3")
        counterHashMap.put("item1")
        counterHashMap.put("item2")
        counterHashMap.put("item1")
        self.assertEqual(3, counterHashMap.count("item1"))
        self.assertEqual(2, counterHashMap.count("item2"))
        self.assertEqual(1, counterHashMap.count("item3"))

    def test_Put2(self):
        counterHashMap = CounterHashMap()
        for i in range(1000):
            counterHashMap.put(randrange(1000))
        count = 0
        for i in range(1000):
            count += counterHashMap.count(i)
        self.assertEqual(1000, count)

    def test_SumOfCounts(self):
        counterHashMap = CounterHashMap()
        for i in range(1000):
            counterHashMap.put(randrange(1000))
        self.assertEqual(1000, counterHashMap.sumOfCounts())

    def test_Put3(self):
        counterHashMap = CounterHashMap()
        for i in range(1000000):
            counterHashMap.put(randrange(1000000))
        self.assertAlmostEqual(len(counterHashMap) / 1000000.0, 0.632, 3)

    def test_PutNTimes1(self):
        counterHashMap = CounterHashMap()
        counterHashMap.putNTimes("item1", 2)
        counterHashMap.putNTimes("item2", 3)
        counterHashMap.putNTimes("item3", 6)
        counterHashMap.putNTimes("item1", 2)
        counterHashMap.putNTimes("item2", 3)
        counterHashMap.putNTimes("item1", 2)
        self.assertEqual(6, counterHashMap.count("item1"))
        self.assertEqual(6, counterHashMap.count("item2"))
        self.assertEqual(6, counterHashMap.count("item3"))

    def test_PutNTimes2(self):
        counterHashMap = CounterHashMap()
        for i in range(1000):
            counterHashMap.putNTimes(randrange(1000), i + 1)
        self.assertEqual(500500, counterHashMap.sumOfCounts())

    def test_Max(self):
        counterHashMap = CounterHashMap()
        counterHashMap.put("item1")
        counterHashMap.put("item2")
        counterHashMap.put("item3")
        counterHashMap.put("item1")
        counterHashMap.put("item2")
        counterHashMap.put("item1")
        self.assertEqual("item1", counterHashMap.maxItem())

    def test_MaxThreshold1(self):
        counterHashMap = CounterHashMap()
        counterHashMap.put("item1")
        counterHashMap.put("item2")
        counterHashMap.put("item3")
        counterHashMap.put("item1")
        counterHashMap.put("item2")
        counterHashMap.put("item1")
        self.assertEqual("item1", counterHashMap.maxItem(0.4999))
        self.assertNotEqual("item1", counterHashMap.maxItem(0.5001))

    def test_MaxThreshold2(self):
        counterHashMap = CounterHashMap()
        for i in range(1000000):
            counterHashMap.put(randrange(100).__str__())
        probability = counterHashMap.count(counterHashMap.maxItem()) / 1000000.0
        self.assertIsNotNone(counterHashMap.maxItem(probability - 0.001))
        self.assertIsNone(counterHashMap.maxItem(probability + 0.001))

    def test_Add1(self):
        counterHashMap1 = CounterHashMap()
        counterHashMap1.put("item1")
        counterHashMap1.put("item2")
        counterHashMap1.put("item3")
        counterHashMap1.put("item1")
        counterHashMap1.put("item2")
        counterHashMap1.put("item1")
        counterHashMap2 = CounterHashMap()
        counterHashMap2.putNTimes("item1", 2)
        counterHashMap2.putNTimes("item2", 3)
        counterHashMap2.putNTimes("item3", 6)
        counterHashMap2.putNTimes("item1", 2)
        counterHashMap2.putNTimes("item2", 3)
        counterHashMap2.putNTimes("item1", 2)
        counterHashMap1.add(counterHashMap2)
        self.assertEqual(9, counterHashMap1.count("item1"))
        self.assertEqual(8, counterHashMap1.count("item2"))
        self.assertEqual(7, counterHashMap1.count("item3"))

    def test_Add2(self):
        counterHashMap1 = CounterHashMap()
        counterHashMap1.put("item1")
        counterHashMap1.put("item2")
        counterHashMap1.put("item1")
        counterHashMap1.put("item2")
        counterHashMap1.put("item1")
        counterHashMap2 = CounterHashMap()
        counterHashMap2.put("item4")
        counterHashMap2.putNTimes("item5", 4)
        counterHashMap2.put("item2")
        counterHashMap1.add(counterHashMap2)
        self.assertEqual(3, counterHashMap1.count("item1"))
        self.assertEqual(3, counterHashMap1.count("item2"))
        self.assertEqual(1, counterHashMap1.count("item4"))
        self.assertEqual(4, counterHashMap1.count("item5"))

    def test_Add3(self):
        counterHashMap1 = CounterHashMap()
        for i in range(1000):
            counterHashMap1.put(i)
        counterHashMap2 = CounterHashMap()
        for i in range(500, 1000):
            counterHashMap2.putNTimes(1000 + i, i + 1)
        counterHashMap1.add(counterHashMap2)
        self.assertEqual(1500, len(counterHashMap1))

    def test_TopN1(self):
        counterHashMap = CounterHashMap()
        counterHashMap.put("item1")
        counterHashMap.put("item2")
        counterHashMap.put("item3")
        counterHashMap.put("item1")
        counterHashMap.put("item2")
        counterHashMap.put("item1")
        self.assertEqual("item1", counterHashMap.topN(1)[0][1])
        self.assertEqual("item2", counterHashMap.topN(2)[1][1])
        self.assertEqual("item3", counterHashMap.topN(3)[2][1])

    def test_TopN2(self):
        counterHashMap = CounterHashMap()
        for i in range(1000):
            counterHashMap.putNTimes(i, 2 * i + 2)
        self.assertEqual(990, counterHashMap.topN(10)[9][1])
        self.assertEqual(900, counterHashMap.topN(100)[99][1])


if __name__ == '__main__':
    unittest.main()
