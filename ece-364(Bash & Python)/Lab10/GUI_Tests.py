import os
import unittest
from PySide.QtTest import *
from PySide.QtCore import *
from Consumer import *

singletonApplication = None
singletonForm = None


class ConsumerTestSuite(unittest.TestCase):

    def setUp(self):
        """
        Creates the QApplication singleton instance, if not present.
        """
        global singletonApplication, singletonForm

        if singletonApplication is None:
            singletonApplication = QApplication(sys.argv)
            singletonForm = Consumer()

        self.app = singletonApplication
        self.form = singletonForm

        # Define a list of text widgets to refer to them all when need.
        self.textWidgets = [self.form.firstNameLineEdit, self.form.lastNameLineEdit, self.form.addressLineEdit,
                            self.form.cityLineEdit, self.form.stateLineEdit, self.form.zipLineEdit, self.form.emailLineEdit]

    def tearDown(self):
        """
        Remove the running application from the self instance.
        """
        del self.app
        del self.form

        # Clean up the file.
        if os.path.exists("target.xml"):
            os.remove("target.xml")

    def test_ClearForm(self):

        formCleared = True

        # Populate all entries.
        QTest.keyClicks(self.form.firstNameLineEdit, "Sherlock")
        QTest.keyClicks(self.form.lastNameLineEdit, "Holmes")
        QTest.keyClicks(self.form.addressLineEdit, "1223 End St.")
        QTest.keyClicks(self.form.cityLineEdit, "West Lafayette")
        QTest.keyClicks(self.form.stateLineEdit, "IN")
        QTest.keyClicks(self.form.zipLineEdit, "47906")

        # Click the button.
        QTest.mouseClick(self.form.clearButton, Qt.LeftButton)

        # Read the form.
        for widget in self.textWidgets:
            formCleared &= widget.text() == ""

        formCleared &= self.form.errorInfoLabel.text() == ""
        formCleared &= self.form.loadButton.isEnabled()
        formCleared &= not self.form.saveToTargetButton.isEnabled()

        self.assertEqual(formCleared, True)

    def test_LoadValidData(self):

        dataCorrect = True

        # Load the xml file.
        self.form.loadDataFromFile("input1.xml")

        # Check values.
        dataCorrect &= self.form.firstNameLineEdit.text() == "George"
        dataCorrect &= self.form.lastNameLineEdit.text() == "Clooney"
        dataCorrect &= self.form.addressLineEdit.text() == "414 Second St."
        dataCorrect &= self.form.cityLineEdit.text() == "Some City"
        dataCorrect &= self.form.stateLineEdit.text() == "CA"
        dataCorrect &= self.form.zipLineEdit.text() == "10001"
        dataCorrect &= self.form.emailLineEdit.text() == "clooney@nowhere.com"

        # Check the buttons.
        dataCorrect &= self.form.errorInfoLabel.text() == ""
        dataCorrect &= self.form.saveToTargetButton.isEnabled()
        dataCorrect &= not self.form.loadButton.isEnabled()

        self.assertEqual(dataCorrect, True)

    def test_SaveValidDataDirect(self):

        # Load the xml file.
        self.form.loadDataFromFile("input1.xml")

        # Save without modification.
        QTest.mouseClick(self.form.saveToTargetButton, Qt.LeftButton)

        with open("input1.xml", "r") as xml:
            source = xml.read()

        with open("target.xml", "r") as xml:
            target = xml.read()

        self.assertEqual(source, target)


    def test_SaveValidDataModified(self):

        # Load the xml file.
        self.form.loadDataFromFile("input1.xml")

        self.form.firstNameLineEdit.clear()
        QTest.keyClicks(self.form.firstNameLineEdit, "Amal")

        self.form.lastNameLineEdit.clear()
        QTest.keyClicks(self.form.lastNameLineEdit, "Alamuddin")

        self.form.addressLineEdit.clear()
        QTest.keyClicks(self.form.addressLineEdit, "909 Second St.")

        self.form.cityLineEdit.clear()
        QTest.keyClicks(self.form.cityLineEdit, "Irvine")

        self.form.stateLineEdit.clear()
        QTest.keyClicks(self.form.stateLineEdit, "TX")

        self.form.zipLineEdit.clear()
        QTest.keyClicks(self.form.zipLineEdit, "56489")

        self.form.emailLineEdit.clear()
        QTest.keyClicks(self.form.emailLineEdit, "amal@hereAndThere.com")

        QTest.mouseClick(self.form.saveToTargetButton, Qt.LeftButton)

        with open("expected1.xml", "r") as xml:
            source = xml.read()

        with open("target.xml", "r") as xml:
            target = xml.read()

        self.assertEqual(source, target)

    def test_SaveWithEmptyEntries(self):

        # Load the xml file.
        self.form.loadDataFromFile("input2.xml")

        # Save without modification.
        QTest.mouseClick(self.form.saveToTargetButton, Qt.LeftButton)

        errorShown = self.form.errorInfoLabel.text() != ""
        fileSaved = os.path.exists("target.xml")

        self.assertEqual(errorShown and not fileSaved, True)

    def test_SaveWithEmptyEntriesPartialFixed(self):

        # Load the xml file.
        self.form.loadDataFromFile("input2.xml")

        QTest.keyClicks(self.form.lastNameLineEdit, "Jackson")

        # Try to save.
        QTest.mouseClick(self.form.saveToTargetButton, Qt.LeftButton)

        errorShown = self.form.errorInfoLabel.text() != ""
        fileSaved = os.path.exists("target.xml")

        self.assertEqual(errorShown and not fileSaved, True)

    def test_SaveWithEmptyEntriesFixed(self):

        # Load the xml file.
        self.form.loadDataFromFile("input2.xml")

        QTest.keyClicks(self.form.lastNameLineEdit, "Jackson")
        QTest.keyClicks(self.form.cityLineEdit, "Los Angeles")

        # Try to save.
        QTest.mouseClick(self.form.saveToTargetButton, Qt.LeftButton)

        errorShown = self.form.errorInfoLabel.text() == ""

        with open("expected2.xml", "r") as xml:
            source = xml.read()

        with open("target.xml", "r") as xml:
            target = xml.read()

        self.assertTrue(errorShown)
        self.assertEqual(source, target)

    def test_SaveWithInvalidEntriesStateFixed(self):

        # Load the xml file.
        self.form.loadDataFromFile("input3.xml")

        self.form.stateLineEdit.clear()
        QTest.keyClicks(self.form.stateLineEdit, "NY")

        # Try to save.
        QTest.mouseClick(self.form.saveToTargetButton, Qt.LeftButton)

        errorShown = self.form.errorInfoLabel.text() != ""
        fileSaved = os.path.exists("target.xml")

        self.assertEqual(errorShown and not fileSaved, True)

    def test_SaveWithInvalidEntriesStateAndZipFixed(self):

        # Load the xml file.
        self.form.loadDataFromFile("input3.xml")

        self.form.stateLineEdit.clear()
        QTest.keyClicks(self.form.stateLineEdit, "NY")

        self.form.zipLineEdit.clear()
        QTest.keyClicks(self.form.stateLineEdit, "20201")

        # Try to save.
        QTest.mouseClick(self.form.saveToTargetButton, Qt.LeftButton)

        errorShown = self.form.errorInfoLabel.text() != ""
        fileSaved = os.path.exists("target.xml")

        self.assertEqual(errorShown and not fileSaved, True)

    def test_SaveWithInvalidEntriesAllFixed(self):

        # Load the xml file.
        self.form.loadDataFromFile("input3.xml")

        self.form.stateLineEdit.clear()
        QTest.keyClicks(self.form.stateLineEdit, "NY")

        self.form.zipLineEdit.clear()
        QTest.keyClicks(self.form.zipLineEdit, "20201")

        self.form.emailLineEdit.clear()
        QTest.keyClicks(self.form.emailLineEdit, "someone@famous.com")

        # Try to save.
        QTest.mouseClick(self.form.saveToTargetButton, Qt.LeftButton)

        errorShown = self.form.errorInfoLabel.text() == ""

        with open("expected3.xml", "r") as xml:
            source = xml.read()

        with open("target.xml", "r") as xml:
            target = xml.read()

        self.assertTrue(errorShown)
        self.assertEqual(source, target)

if __name__ == '__main__':
    unittest.main()
