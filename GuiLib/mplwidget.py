from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

# Matplotlib canvas class to create figure
class MplCanvas(FigureCanvas):
    def __init__(self):
        self.figure = Figure()
        self.axes   = self.figure.subplots()
        FigureCanvas.__init__(self, self.figure)
        FigureCanvas.setSizePolicy(self,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent) 
        self.canvas = MplCanvas()
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.addWidget(self.canvas)





