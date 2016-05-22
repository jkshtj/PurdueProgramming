import sys
import unittest

try:
    from regExPractical import *
except ImportError:
    print("Unable to import 'regExPractical'. Create an Empty Python file with that name.")

try:
    from timeDuration import *
except ImportError:
    print("Unable to import 'timeDuration'. Create an Empty Python file with that name.")

try:
    from timeManager import *
except ImportError:
    print("Unable to import 'timeManager'. Create an Empty Python file with that name.")


class PracticalTestCases(unittest.TestCase):

    def test_validityChecks(self):

        with self.subTest(key="Use of Split()"):
            with open("regExPractical.py", "r") as pyFile:
                sourceCode = pyFile.read()

            self.assertFalse("split(" in sourceCode)

        with self.subTest(key="Python Version"):
            currentVersion = sys.version_info
            self.assertGreaterEqual(currentVersion, (3, 4))

    def test_regEx_getAddress(self):

        with self.subTest(key="Good 1"):

            s = "The card was at 58-1c-0a-6e-39-4d, but it was removed."
            expectedValue = "58-1c-0a-6e-39-4d"
            actualValue = getAddress(s)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Good 2"):

            s = "Installation defaults to 00:A0:C9:14:C8:29"
            expectedValue = "00:A0:C9:14:C8:29"
            actualValue = getAddress(s)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Good 3"):

            s = "00:1c:b3:09:85:1f is not present in the system."
            expectedValue = "00:1c:b3:09:85:1f"
            actualValue = getAddress(s)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Bad 1"):

            s = "Certain parts of 10:1G:H3:09:85:IF are invalid."
            actualValue = getAddress(s)

            self.assertIsNone(actualValue)

        with self.subTest(key="Bad 2"):

            s = "The row has the address 6A08F128C642."
            actualValue = getAddress(s)

            self.assertIsNone(actualValue)

        with self.subTest(key="Bad 3"):

            s = "Antivirus located a bug at 96:00:6d:9c:ba."
            actualValue = getAddress(s)

            self.assertIsNone(actualValue)

    def test_regEx_getSwitches(self):

        with self.subTest(key="Group 1"):

            commandline = r"myScript.bash +v  \i 2   +p  /local/bin/somefolder"
            expectedValue = [("i", "2"), ("p", "/local/bin/somefolder")]
            actualValue = getSwitches(commandline)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Group 2"):

            commandline = r"program.py +k +D 44 \j full  \t  allArea"
            expectedValue = [("j", "full"), ("t", "allArea")]
            actualValue = getSwitches(commandline)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Group 3"):

            commandline = r"checkMap.pl  +g gcc5  +K optimize \f skip \c include:new.c \w +a"
            expectedValue = [("c", "include:new.c"), ("f", "skip"), ("g", "gcc5")]
            actualValue = getSwitches(commandline)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Group 4"):

            commandline = r"tryCode.sh \X repeat  -u 3.1  \h local/bin/python3.5  +s +a +z combine"
            expectedValue = [("h", "local/bin/python3.5"), ("z", "combine")]
            actualValue = getSwitches(commandline)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Group 5"):

            commandline = r"run.exe \a \b \d +g +w OK"
            expectedValue = [("w", "OK")]
            actualValue = getSwitches(commandline)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Group 6"):

            commandline = r"begin_parse.sh -w 2 +q startnow \s stopOnError"
            expectedValue = [("q", "startnow"), ("s", "stopOnError")]
            actualValue = getSwitches(commandline)

            self.assertEqual(expectedValue, actualValue)

    def test_regEx_getElements(self):

        with self.subTest(key="Valid 1"):

            url = "https://www.paypal.com/Customer1Area/Pay2"
            expectedValue = "www.paypal.com", "Customer1Area", "Pay2"
            actualValue = getElements(url)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Valid 2"):

            url = "http://www3.google.com.cn/search/music"
            expectedValue = "www3.google.com.cn", "search", "music"
            actualValue = getElements(url)

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Underscore in Controller"):

            url = "http://www.purdue.edu/About_Us/History"
            actualValue = getElements(url)

            self.assertIsNone(actualValue)

        with self.subTest(key="Less"):

            url = "https://purdue.syncplicity.com/AboutUs"
            actualValue = getElements(url)

            self.assertIsNone(actualValue)

        with self.subTest(key="More"):

            url = "http://www.yahoo.com/AboutUs/Vision/Leadership"
            actualValue = getElements(url)

            self.assertIsNone(actualValue)

        with self.subTest(key="Wrong 1"):

            url = "ftp://files.microsoft.com/Download/New"
            actualValue = getElements(url)

            self.assertIsNone(actualValue)

        with self.subTest(key="Wrong 2"):

            url = "http://www.cnn.com/First.New/Articles"
            actualValue = getElements(url)

            self.assertIsNone(actualValue)

        with self.subTest(key="Wrong 3"):

            url = "http://www.cnn.com/News/On.Tuesday"
            actualValue = getElements(url)

            self.assertIsNone(actualValue)

    def test_timeSpan_initializer(self):

        with self.subTest(key="Normal"):

            d = TimeSpan(3, 2, 20)
            self.assertIsNotNone(d)

        with self.subTest(key="AttributeCheck"):

            d = TimeSpan(4, 20, 188)

            self.assertTrue(hasattr(d, "weeks") and hasattr(d, "days") and hasattr(d, "hours"))

        with self.subTest(key="Large 1"):

            d = TimeSpan(3, 14, 188)
            expectedValue = 6, 0, 20
            actualValue = d.weeks, d.days, d.hours

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Large 2"):

            d = TimeSpan(1, 92, 30)
            expectedValue = 14, 2, 6
            actualValue = d.weeks, d.days, d.hours

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="LargeIntegers"):

            d = TimeSpan(103, 148, 397)
            expectedValue = 126, 3, 13
            actualValue = d.weeks, d.days, d.hours

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Wrong Type"):

            self.assertRaises(TypeError, TimeSpan, 2, 3.5, 10)

        with self.subTest(key="Wrong Value"):

            self.assertRaises(ValueError, TimeSpan, 0, 15, -1)

    def test_timeSpan_stringRepresentation(self):

        with self.subTest(key="String1"):

            expectedValue = "01W 2D 03H"
            actualValue = str(TimeSpan(1, 2, 3))

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="String2"):

            expectedValue = "101W 0D 00H"
            actualValue = str(TimeSpan(101, 0, 0))

            self.assertEqual(expectedValue, actualValue)

    def test_timeSpan_TotalHours(self):

        with self.subTest(key="Check 1"):

            expectedValue = 4873
            actualValue = TimeSpan(23, 41, 25).getTotalHours()

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Check 2"):

            expectedValue = 5610
            actualValue = TimeSpan(26, 50, 42).getTotalHours()

            self.assertEqual(expectedValue, actualValue)

    def test_timeSpan_addition(self):

        d1 = TimeSpan(5, 59, 23)
        d2 = TimeSpan(3, 12, 45)

        d = d1 + d2

        with self.subTest(key="Normal"):

            expectedValue = 18, 3, 20
            actualValue = d.weeks, d.days, d.hours

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            self.assertTrue(d is not d1 and d is not d2)

        with self.subTest(key="WrongType"):

            self.assertRaises(TypeError, lambda x, y: x + y, d1, 2.70)

    def test_timeSpan_multiplication(self):

        d = TimeSpan(11, 13, 50)

        with self.subTest(key="Scale 1"):

            scaled = d * 3
            expectedValue = 39, 3, 6
            actualValue = scaled.weeks, scaled.days, scaled.hours

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Scaled 2"):

            scaled = 5 * d
            expectedValue = 65, 5, 10
            actualValue = scaled.weeks, scaled.days, scaled.hours

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Identity"):

            scaled = d * 2
            self.assertTrue(scaled is not d)

        with self.subTest(key="Wrong 1"):

            self.assertRaises(TypeError, lambda x, y: x * y, d, 3.14)

        with self.subTest(key="Wrong 2"):

            self.assertRaises(ValueError, lambda x, y: x * y, d, 0)

    def test_modules_getTotalEventSpan(self):

        with self.subTest(key="Event13"):

            ex = "Event13"
            total = getTotalEventSpan(ex)

            expectedValue = 112, 1, 10
            actualValue = total.weeks, total.days, total.hours

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Event09"):

            ex = "Event09"
            total = getTotalEventSpan(ex)

            expectedValue = 126, 5, 21
            actualValue = total.weeks, total.days, total.hours

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Event07"):

            ex = "Event07"
            total = getTotalEventSpan(ex)

            expectedValue = 11, 5, 0
            actualValue = total.weeks, total.days, total.hours

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Event17"):

            ex = "Event17"
            total = getTotalEventSpan(ex)

            expectedValue = 4, 5, 2
            actualValue = total.weeks, total.days, total.hours

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Event00"):

            ex = "Event00"
            total = getTotalEventSpan(ex)

            expectedValue = 73, 3, 14
            actualValue = total.weeks, total.days, total.hours

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="Event03"):

            ex = "Event03"
            total = getTotalEventSpan(ex)

            expectedValue = 2, 1, 14
            actualValue = total.weeks, total.days, total.hours

            self.assertEqual(expectedValue, actualValue)

    def test_modules_rankEvents(self):

        with self.subTest(key="00, 09, 17"):

            expectedValue = ["Event09", "Event00", "Event17"]
            actualValue = rankEventsBySpan("Event00", "Event09", "Event17")

            self.assertEqual(expectedValue, actualValue)

        with self.subTest(key="01, 02, 03, 04, 05"):

            expectedValue = ['Event01', 'Event04', 'Event05', 'Event03', 'Event02']
            actualValue = rankEventsBySpan("Event01", "Event02", "Event03", "Event04", "Event05")

            self.assertEqual(expectedValue, actualValue)


if __name__ == '__main__':
    unittest.main()
