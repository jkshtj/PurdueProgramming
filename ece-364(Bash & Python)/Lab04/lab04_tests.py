import sys
import unittest

from registrar import *


class Lab04TestSuite(unittest.TestCase):

    def test_checkPythonVersion(self):
        currentVersion = sys.version_info
        self.assertGreaterEqual(currentVersion, (3, 4))

    def test_getDetails(self):

        studentMap = getDetails()

        with self.subTest(key="Key Type"):
            self.assertTrue(all([type(k) is str for k in studentMap.keys()]))

        with self.subTest(key="Value Type"):
            self.assertTrue(all([type(v) is set for v in studentMap.values()]))

        with self.subTest(key="Entry Count"):

            expectedValue1 = 20
            actualValue1 = len(studentMap)
            expectedValue2 = 50
            actualValue2 = sum([len(value) for value in studentMap.values()])

            check = expectedValue1 == actualValue1 and expectedValue2 == actualValue2

            self.assertTrue(check)

        with self.subTest(key="Student 1"):
            expectedValue = {('370', 61), ('430', 96)}
            actualValue = studentMap["Evelyn R Bryant"]

            self.assertSetEqual(expectedValue, actualValue)

        with self.subTest(key="Student 2"):
            expectedValue = {('370', 98), ('430', 85), ('410', 72)}
            actualValue = studentMap["Carolyn G King"]

            self.assertSetEqual(expectedValue, actualValue)

        with self.subTest(key="Student 3"):
            expectedValue = {('410', 53), ('450', 61), ('370', 80), ('375', 72)}
            actualValue = studentMap["Keith Z Adams"]

            self.assertSetEqual(expectedValue, actualValue)

        with self.subTest(key="Student 4"):
            expectedValue = {('450', 53)}
            actualValue = studentMap["Douglas K Davis"]

            self.assertSetEqual(expectedValue, actualValue)

        with self.subTest(key="Student 5"):
            expectedValue = {('375', 84), ('450', 66), ('370', 67)}
            actualValue = studentMap["Marie E Perry"]

            self.assertSetEqual(expectedValue, actualValue)

    def test_getStudentList(self):

        with self.subTest(key="Invalid Class"):
            className = "700"
            actualValue = getStudentList(className)
            expectedValue = []

            self.assertListEqual(expectedValue, actualValue)

        with self.subTest(key="Class EECS370"):
            className = "370"
            actualValue = getStudentList(className)
            expectedValue = ['Anne O Harris', 'Betty T Torres', 'Beverly Z Hall', 'Carolyn G King', 'Evelyn R Bryant',
                             'Joyce Q Kelly', 'Keith Z Adams', 'Marie E Perry', 'Martha E Garcia', 'Paul T Jenkins']

            self.assertListEqual(expectedValue, actualValue)

        with self.subTest(key="Class EECS410"):
            className = "410"
            actualValue = getStudentList(className)
            expectedValue = ['Betty T Torres', 'Carolyn G King', 'Catherine Q Bailey', 'Eugene E Campbell',
                             'Frank Q Young', 'George J Richardson', 'Johnny W Evans', 'Keith Z Adams',
                             'Linda P Ramirez', 'Paul T Jenkins']

            self.assertListEqual(expectedValue, actualValue)

        with self.subTest(key="Class EECS450"):
            className = "450"
            actualValue = getStudentList(className)
            expectedValue = ['Betty T Torres', 'Catherine Q Bailey', 'Douglas K Davis', 'Eugene E Campbell',
                             'Heather Z Morris', 'Keith Z Adams', 'Linda P Ramirez', 'Marie E Perry', 'Martha E Garcia',
                             'Paul T Jenkins']

            self.assertListEqual(expectedValue, actualValue)

    def test_searchForName(self):
        with self.subTest(key="Invalid Name"):
            studentName = "Carolyn Martin"
            actualValue = searchForName(studentName)
            expectedValue = {}

            self.assertDictEqual(expectedValue, actualValue)

        with self.subTest(key="Valid Student Name 1"):
            studentName = "Martha E Garcia"
            actualValue = searchForName(studentName)
            expectedValue = {'370': 83, '430': 65, '375': 91, '450': 89}

            self.assertDictEqual(expectedValue, actualValue)

        with self.subTest(key="Valid Student Name 2"):
            studentName = "Keith Z Adams"
            actualValue = searchForName(studentName)
            expectedValue = {'450': 61, '370': 80, '410': 53, '375': 72}

            self.assertDictEqual(expectedValue, actualValue)

        with self.subTest(key="Valid Student Name 3"):
            studentName = "Eugene E Campbell"
            actualValue = searchForName(studentName)
            expectedValue = {'410': 83, '450': 81}

            self.assertDictEqual(expectedValue, actualValue)

    def test_searchForID(self):

        with self.subTest(key="Invalid ID"):
            studentID = "12345-98765"
            actualValue = searchForID(studentID)
            expectedValue = {}

            self.assertDictEqual(expectedValue, actualValue)

        with self.subTest(key="Valid ID"):
            studentID = "63581-09884"
            actualValue = searchForID(studentID)
            expectedValue = {'370': 94, '410': 88, '450': 78}

            self.assertDictEqual(expectedValue, actualValue)

    def test_findScore(self):
        with self.subTest(key="Invalid Student Name"):
            studentName = "Arya Stark"
            classNumber = "370"
            actualValue = findScore(studentName, classNumber)

            self.assertIsNone(actualValue)

        with self.subTest(key="Invalid Class Number"):
            studentName = "Douglas K Davis"
            classNumber = "699"
            actualValue = findScore(studentName, classNumber)

            self.assertIsNone(actualValue)

        with self.subTest(key="Valid Query 1"):
            studentName = "Johnny W Evans"
            classNumber = "375"
            actualValue = findScore(studentName, classNumber)
            expectedValue = 94

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Valid Query 2"):
            studentName = "Carolyn G King"
            classNumber = "410"
            actualValue = findScore(studentName, classNumber)
            expectedValue = 72

            self.assertEqual(expectedValue, actualValue)

    def test_getHighest(self):

        with self.subTest(key="Return Type"):
            classNumber = "370"
            actualValue = getHighest(classNumber)

            self.assertTrue(type(actualValue) is tuple)

        with self.subTest(key="Invalid Class"):
            classNumber = "700"
            actualValue = getHighest(classNumber)
            expectedValue = ()

            self.assertTupleEqual(expectedValue, actualValue)

        with self.subTest(key="Class EECS370"):
            classNumber = "370"
            actualValue = getHighest(classNumber)
            expectedValue = 'Carolyn G King', 98

            self.assertTupleEqual(expectedValue, actualValue)

        with self.subTest(key="Class EECS430"):
            classNumber = "430"
            actualValue = getHighest(classNumber)
            expectedValue = 'Evelyn R Bryant', 96

            self.assertTupleEqual(expectedValue, actualValue)

    def test_getLowest(self):
        with self.subTest(key="Invalid Class"):
            classNumber = "700"
            actualValue = getLowest(classNumber)
            expectedValue = ()

            self.assertTupleEqual(expectedValue, actualValue)

        with self.subTest(key="Class EECS450"):
            classNumber = "450"
            actualValue = getLowest(classNumber)
            expectedValue = 'Heather Z Morris', 50

            self.assertTupleEqual(expectedValue, actualValue)

    def test_getAverageScore(self):
        with self.subTest(key="Invalid Name"):
            studentName = "Goku Siachan"
            actualValue = getAverageScore(studentName)

            self.assertIsNone(actualValue)

        with self.subTest(key="Valid Name 1"):
            studentName = "James F Hughes"
            actualValue = getAverageScore(studentName)
            expectedValue = 71.5

            self.assertAlmostEqual(expectedValue, actualValue, 1)

        with self.subTest(key="Valid Name 2"):
            studentName = "Beverly Z Hall"
            actualValue = getAverageScore(studentName)
            expectedValue = 68.5

            self.assertAlmostEqual(expectedValue, actualValue, 1)

if __name__ == '__main__':
    unittest.main()

