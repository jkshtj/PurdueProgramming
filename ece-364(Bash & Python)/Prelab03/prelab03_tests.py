import sys
import unittest
import basicOps

class Prelab03TestSuite(unittest.TestCase):

    def test_checkPythonVersion(self):

        currentVersion = sys.version_info

        self.assertGreaterEqual(currentVersion, (3, 4))


    def test_addNumbers(self):

        expectedValue = 500500
        actualValue = basicOps.addNumbers(1000)

        self.assertEqual(expectedValue, actualValue)

    def test_addMultiplesOf(self):

        expectedValue = 166833
        actualValue = basicOps.addMultiplesOf(3)

        self.assertEqual(expectedValue, actualValue)

    def test_getNumberFrequency(self):

        expectedValue = 10
        actualValue = basicOps.getNumberFrequency(7)

        self.assertEqual(expectedValue, actualValue)

    def test_getDigitalSum(self):

        expectedValue = 23
        actualValue = basicOps.getDigitalSum("314159")

        self.assertEqual(expectedValue, actualValue)

    def test_getSequenceWithoutDigit(self):

        expectedValue = '73692523369559930303550958176261762318'
        actualValue = basicOps.getSequenceWithoutDigit(4)

        self.assertEqual(expectedValue, actualValue)


    def test_capitalizeMe(self):

        expectedValue = 'LoreM IpsuM DoloR A SiT AmeT EU'
        actualValue = basicOps.capitalizeMe('lorem ipsum dolor a sit amet eu')

        self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()

