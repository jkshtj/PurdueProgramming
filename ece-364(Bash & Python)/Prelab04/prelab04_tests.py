import sys
import unittest
import dataStructs

class Prelab04TestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.wordFrequencyDict = dataStructs.getWordFrequency()
        cls.duplicateFilesDict = dataStructs.getDuplicates()
        cls.purchaseDict = dataStructs.getPurchaseReport()
        cls.totalSoldDict = dataStructs.getTotalSold()


    def test_checkPythonVersion(self):

        currentVersion = sys.version_info

        self.assertGreaterEqual(currentVersion, (3, 4))


    def test_getWordFrequency(self):

        key, value = 'Pellentesque', 153

        expectedValue = value
        actualValue = self.wordFrequencyDict[key]

        self.assertEqual(expectedValue, actualValue)


    def test_getDuplicates(self):

        key, value = '1WS', (40, ['1WS', 'BWO', 'S68', 'YX5'])

        expectedValue = value
        actualValue = self.duplicateFilesDict[key]

        self.assertEqual(expectedValue, actualValue)


    def test_getPurchaseReport(self):

        key, value = 7, 393.34

        expectedValue = value
        actualValue = self.purchaseDict[key]

        self.assertEqual(expectedValue, actualValue)


    def test_getTotalSold(self):

        key, value = 'Nectarines', 49

        expectedValue = value
        actualValue = self.totalSoldDict[key]

        self.assertEqual(expectedValue, actualValue)

    def test_getWordFrequency2(self):

        key, value = 'Vestibulum', 163

        expectedValue = value
        actualValue = self.wordFrequencyDict[key]

        self.assertEqual(expectedValue, actualValue)


    def test_getDuplicates2(self):

        key, value = 'HOS', (68, ['HOS', 'LMY', 'Q39'])

        expectedValue = value
        actualValue = self.duplicateFilesDict[key]

        self.assertEqual(expectedValue, actualValue)


    def test_getPurchaseReport2(self):

        key, value = 3, 310.38

        expectedValue = value
        actualValue = self.purchaseDict[key]

        self.assertEqual(expectedValue, actualValue)


    def test_getTotalSold2(self):

        key, value = 'Asparagus', 37

        expectedValue = value
        actualValue = self.totalSoldDict[key]

        self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()

