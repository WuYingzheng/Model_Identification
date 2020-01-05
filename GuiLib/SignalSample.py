from PyQt5.QtWidgets  import QDialog, QFileDialog, QComboBox
from PyQt5.QtCore     import pyqtSlot, pyqtSignal
from ui_signal_sample import Ui_SignalSampleDialog
from sample           import Sample

class SignalSampleDialog(QDialog, Ui_SignalSampleDialog):
    file_stimulus = ""
    file_response = ""
    sample_stimulus = None
    sample_response = None
    plot_mode = 0             # 0: time 1: frequence

    def __init__(self, parent=0):
        super().__init__()
        self.setupUi(self)
        self.comboBox_Domain.activated[int].connect(self.comboBox_Domain_activated)

    @pyqtSlot()
    def on_pushButton_OpenStimulate_clicked(self):
        dialog = QFileDialog(self)
        if dialog.exec():
            self.file_stimulus = dialog.selectedFiles()[0]
            self.lineEdit_Stimulate.setText(self.file_stimulus)
            self.sample_stimulus = Sample(file=self.file_stimulus)
            self.plot(self.MplWidget_Stimulate.canvas,
                self.sample_stimulus, "Input Signal")

    @pyqtSlot()
    def on_pushButton_OpenResponse_clicked(self):
        dialog = QFileDialog(self)
        if dialog.exec():
            self.file_response = dialog.selectedFiles()[0]
            self.lineEdit_Response.setText(self.file_response)
            self.sample_response = Sample(file=self.file_response)
            self.plot(self.MplWidget_Response.canvas,
                self.sample_response, "Output Signal")

    @pyqtSlot()
    def plot(self, canvas, sample, title = "signal"):
        canvas.axes.clear()
        canvas.axes.set_title(title)
        if(self.plot_mode):
            canvas.axes.magnitude_spectrum(sample.sample[0], Fs=20480, color='C1')
        else:
            canvas.axes.plot(sample.time, sample.sample[0])
        canvas.draw()

    @pyqtSlot()
    def comboBox_Domain_activated(self):
        self.plot_mode = self.comboBox_Domain.currentIndex()
        if (self.sample_stimulus):
            self.plot(self.MplWidget_Stimulate.canvas,
                self.sample_stimulus, "Input Signal")
        if (self.sample_response):
            self.plot(self.MplWidget_Response.canvas,
                self.sample_response, "Output Signal")
