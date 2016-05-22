import sys
import unittest

##from wheel.wininst2wheel import parse_info

from test import *

class Lab03TestSuite(unittest.TestCase):

    def test_checkPythonVersion(self):

        currentVersion = sys.version_info

        self.assertGreaterEqual(currentVersion, (3, 4))

    def test_getPairwiseDifference(self):

        with self.subTest(key="Invalid Type"):
            vec = "I am not a list."
            self.assertIsNone(getPairwiseDifference(vec))

        with self.subTest(key="Empty List"):
            vec = []
            self.assertIsNone(getPairwiseDifference(vec))


            vec = [8, 4, 15, 10, 12, 14, 13]
            expectedValue = [-4, 11, -5, 2, 2, -1]
            actualValue = getPairwiseDifference(vec)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Good Input 2"):
            vec = [16, 10, 27, 4, 7, 3, 24, 13, 27, 21]
            expectedValue = [-6, 17, -23, 3, -4, 21, -11, 14, -6]
            actualValue = getPairwiseDifference(vec)
            self.assertEqual(expectedValue, actualValue)

    def test_flatten(self):

        with self.subTest(key="Invalid Type"):
            vec = 3.14
            self.assertIsNone(flatten(vec))

        with self.subTest(key="List of Items"):
            vec = [[2, 3], 7, [8, 9]]
            self.assertIsNone(flatten(vec))

        with self.subTest(key="Good Input 1"):
            vec = [[2, 3, 1], [9], [7, -1]]
            expectedValue = [2, 3, 1, 9, 7, -1]
            actualValue = flatten(vec)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Good Input 2"):
            vec = [[-1, 0, 6], [-2, -2], [8, 11]]
            expectedValue = [-1, 0, 6, -2, -2, 8, 11]
            actualValue = flatten(vec)
            self.assertEqual(expectedValue, actualValue)

    def test_partition(self):

        with self.subTest(key="Invalid Type"):
            vec = "I am not a list."
            self.assertIsNone(partition(vec, 2))

        with self.subTest(key="Empty List"):
            vec = []
            self.assertIsNone(partition(vec, 3))

        with self.subTest(key="Good Input 1"):
            vec = [11, 18, 15, 21, 19, 13, 14, 17]
            expectedValue = [[11, 18, 15], [21, 19, 13], [14, 17]]
            actualValue = partition(vec, 3)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Good Input 2"):
            vec = [15, 23, 28, 19, 22, 29]
            expectedValue = [[15, 23], [28, 19], [22, 29]]
            actualValue = partition(vec, 2)
            self.assertEqual(expectedValue, actualValue)

    def test_rectifySignal(self):

        with self.subTest(key="Invalid Type"):
            vec = "Hello?"
            self.assertIsNone(rectifySignal(vec))

        with self.subTest(key="Empty List"):
            vec = []
            self.assertIsNone(rectifySignal(vec))

        with self.subTest(key="Good Input 1"):
            vec = [1.0, 0.81, 0.31, -0.31, -0.81, -1.0, -0.81, -0.31, 0.31, 0.81]
            expectedValue = [1.0, 0.81, 0.31, 0, 0, 0, 0, 0, 0.31, 0.81]
            actualValue = rectifySignal(vec)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Good Input 2"):
            vec = [2.0, -3.0, 4.0, -5.5, 6.7, -2.7, 9.6, -3.1]
            expectedValue = [2.0, 0, 4.0, 0, 6.7, 0, 9.6, 0]
            actualValue = rectifySignal(vec)
            self.assertEqual(expectedValue, actualValue)

    def test_floatRange(self):

        with self.subTest(key="Incorrect Input"):
            self.assertIsNone(floatRange(0, 0, 0.1))

        with self.subTest(key="0.1"):
            expectedValue = [4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0]
            actualValue = floatRange(4, 5, 0.1)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="0.2"):
            expectedValue = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0]
            actualValue = floatRange(1, 3, 0.2)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="0.5"):
            expectedValue = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
            actualValue = floatRange(0, 4, 0.5)
            self.assertEqual(expectedValue, actualValue)

    def test_getLongestWord(self):

        with self.subTest(key="Invalid Type"):
            s = 3.14
            self.assertIsNone(getLongestWord(s))

        with self.subTest(key="Longer than 1"):
            s = "World"
            self.assertIsNone(getLongestWord(s))

        with self.subTest(key="Good Input 1"):
            s = "The weather is cool today"
            expectedValue = "weather"
            actualValue = getLongestWord(s)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Good Input 2"):
            s = "The Aardvark decided he shall eat ants today"
            expectedValue = "Aardvark"
            actualValue = getLongestWord(s)
            self.assertEqual(expectedValue, actualValue)

    def test_decodeNumbers(self):

        with self.subTest(key="Invalid Type"):
            l = "I am not a list."
            self.assertIsNone(decodeNumbers(l))

        with self.subTest(key="Non-integer List"):
            l = [32, 11, 121, True, None]
            self.assertIsNone(decodeNumbers(l))

        with self.subTest(key="Good Input 1"):
            l = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 116, 104, 101, 32, 98, 101, 115, 116, 32, 108, 97, 110,
                 103, 117, 97, 103, 101, 44, 32, 97, 110, 100, 32, 101, 118, 101, 114, 121, 111, 110, 101, 32, 115, 104,
                 111, 117, 108, 100, 32, 114, 101, 97, 108, 108, 121, 32, 108, 101, 97, 114, 110, 32, 105, 116, 33]
            expectedValue = "Python is the best language, and everyone should really learn it!"
            actualValue = decodeNumbers(l)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Good Input 2"):
            l = [69, 67, 69, 51, 54, 52, 32, 115, 104, 111, 117, 108, 100, 32, 98, 101, 32, 109, 111, 114, 101, 32, 116,
                 104, 97, 110, 32, 49, 32, 67, 114, 101, 100, 105, 116, 32, 72, 111, 117, 114, 33]
            expectedValue = "ECE364 should be more than 1 Credit Hour!"
            actualValue = decodeNumbers(l)
            self.assertEqual(expectedValue, actualValue)

    def test_getCreditCard(self):

        with self.subTest(key="Incorrect Input"):
            self.assertIsNone(getCreditCard(""))

        with self.subTest(key="Good Input 1"):
            s = "Sherlock Holmes 1234-6598-7845-2050"
            expectedValue = [1, 2, 3, 4, 6, 5, 9, 8, 7, 8, 4, 5, 2, 0, 5, 0]
            actualValue = getCreditCard(s)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Good Input 2"):
            s = "Adele 9461875431642435"
            expectedValue = [9, 4, 6, 1, 8, 7, 5, 4, 3, 1, 6, 4, 2, 4, 3, 5]
            actualValue = getCreditCard(s)
            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Good Input 3"):
            s = "Edgar Allan Poe 4315 4404 9080 8866"
            expectedValue = [4, 3, 1, 5, 4, 4, 0, 4, 9, 0, 8, 0, 8, 8, 6, 6]
            actualValue = getCreditCard(s)
            self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()
