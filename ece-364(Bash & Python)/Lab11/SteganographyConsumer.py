import sys
from functools import partial
from os.path import splitext
from SteganographyGUI import *
from PySide.QtCore import *
from PySide.QtGui import *
from Steganography import *
import scipy.misc
import numpy as np

class SteganographyConsumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(SteganographyConsumer, self).__init__(parent)
        self.pload_filepath = ''
        self.carr_filepath = ''
        self.payload_flag = 0
        self.carrier_flag = 0
        self.payload_array=0
        self.carrier_array=0
        self.compression = -1
        self.setupUi(self)
        self.chkApplyCompression.stateChanged.connect(lambda :self.compression_changed())
        self.slideCompression.valueChanged.connect(lambda:self.slider_moved())
        self.chkOverride.stateChanged.connect(lambda:self.override_chkd())
        self.btnSave.clicked.connect(lambda:self.save())
        self.btnClean.clicked.connect(lambda:self.clean())
        self.btnExtract.clicked.connect(lambda:self.extract())

        # Get the views that are required to have the drag-and-drop enabled.
        views = [self.viewPayload1, self.viewCarrier1, self.viewCarrier2]
        accept = lambda e: e.accept()

        for view in views:
            # We need to accept the drag event to be able to accept the drop.
            view.dragEnterEvent = accept
            view.dragMoveEvent = accept
            view.dragLeaveEvent = accept

            # Assign an event handler (a method,) to be invoked when a drop is performed.
            view.dropEvent = partial(self.processDrop, view)

        # NOTE: The line above links "all" views to the same function, and passes the view as a parameter in the
        # function. You could pass more than one widget to the function by adding more parameters to the signature,
        # in case you want to bind more than one widget together. you can even pass in another function, as a parameter,
        # which might significantly reduce the size of your code. Finally, if you prefer to have a separate function
        # for each view, where the view name is, say, "someView", you will need to:
        # 1- Create a function with a definition similar: funcName(self, e)
        # 2- Assign the function to be invoked as the event handler:
        #   self.someView.dropEvent = self.funcName


    def clean(self):
        pload_img = scipy.misc.imread(self.filePath)
        carrier = Carrier(pload_img)
        cleaned_image = carrier.clean()
        scipy.misc.imsave("cleaned.png",cleaned_image)
        self.display_image(self.viewCarrier2,'cleaned.png')
        self.btnExtract.setDisabled(True)
        self.btnClean.setDisabled(True)
        self.lblCarrierEmpty.setText(">>>> Carrier Empty <<<<")

    def extract(self):
        pload_img = scipy.misc.imread(self.filePath)
        carrier = Carrier(pload_img)
        pload = carrier.extractPayload()
        scipy.misc.imsave("extracted.png",pload.img)
        self.display_image(self.viewPayload2,'extracted.png')

    def override_chkd(self):
        if self.chkOverride.isChecked() and self.txtPayloadSize.text() != '0':
            self.btnSave.setEnabled(True)
        else:
            self.btnSave.setDisabled(True)

    def save(self):
        if self.chkOverride.isChecked():
            override = True
        else:
            override = False

        filePath, _ = QFileDialog.getSaveFileName(self, caption='Embed Payload into Carrier', filter="PNG files (*.png)")

        payload = Payload(self.payload_array,compressionLevel=self.compression)
        carrier = Carrier(self.carrier_array)
        image = carrier.embedPayload(payload,override)

        scipy.misc.imsave(filePath,image)



    def compression_changed(self):
        if self.chkApplyCompression.isChecked():
            self.slideCompression.setEnabled(True)
            self.txtCompression.setEnabled(True)
            self.setPloadSize(self.txtPayloadSize,self.pload_filepath,compression=self.slideCompression.value())
        else:
            self.slideCompression.setEnabled(False)
            self.txtCompression.setEnabled(False)
            self.setPloadSize(self.txtPayloadSize,self.pload_filepath,compression=-1)


    def slider_moved(self):
        self.txtCompression.setText(str(self.slideCompression.value()))
        self.setPloadSize(self.txtPayloadSize,self.pload_filepath,compression=self.slideCompression.value())
        self.compression = self.slideCompression.value()

    def display_image(self,view,filePath):
        frame = QGraphicsScene()
        img = QPixmap(filePath)
        img = img.scaled(355,280, Qt.KeepAspectRatio)
        frame.addPixmap(img)
        view.setScene(frame)
        view.show()


    def setPloadSize(self,item,filePath,compression =-1):
        pload_img = scipy.misc.imread(filePath) #converting the file into an ndarray
        pload = Payload(pload_img,compression)
        pload_xml = pload.xml              # main data in the xml of the payload
        if item == self.txtCarrierSize:
            item.setText(str(int(len(pload_xml)/8)))
        else:
            item.setText(str(len(pload_xml)))



    def processDrop(self, view, e):
        """
        Process a drop event when it occurs on the views.
        """
        mime = e.mimeData()

        # Guard against types of drops that are not pertinent to this app.
        if not mime.hasUrls():
            return

        # Obtain the file path using the OS format.
        filePath = mime.urls()[0].toLocalFile()
        _, ext = splitext(filePath)

        if not ext == ".png":
            return

        # Now the file path is ready to be processed.

        #1)First read image from file, convert it into ndarray and find its size
        self.filePath = filePath         #making filePath accesible to all functions
        self.display_image(view,filePath)

        if view == self.viewPayload1:
            self.pload_filepath = filePath
            item = self.txtPayloadSize
            pload_img = scipy.misc.imread(self.pload_filepath) #converting the file into an ndarray
            self.setPloadSize(item,self.pload_filepath)
            self.chkApplyCompression.setChecked(False)
            self.slideCompression.setValue(0)
            self.slideCompression.setDisabled(True)
            self.txtCompression.setText('0')
            self.txtCompression.setDisabled(True)
            self.payload_flag = 1
            self.payload_array = pload_img

        elif view == self.viewCarrier1:
            self.carr_filepath = filePath
            item = self.txtCarrierSize
            self.setPloadSize(item,self.carr_filepath)
            pload_img = scipy.misc.imread(self.carr_filepath) #converting the file into an ndarray
            carrier = Carrier(pload_img)
            if carrier.payloadExists():
                self.lblPayloadFound.setText(">>>> Payload Found <<<<")
                self.chkOverride.setEnabled(True)
            else:
                self.lblPayloadFound.clear()
                self.chkOverride.setEnabled(False)
            self.carrier_flag = 1
            self.carrier_array = pload_img

        else:
            pload_img = scipy.misc.imread(filePath) #converting the file into an ndarray
            carrier = Carrier(pload_img)
            if not carrier.payloadExists():
                self.lblCarrierEmpty.setText(">>>> Carrier Empty <<<<")
                self.btnExtract.setDisabled(True)
                self.btnClean.setDisabled(True)
            else:
                self.lblCarrierEmpty.clear()
                self.btnExtract.setDisabled(False)
                self.btnClean.setDisabled(False)

        if self.carrier_flag == 1 and self.payload_flag == 1:
            carrier_size = int(self.txtCarrierSize.text())
            payload_size = int(self.txtPayloadSize.text())
            if self.lblPayloadFound.text() == "" or self.chkOverride.isChecked() == True and carrier_size >= payload_size and self.txtPayloadSize.text() != '0':
                self.btnSave.setEnabled(True)
            else:
                self.btnSave.setEnabled(False)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = SteganographyConsumer()
    currentForm.show()
    currentApp.exec_()
