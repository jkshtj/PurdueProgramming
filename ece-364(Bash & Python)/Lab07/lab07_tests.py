import sys
import unittest
from Institute import *


class Lab07TestSuite(unittest.TestCase):

    def test_checkPythonVersion(self):

        currentVersion = sys.version_info

        self.assertGreaterEqual(currentVersion, (3, 4))

    def test_simulation_initializerAndAttributes(self):

        sim = Simulation(128, "01/01/2016", "SomeChip", 20, 3.14)

        with self.subTest(key="Number"):
            self.assertEqual(128, sim.simulationNumber)

        with self.subTest(key="Date"):
            self.assertEqual("01/01/2016", sim.simulationDate)

        with self.subTest(key="ChipName"):
            self.assertEqual("SomeChip", sim.chipName)

        with self.subTest(key="ChipCount"):
            self.assertEqual(20, sim.chipCount)

        with self.subTest(key="ChipCost"):
            self.assertEqual(3.14, sim.chipCost)

        with self.subTest(key="TotalCost"):
            self.assertAlmostEqual(62.8, sim.simulationCost, 2)

    def test_simulation_representation(self):

        sim = Simulation(55, "02/29/2016", "i3-9988", 3, 3.14)

        expectedValue = "i3-9988: 055, 02/29/2016, $009.42"
        actualValue = str(sim)

        self.assertEqual(expectedValue, actualValue)

    def test_employee_initializerAndAttribute(self):

        e = Employee("Elizabeth Rogers", "987-63-1245")

        with self.subTest(key="Name"):
            self.assertEqual("Elizabeth Rogers", e.employeeName)

        with self.subTest(key="ID"):
            self.assertEqual("987-63-1245", e.employeeID)

    def test_employee_representation(self):

        s1 = Simulation(128, "01/01/2016", "SomeChip", 20, 3.14)
        s2 = Simulation(497, "05/07/2016", "AnotherChip", 10, 2.71)
        s3 = Simulation(5, "11/12/2016", "UniqueChip", 45, 10.0)

        e = Employee("Margaret Cook", "124-63-1987")

        for s in [s1, s2, s3]:
            e.addSimulation(s)

        expectedValue = "124-63-1987, Margaret Cook: 03 Simulations"
        actualValue = str(e)

        self.assertEqual(expectedValue, actualValue)

    def test_employee_addSimulation(self):

        s1 = Simulation(128, "01/01/2016", "SomeChip", 20, 3.14)
        s2 = Simulation(497, "05/07/2016", "AnotherChip", 10, 2.71)
        s3 = Simulation(497, "07/09/2016", "UniqueChip", 30, 10.0)

        e = Employee("Margaret Cook", "124-63-1987")

        with self.subTest(key="Add"):

            e.addSimulation(s1)
            self.assertEqual(s1, e.simulationsDict[128])

        with self.subTest(key="Update"):

            e.addSimulation(s2)
            e.addSimulation(s3)

            self.assertNotEqual(s2, e.simulationsDict[497])

    def test_employee_getSimulation(self):

        s1 = Simulation(128, "01/01/2016", "SomeChip", 20, 3.14)
        s2 = Simulation(497, "05/07/2016", "AnotherChip", 10, 2.71)
        s3 = Simulation(5, "11/12/2016", "UniqueChip", 45, 10.0)

        e = Employee("Elizabeth Rogers", "987-63-1245")

        for s in [s1, s2, s3]:
            e.addSimulation(s)

        with self.subTest(key="Present"):
            self.assertEqual(s3, e.getSimulation(5))

        with self.subTest(key="Absent"):
            self.assertIsNone(e.getSimulation(125))

    def test_employee_getWorkload(self):

        s1 = Simulation(128, "01/01/2016", "SomeChip", 20, 3.14)
        s2 = Simulation(497, "05/07/2016", "AnotherChip", 10, 2.71)
        s3 = Simulation(5, "11/12/2016", "UniqueChip", 45, 10.0)

        e = Employee("Elizabeth Rogers", "987-63-1245")

        for s in [s1, s2, s3]:
            e.addSimulation(s)

        expectedValue = "987-63-1245, Elizabeth Rogers: 03 Simulations\n"
        expectedValue += "AnotherChip: 497, 05/07/2016, $027.10\n"
        expectedValue += "SomeChip: 128, 01/01/2016, $062.80\n"
        expectedValue += "UniqueChip: 005, 11/12/2016, $450.00"
        actualValue = e.getWorkload()

        self.assertEqual(expectedValue, actualValue)

    def test_employee_addWorkload(self):

        s1 = Simulation(23, "04/28/2015", "i7-3456", 30, 3.28)
        s2 = Simulation(495, "06/10/2015", "i7-4152", 160, 1.94)
        s3 = Simulation(1, "03/16/2015", "i7-7532", 5, 3.07)

        e = Employee("Mitch Daniels", "351-46-4136")
        e.addWorkload("workload1.txt")

        with self.subTest(key="Chip 1"):
            self.assertEqual(str(s1), str(e.simulationsDict[23]))

        with self.subTest(key="Chip 2"):
            self.assertEqual(s2.simulationDate, "06/10/2015")

        with self.subTest(key="Chip 3"):
            self.assertEqual(s3.simulationNumber, 1)

        with self.subTest(key="All"):
            expectedValue = "351-46-4136, Mitch Daniels: 04 Simulations\n"
            expectedValue += "i7-3456: 023, 04/28/2015, $098.40\n"
            expectedValue += "i7-4152: 495, 06/10/2015, $310.40\n"
            expectedValue += "i7-7532: 001, 03/16/2015, $015.35\n"
            expectedValue += "i7-9546: 017, 07/19/2015, $112.80"
            actualValue = e.getWorkload()

            self.assertEqual(expectedValue, actualValue)

    def test_facility_initializerAndAttribute(self):

        f = Facility("IBM")

        with self.subTest(key="Name"):
            self.assertEqual("IBM", f.facilityName)

        with self.subTest(key="Map"):
            self.assertDictEqual({}, f.employeesDict)

    def test_facility_representation(self):

        f = Facility("Intel")
        e1 = Employee("Alejandro Carrero", "520-11-9977")
        e2 = Employee("Tracey Driscoll", "741-85-9632")

        e1.addWorkload("workload1.txt")
        e2.addWorkload("workload2.txt")
        f.addEmployee(e1)
        f.addEmployee(e2)

        expectedValue = "Intel: 02 Employees\n"
        expectedValue += "520-11-9977, Alejandro Carrero: 04 Simulations\n"
        expectedValue += "741-85-9632, Tracey Driscoll: 04 Simulations"
        actualValue = str(f)

        self.assertEqual(expectedValue, actualValue)

    def test_facility_addEmployee(self):

        f = Facility("TI")
        e1 = Employee("Diego Jesus", "520-11-9977")
        e2 = Employee("John George", "741-85-9632")
        e3 = Employee("John George", "999-88-7777")

        with self.subTest(key="Add"):

            f.addEmployee(e1)
            self.assertEqual(e1, f.employeesDict["Diego Jesus"])

        with self.subTest(key="Update"):

            f.addEmployee(e2)
            f.addEmployee(e3)

            self.assertNotEqual(e2, f.employeesDict["John George"])

    def test_facility_getEmployees(self):

        f = Facility("TI")
        e1 = Employee("Diego Jesus", "520-11-9977")
        e2 = Employee("John George", "741-85-9632")
        e3 = Employee("George Michael", "456-58-2369")

        for e in [e1, e2, e3]:
            f.addEmployee(e)

        with self.subTest(key="Get1"):
            self.assertListEqual([e1], f.getEmployees("Diego Jesus"))

        with self.subTest(key="Get2"):
            self.assertListEqual([e2, e3], f.getEmployees("John George", "George Michael"))

    def test_facility_getSimulation(self):

        f = Facility("Intel")
        e1 = Employee("Alejandro Carrero", "520-11-9977")
        e2 = Employee("Tracey Driscoll", "741-85-9632")

        e1.addWorkload("workload1.txt")
        e2.addWorkload("workload2.txt")
        f.addEmployee(e1)
        f.addEmployee(e2)

        with self.subTest(key="Get1"):
            s = Simulation(17, "07/19/2015", "i7-9546", 94, 1.20)
            fs = f.getSimulation(17)
            expectedValue = {s.simulationNumber, s.simulationDate, s.simulationCost}
            actualValue = {fs.simulationNumber, fs.simulationDate, fs.simulationCost}

            self.assertSetEqual(expectedValue, actualValue)

        with self.subTest(key="Get2"):
            s = Simulation(22, "02/15/2015", "i7-3456", 112, 1.2)
            fs = f.getSimulation(22)
            expectedValue = {s.simulationNumber, s.simulationDate, s.simulationCost}
            actualValue = {fs.simulationNumber, fs.simulationDate, fs.simulationCost}

            self.assertSetEqual(expectedValue, actualValue)

        with self.subTest(key="Get3"):
            s = Simulation(71, "03/02/2015", "i7-9546", 28, 3.62)
            fs = f.getSimulation(71)
            expectedValue = {s.simulationNumber, s.simulationDate, s.simulationCost}
            actualValue = {fs.simulationNumber, fs.simulationDate, fs.simulationCost}

            self.assertSetEqual(expectedValue, actualValue)

        with self.subTest(key="Get2"):
            fs = f.getSimulation(999)

            self.assertIsNone(fs)


if __name__ == '__main__':
    unittest.main()
