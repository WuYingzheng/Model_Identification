#!/usr/bin/env python3
import sys, os, time;
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, Qt, QTimer, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QDateTimeEdit, QMessageBox,
        QProgressBar, QWidget)
from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

sys.path.append(os.path.dirname(__file__) + "/GuiLib")
sys.path.append(os.path.dirname(__file__) + "/utility")
from ui_mainwindow import Ui_MainWindow
from SignalGen     import SignalGenDialog
from SignalSample  import SignalSampleDialog
from AboutAuthor   import AboutAuthorDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.flag = 0
        # 定义信号canvas
        signal_figure = Figure(figsize=(5, 2), tight_layout=True)
        signal_canvas = FigureCanvas(signal_figure)
        self.addToolBar(NavigationToolbar(signal_canvas, self))
        # 定义频谱canvas
        spectrum_figure = Figure(figsize=(5, 4), tight_layout=True)
        spectrum_canvas = FigureCanvas(spectrum_figure)
        self.addToolBar(QtCore.Qt.BottomToolBarArea,
            NavigationToolbar(spectrum_canvas, self))

        self.SpectrumLayout.addWidget(signal_canvas)
        self.SpectrumLayout.addWidget(spectrum_canvas)
        # 设置signal_canvas和spectrum_canvas的比例为　1:3
        self.SpectrumLayout.setStretch(1, 3)

        self.signal_axes = signal_canvas.figure.subplots()
        dt = 0.005  # sampling interval
        Fs = 1 / dt  # sampling frequency
        t = np.arange(0, 10, dt)
        # t = np.linspace(0, 10, 501)
        # generate noise:
        nse = np.random.randn(len(t))
        r = np.exp(-t / 0.05)
        cnse = np.convolve(nse, r) * dt
        cnse = cnse[:len(t)]
        # 定义函数信号
        s = 0.1 * np.sin(4 * np.pi * t) + cnse
        # 绘制信号波形图
        self.signal_axes.set_title("Origin Signal")
        self.signal_axes.set_xlabel("Time")
        self.signal_axes.set_ylabel("Amplitude")
        self.signal_axes.plot(t, s, color='C0')

        # 创建两个频谱图：幅度响应／相位响应
        self.spectrum_axes = spectrum_canvas.figure.subplots(nrows=2)
        self.spectrum_axes[0].magnitude_spectrum(s, Fs=Fs, color='C1')
        # 相位响应
        self.spectrum_axes[1].phase_spectrum(s, Fs=Fs, color='C2')

    @pyqtSlot()
    def on_action_SignalGen_triggered(self):
        dialog = SignalGenDialog(self)
        if (dialog.exec()):
            print("ok")

    @pyqtSlot()
    def on_action_SignalSample_triggered(self):
        dialog = SignalSampleDialog(self)
        dialog.exec()

    # qt槽函数，当点击关于系统按钮后会触发该函数
    @pyqtSlot()
    def on_action_AboutSystem_triggered(self):
        _translate = QtCore.QCoreApplication.translate
        #self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        retv = QMessageBox.about(self, _translate("MainWindow", "关于碳滑板振动信号分析系统"),
                _translate("MainWindow", "<html><head/><body><p><span \
                style=\" font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\';\
                font-size:14px; font-weight:600; color:#000000;\
                \">碳滑板振动信号分析系统  </span><span style=\"\
                font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\';\
                font-size:14px; color:#000000;\">v0.01</span></p><p><span style=\"\
                font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\';\
                font-size:14px; color:#000000;\
                \">本软件用于受电弓碳滑板振动信号分析. 本软件基于 Python3 - Qt5</span></p><p><span\
                style=\" font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\';\
                font-size:14px; color:#000000;\
                \">已实现功能如下：</span></p><p><span\
                style=\" font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\';\
                font-size:14px; color:#000000;\
                \">    1. 相关性分析</span></p><p><span\
                style=\" font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\';\
                font-size:14px; color:#000000;\
                \">    2. 功率普分析</span></p><p><span\
                style=\" font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\';\
                font-size:14px; color:#000000;\
                \">    3. 冲击响应分析</span></p><p><span\
                style=\" font-family:\'Droid Sans Mono,monospace,monospace,Droid Sans Fallback\';\
                font-size:12pt; color:#aa0000; vertical-align:super;\
                \">Copyright &copy; 2019 黄超. All rights reserved.</span></p></body></html>")
                )
    # qt槽函数，当点击关于作者按钮后会触发该函数
    @pyqtSlot()
    def on_action_AboutAuthor_triggered(self):
        dialog = AboutAuthorDialog()
        dialog.exec()

qapp = QApplication(sys.argv)
app = MainWindow()
app.show()
sys.exit(qapp.exec_())
