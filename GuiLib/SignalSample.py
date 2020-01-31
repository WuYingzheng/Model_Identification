from PyQt5.QtWidgets  import QDialog, QFileDialog, QComboBox, QListWidgetItem
from PyQt5.QtCore     import pyqtSlot, pyqtSignal, QCoreApplication
from ui_signal_sample import Ui_SignalSampleDialog
from sample           import Sample

import scipy.fftpack
import numpy as np

class SignalSampleDialog(QDialog, Ui_SignalSampleDialog):
    file_stimulus = ""
    file_response = ""
    sample_stimulus = None
    sample_response = None
    plot_mode = 0             # 0: time 1: frequence
    stimulus_idx = 0
    response_channel = 0
    response_idx = 0

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
            # update list view
            num = self.sample_stimulus.signum
            _translate = QCoreApplication.translate
            for i in range(num):
                name = "Force " + str(i)
                item = QListWidgetItem()
                item.setText(_translate("SignalSampleDialog", name))
                self.listWidget_Stimulate.addItem(item)

            self.plot(self.MplWidget_Stimulate.canvas,
                self.sample_stimulus, title = "Input Signal")

    @pyqtSlot(int)
    def on_listWidget_Stimulate_currentRowChanged(self, idx):
        self.stimulus_idx = idx
        self.plot(self.MplWidget_Stimulate.canvas,
            self.sample_stimulus,
            idx = idx,
            title = "Input Signal")

    @pyqtSlot(int)
    def on_listWidget_Response_currentRowChanged(self, idx):
        self.response_idx = idx
        self.plot(self.MplWidget_Response.canvas,
            self.sample_response,
            idx = idx,
            title = "Output Signal")

    @pyqtSlot()
    def on_pushButton_OpenResponse_clicked(self):
        dialog = QFileDialog(self)
        if dialog.exec():
            self.file_response = dialog.selectedFiles()[0]
            self.lineEdit_Response.setText(self.file_response)
            self.sample_response = Sample(file=self.file_response)
            _translate = QCoreApplication.translate
            num = self.sample_response.signum
            for i in range(num):
                name = "Response " + str(i)
                item = QListWidgetItem()
                item.setText(_translate("SignalSampleDialog", name))
                self.listWidget_Response.addItem(item)
            self.plot(self.MplWidget_Response.canvas,
                self.sample_response, title = "Output Signal")

    @pyqtSlot()
    def plot(self, canvas, sample, idx=0, title = "signal"):
        canvas.axes.clear()
        canvas.axes.set_title(title)
        if not sample:
            print("Sample is empty, please import again.")
            return -1
        sequence = sample.sample[idx]
        if(self.plot_mode):
            #canvas.axes.magnitude_spectrum(sample.sample[0], Fs=20480, color='C1')
            N = len(sample.time)        # 采样个数
            time = sample.time[N-1]- sample.time[0]
            T = time / N                # 采样周期
            yf = scipy.fftpack.fft(sequence)
            xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
            canvas.axes.plot(xf, 2.0/N * np.abs(yf[:N//2]))
            if canvas is self.MplWidget_Response.canvas:
                # freqence domain
                thred = self.doubleSpinBox_UpperFrequence.value()
                canvas.axes.set_xlim(right=thred)                
        else:
            canvas.axes.plot(sample.time, sequence)
        canvas.axes.set_xlim(left=0)
        canvas.draw()

    @pyqtSlot()
    def comboBox_Domain_activated(self):
        self.plot_mode = self.comboBox_Domain.currentIndex()
        if (self.sample_stimulus):
            self.plot(self.MplWidget_Stimulate.canvas,
                self.sample_stimulus, title = "Input Signal")
        if (self.sample_response):
            self.plot(self.MplWidget_Response.canvas,
                self.sample_response, title = "Output Signal")

