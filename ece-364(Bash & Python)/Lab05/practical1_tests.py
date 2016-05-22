import sys
import unittest
from practical1 import *


class Practical1TestSuite(unittest.TestCase):

    def test_checkPythonVersion(self):

        currentVersion = sys.version_info
        self.assertGreaterEqual(currentVersion, (3, 4))

    def test_rowSumIsValid(self):

        with self.subTest(key="Bad Row Sum"):
            actualValue = rowSumIsValid(square4)
            self.assertFalse(actualValue)

        with self.subTest(key="Good Row Sum"):
            actualValue = rowSumIsValid(square6)
            self.assertTrue(actualValue)

    def test_columnSumIsValid(self):

        with self.subTest(key="Bad Column Sum"):
            actualValue = columnSumIsValid(square6)
            self.assertFalse(actualValue)

        with self.subTest(key="Good Column Sum"):
            actualValue = columnSumIsValid(square4)
            self.assertTrue(actualValue)

    def test_magicSquareIsValid(self):

        with self.subTest(key="Bad Square"):
            actualValue = magicSquareIsValid("Squares/magic6.txt")
            self.assertFalse(actualValue)

        with self.subTest(key="Good Square"):
            actualValue = magicSquareIsValid("Squares/magic7.txt")
            self.assertTrue(actualValue)

    def test_getTotalCost(self):

        with self.subTest(key="Set 1"):
            itemSet = {('Intel i7-4960HQ', 9), ('Intel i7-6700HQ', 7), ('Intel i7-6970HQ', 3)}
            expectedValue = {'WalMart': 20552.43, 'NewEgg': 22059.9, 'Amazon': 13163.15,
                             'TigerDirect': 18395.45, 'Jet': 15224.04}
            actualValue = getTotalCost(itemSet)

            self.assertDictEqual(actualValue, expectedValue)

        with self.subTest(key="Set 2"):
            itemSet = {('Intel i7-4702HQ', 8), ('Intel i7-4710MQ', 9), ('Intel i7-4700EC', 9), ('Intel i7-6600U', 7)}
            expectedValue = {'WalMart': 28481.39, 'NewEgg': 28714.53, 'Amazon': 28098.6,
                             'TigerDirect': 37168.32, 'Jet': 30924.9}
            actualValue = getTotalCost(itemSet)

            self.assertDictEqual(actualValue, expectedValue)

        with self.subTest(key="Set 3"):
            itemSet = {('Intel i7-6567U', 10)}
            expectedValue = {'WalMart': 9241.7, 'NewEgg': 10910.7, 'Amazon': 11018.8,
                             'TigerDirect': 11471.3, 'Jet': 10738.9}
            actualValue = getTotalCost(itemSet)

            self.assertDictEqual(actualValue, expectedValue)

        with self.subTest(key="Set 4"):
            itemSet = {('Intel i7-5700HQ', 5), ('Intel i7-6650U', 2), ('Intel i7-4860HQ', 5), ('Intel i7-4800MQ', 7)}
            expectedValue = {'WalMart': 18697.83, 'NewEgg': 13727.64, 'Amazon': 22721.03,
                             'TigerDirect': 21537.87, 'Jet': 25596.04}
            actualValue = getTotalCost(itemSet)

            self.assertDictEqual(actualValue, expectedValue)

    def test_getBestPrices(self):

        with self.subTest(key="Set 1"):
            cpuSet = {'Intel i7-5950HQ', 'Intel i7-4700HQ', 'Intel i7-4702EC', 'Intel i7-4702MQ', 'Intel i7-6770HQ'}
            expectedValue = {'Intel i7-4700HQ': (801.98, 'TigerDirect'),
                             'Intel i7-4702EC': (1202.88, 'NewEgg'),
                             'Intel i7-4702MQ': (779.67, 'NewEgg'),
                             'Intel i7-5950HQ': (626.66, 'Jet'),
                             'Intel i7-6770HQ': (1293.09, 'NewEgg')}
            actualValue = getBestPrices(cpuSet)

            self.assertDictEqual(actualValue, expectedValue)

        with self.subTest(key="Set 2"):
            cpuSet = {'Intel i7-6970HQ', 'Intel i7-6700TE', 'Intel i7-4860HQ', 'Intel i7-4870HQ', 'Intel i7-6700K'}
            expectedValue = {'Intel i7-4860HQ': (523.55, 'TigerDirect'),
                             'Intel i7-4870HQ': (644.27, 'Amazon'),
                             'Intel i7-6700K': (662.91, 'TigerDirect'),
                             'Intel i7-6700TE': (698.31, 'TigerDirect'),
                             'Intel i7-6970HQ': (511.96, 'Jet')}
            actualValue = getBestPrices(cpuSet)

            self.assertDictEqual(actualValue, expectedValue)

        with self.subTest(key="Set 3"):
            cpuSet = {'Intel i7-4702HQ', 'Intel i7-6700', 'Intel i7-5500U', 'Intel i7-4710MQ', 'Intel i7-4700EQ'}
            expectedValue = {'Intel i7-4700EQ': (807.31, 'NewEgg'),
                             'Intel i7-4702HQ': (520.35, 'Jet'),
                             'Intel i7-4710MQ': (765.3, 'Amazon'),
                             'Intel i7-5500U': (565.45, 'NewEgg'),
                             'Intel i7-6700': (635.08, 'Amazon')}
            actualValue = getBestPrices(cpuSet)

            self.assertDictEqual(actualValue, expectedValue)

    def test_getMissingItems(self):

        missingDictionary = getMissingItems()

        with self.subTest(key="General Check"):
            keysAreOK = missingDictionary.keys() == {'WalMart', 'Jet', 'TigerDirect', 'Amazon', 'NewEgg'}
            valueCountIsOK = all([len(value) == 10 for value in missingDictionary.values()])

            self.assertTrue(keysAreOK and valueCountIsOK)

        with self.subTest(key="Amazon"):
            expectedValue = {'Intel i7-6920HQ', 'Intel i7-5775C', 'Intel i7-4900MQ', 'Intel i7-6560U',
                              'Intel i7-4700EQ', 'Intel i7-6500U', 'Intel i7-4700HQ', 'Intel i7-4980HQ',
                              'Intel i7-4910MQ', 'Intel i7-5500U'}
            actualValue = missingDictionary["Amazon"]

            self.assertSetEqual(actualValue, expectedValue)

        with self.subTest(key="Jet"):
            expectedValue = {'Intel i7-6770HQ', 'Intel i7-6920HQ', 'Intel i7-6700', 'Intel i7-4900MQ',
                             'Intel i7-5650U', 'Intel i7-6700T', 'Intel i7-6560U', 'Intel i7-4700HQ',
                             'Intel i7-5750HQ', 'Intel i7-6700TE'}
            actualValue = missingDictionary["Jet"]

            self.assertSetEqual(actualValue, expectedValue)

        with self.subTest(key="TigerDirect"):
            expectedValue = {'Intel i7-6822EQ', 'Intel i7-5775C', 'Intel i7-5650U', 'Intel i7-6700T',
                             'Intel i7-4702MQ', 'Intel i7-6500U', 'Intel i7-4702EC', 'Intel i7-4980HQ',
                             'Intel i7-6820HK', 'Intel i7-4950HQ'}
            actualValue = missingDictionary["TigerDirect"]

            self.assertSetEqual(actualValue, expectedValue)


square4 = [[16, 2, 3, 13],
           [5, 11, 10, 1],
           [9, 7, 6, 12],
           [4, 14, 15, 8]]

square6 = [[35, 1, 6, 26, 19, 24],
           [3, 25, 7, 21, 23, 32],
           [31, 9, 2, 22, 27, 20],
           [8, 28, 33, 17, 10, 15],
           [30, 5, 34, 12, 14, 16],
           [4, 36, 29, 13, 18, 11]]


if __name__ == '__main__':
    unittest.main()
