from ui_signal_gen   import Ui_SignalGenDialog
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtCore    import pyqtSlot, pyqtSignal
from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

import numpy as np

class SignalGenDialog(QDialog, Ui_SignalGenDialog):
    filename=""
    axes_import=None
    canvas_import = None

    def __init__(self, parent=0):
        super().__init__()
        self.setupUi(self)
        self.canvas_import = self.MplWidget_ImportSignal.canvas

    def plot(self, file, canvas):
        fd = open(file, 'r')
        sample_per_signal = sum(1 for line in fd)
        fd.seek(0, 0)
        signal_num = len(fd.readline().split()) - 1
        time = np.zeros(sample_per_signal, dtype = float)
        sample = np.zeros((signal_num, sample_per_signal), dtype = float)
        fd.seek(0, 0)
        for num, line in enumerate(fd):
            iterns = line.split()
            time[num] = iterns[0]
            sample[0][num] = iterns[1]
            print(iterns[0], iterns[1])
        canvas.axes.set_title("Input Signal")
        canvas.axes.plot(time, sample[0])
        canvas.draw()

    @pyqtSlot()
    def on_pushButton_ImportSignal_clicked(self):
        dialog = QFileDialog()
        if dialog.exec():
            self.filename = dialog.selectedFiles()[0]
            self.lineEdit_ImportFile.setText(self.filename)
        self.plot(file = self.filename, canvas = self.canvas_import)