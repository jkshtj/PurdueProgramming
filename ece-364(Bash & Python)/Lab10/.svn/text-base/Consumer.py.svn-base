import sys
import re
from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):



    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
          "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
          "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

        self.clearButton.clicked.connect(lambda :self.clear())
        self.firstNameLineEdit.textChanged.connect(lambda :self.data_entry())
        self.lastNameLineEdit.textChanged.connect(lambda :self.data_entry())
        self.addressLineEdit.textChanged.connect(lambda :self.data_entry())
        self.cityLineEdit.textChanged.connect(lambda :self.data_entry())
        self.stateLineEdit.textChanged.connect(lambda :self.data_entry())
        self.emailLineEdit.textChanged.connect(lambda :self.data_entry())
        self.zipLineEdit.textChanged.connect(lambda :self.data_entry())
        self.saveToTargetButton.clicked.connect(lambda :self.validate())
        self.loadButton.clicked.connect(lambda :self.loadData())



    def clear(self):
        self.firstNameLineEdit.clear()
        self.lastNameLineEdit.clear()
        self.addressLineEdit.clear()
        self.cityLineEdit.clear()
        self.stateLineEdit.clear()
        self.emailLineEdit.clear()
        self.zipLineEdit.clear()
        self.loadButton.setEnabled(True)
        self.saveToTargetButton.setDisabled(True)


    def data_entry(self):
        self.saveToTargetButton.setEnabled(True)
        self.loadButton.setDisabled(True)


    def validate(self):
        if self.all_pop() == False:
            self.errorInfoLabel.setText("Error: All fields not populted!")

        elif self.stateLineEdit.text() not in self.states:
            self.errorInfoLabel.setText("Error: State is not valid!")

        elif len(self.zipLineEdit.text()) != 5 or self.zipLineEdit.text().isdigit() == False:
            self.errorInfoLabel.setText("Error: Zip is not valid!")

        elif re.match(r"\w+@\w+\.\w+",self.emailLineEdit.text()) == None:
            self.errorInfoLabel.setText("Error: Email is not valid!")

        else:
            self.errorInfoLabel.clear()
            self.save_to_xml()


    def save_to_xml(self):
        with open("target.xml","w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?\n')
            f.write('<user>\n')
            f.write('\t<FirstName>'+self.firstNameLineEdit.text()+'</FirstName>\n')
            f.write('\t<LastName>'+self.lastNameLineEdit.text()+'</LastName>\n')
            f.write('\t<Address>'+self.addressLineEdit.text()+'</Address>\n')
            f.write('\t<City>'+self.cityLineEdit.text()+'</City>\n')
            f.write('\t<State>'+self.stateLineEdit.text()+'</State>\n')
            f.write('\t<ZIP>'+self.zipLineEdit.text()+'</ZIP>\n')
            f.write('\t<Email>'+self.emailLineEdit.text()+'</Email>\n')
            f.write('</user>')
        f.close()


    def all_pop(self):
        if self.firstNameLineEdit.text() == "":
            return False
        elif self.lastNameLineEdit.text() == "":
            return False
        elif self.addressLineEdit.text() == "":
            return False
        elif self.cityLineEdit.text() == "":
            return False
        elif self.stateLineEdit.text() == "":
            return False
        elif self.emailLineEdit.text() == "":
            return False
        elif self.zipLineEdit.text() == "":
            return False
        else:
            return True





    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """
        data = []
        with open(filePath,'r') as f:
            data = f.readlines()
            self.firstNameLineEdit.setText(re.search(">.*<",data[2]).group(0).lstrip('>').rstrip('<'))
            self.lastNameLineEdit.setText(re.search(r">.*<",data[3]).group(0).lstrip('>').rstrip('<'))
            self.addressLineEdit.setText(re.search(r">.*<",data[4]).group(0).lstrip('>').rstrip('<'))
            self.cityLineEdit.setText(re.search(r">.*<",data[5]).group(0).lstrip('>').rstrip('<'))
            self.stateLineEdit.setText(re.search(r">.*<",data[6]).group(0).lstrip('>').rstrip('<'))
            self.zipLineEdit.setText(re.search(r">.*<",data[7]).group(0).lstrip('>').rstrip('<'))
            self.emailLineEdit.setText(re.search(r">.*<",data[8]).group(0).lstrip('>').rstrip('<'))
        f.close()

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)




if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
