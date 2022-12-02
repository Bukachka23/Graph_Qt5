from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from graph import *

# The main window
class UiMainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Background gradient
        p = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0, 0, 0, 400)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(120, 0, 120))
        p.setBrush(QtGui.QPalette.Window, QtGui.QBrush(gradient))
        MainWindow.setPalette(p)

        self.font = QtGui.QFont()
        self.font.setPointSize(12)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 260, 400, 300))
        self.widget.setObjectName("widget")

        self.graphSizeLine = QtWidgets.QLineEdit(self.centralwidget)
        self.graphSizeLine.setGeometry(QtCore.QRect(230, 40, 60, 30))
        self.graphSizeLine.setFont(self.font)
        self.graphSizeLine.setObjectName("graphSizeLine")

        self.graphSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.graphSizeLabel.setGeometry(QtCore.QRect(40, 40, 165, 30))
        self.graphSizeLabel.setFont(self.font)
        self.graphSizeLabel.setObjectName("graphSizeLabel")

        self.graphSizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.graphSizeButton.setGeometry(QtCore.QRect(320, 40, 121, 30))
        self.graphSizeButton.setFont(self.font)
        self.graphSizeButton.setObjectName("graphSizeButton")

        self.sourceLabel = QtWidgets.QLabel(self.centralwidget)
        self.sourceLabel.setGeometry(QtCore.QRect(40, 90, 40, 30))
        self.sourceLabel.setFont(self.font)
        self.sourceLabel.setObjectName("sourceLabel")

        self.targetLabel = QtWidgets.QLabel(self.centralwidget)
        self.targetLabel.setGeometry(QtCore.QRect(180, 90, 40, 30))
        self.targetLabel.setFont(self.font)
        self.targetLabel.setObjectName("targetLabel")

        self.weightLabel = QtWidgets.QLabel(self.centralwidget)
        self.weightLabel.setGeometry(QtCore.QRect(320, 90, 50, 30))
        self.weightLabel.setFont(self.font)
        self.weightLabel.setObjectName("weightLabel")

        self.weightLine = QtWidgets.QLineEdit(self.centralwidget)
        self.weightLine.setGeometry(QtCore.QRect(380, 90, 60, 30))
        self.weightLine.setFont(self.font)
        self.weightLine.setObjectName("weightLine")

        self.addEdgeButton = QtWidgets.QPushButton(self.centralwidget)
        self.addEdgeButton.setGeometry(QtCore.QRect(40, 140, 180, 30))
        self.addEdgeButton.setFont(self.font)
        self.addEdgeButton.setObjectName("addEdgeButton")

        self.graphList = QtWidgets.QListWidget(self.centralwidget)
        self.graphList.setGeometry(QtCore.QRect(510, 260, 250, 300))
        self.graphList.setObjectName("graphList")

        self.pathMethod = QtWidgets.QComboBox(self.centralwidget)
        self.pathMethod.setGeometry(QtCore.QRect(510, 140, 150, 30))
        self.pathMethod.setFont(self.font)
        self.pathMethod.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.pathMethod.setEditable(False)
        self.pathMethod.setMaxVisibleItems(4)
        self.pathMethod.setObjectName("pathMethod")
        self.pathMethod.addItem("")
        self.pathMethod.addItem("")
        self.pathMethod.addItem("")

        self.pathButton = QtWidgets.QPushButton(self.centralwidget)
        self.pathButton.setGeometry(QtCore.QRect(680, 140, 80, 30))
        self.pathButton.setFont(self.font)
        self.pathButton.setObjectName("pathButton")

        self.pathLabel = QtWidgets.QLabel(self.centralwidget)
        self.pathLabel.setGeometry(QtCore.QRect(510, 230, 250, 30))
        self.pathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pathLabel.setFont(self.font)
        self.pathLabel.setObjectName("pathLabel")

        self.pathNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.pathNameLabel.setGeometry(QtCore.QRect(510, 40, 250, 30))
        self.pathNameLabel.setFont(self.font)
        self.pathNameLabel.setObjectName("pathNameLabel")

        self.addNodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.addNodeButton.setGeometry(QtCore.QRect(260, 140, 180, 30))
        self.addNodeButton.setFont(self.font)
        self.addNodeButton.setObjectName("addNodeButton")

        self.removeNodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeNodeButton.setGeometry(QtCore.QRect(340, 190, 100, 30))
        self.removeNodeButton.setFont(self.font)
        self.removeNodeButton.setStyleSheet("")
        self.removeNodeButton.setObjectName("removeNodeButton")

        self.removeNodeSpin = QtWidgets.QComboBox(self.centralwidget)
        self.removeNodeSpin.setGeometry(QtCore.QRect(260, 190, 60, 30))
        self.removeNodeSpin.setFont(self.font)
        self.removeNodeSpin.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.removeNodeSpin.setEditable(False)
        self.removeNodeSpin.setMaxVisibleItems(4)
        self.removeNodeSpin.setObjectName("removeNodeSpin")

        self.sourceNode = QtWidgets.QComboBox(self.centralwidget)
        self.sourceNode.setGeometry(QtCore.QRect(100, 90, 60, 30))
        self.sourceNode.setFont(self.font)
        self.sourceNode.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.sourceNode.setEditable(False)
        self.sourceNode.setMaxVisibleItems(4)
        self.sourceNode.setObjectName("sourceNode")

        self.targetNode = QtWidgets.QComboBox(self.centralwidget)
        self.targetNode.setGeometry(QtCore.QRect(230, 90, 60, 30))
        self.targetNode.setFont(self.font)
        self.targetNode.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.targetNode.setEditable(False)
        self.targetNode.setMaxVisibleItems(4)
        self.targetNode.setObjectName("targetNode")

        self.pathSourceLabel = QtWidgets.QLabel(self.centralwidget)
        self.pathSourceLabel.setGeometry(QtCore.QRect(510, 90, 40, 30))
        self.pathSourceLabel.setFont(self.font)
        self.pathSourceLabel.setObjectName("pathSourceLabel")

        self.pathTargetLabel = QtWidgets.QLabel(self.centralwidget)
        self.pathTargetLabel.setGeometry(QtCore.QRect(650, 90, 40, 30))
        self.pathTargetLabel.setFont(self.font)
        self.pathTargetLabel.setObjectName("pathTargetLabel")

        self.pathSourceNode = QtWidgets.QComboBox(self.centralwidget)
        self.pathSourceNode.setGeometry(QtCore.QRect(570, 90, 60, 30))
        self.pathSourceNode.setFont(self.font)
        self.pathSourceNode.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.pathSourceNode.setEditable(False)
        self.pathSourceNode.setMaxVisibleItems(4)
        self.pathSourceNode.setObjectName("pathSourceNode")

        self.pathTargetNode = QtWidgets.QComboBox(self.centralwidget)
        self.pathTargetNode.setGeometry(QtCore.QRect(700, 90, 60, 30))
        self.pathTargetNode.setFont(self.font)
        self.pathTargetNode.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.pathTargetNode.setEditable(False)
        self.pathTargetNode.setMaxVisibleItems(4)
        self.pathTargetNode.setObjectName("pathTargetNode")

        self.removeEdgeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeEdgeButton.setGeometry(QtCore.QRect(40, 190, 180, 30))
        self.removeEdgeButton.setFont(self.font)
        self.removeEdgeButton.setObjectName("removeEdgeButton")

        self.graphNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.graphNameLabel.setGeometry(QtCore.QRect(215, 230, 50, 30))
        self.graphNameLabel.setFont(self.font)
        self.graphNameLabel.setObjectName("graphNameLabel")

        MainWindow.setCentralWidget(self.centralwidget)

        # Button handlers
        self.graphSizeButton.clicked.connect(self.__size_enter)
        self.addEdgeButton.clicked.connect(self.__add_edge)
        self.removeEdgeButton.clicked.connect(self.__remove_edge)
        self.addNodeButton.clicked.connect(self.__add_node)
        self.removeNodeButton.clicked.connect(self.__remove_node)
        self.pathButton.clicked.connect(self.__find_path)

        # Logic variables
        self.nodes = []
        self.graph = None
        self.layout = QtWidgets.QVBoxLayout()
        self.canvas = None
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(1, 1, 1, 1)

        buttons = [self.graphSizeButton, self.addEdgeButton, self.removeEdgeButton,
                   self.addNodeButton, self.removeNodeButton, self.pathButton]
        for button in buttons:
            pass

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Графи"))
        self.graphSizeLabel.setText(_translate("MainWindow", "Кількість вершин:"))
        self.graphSizeButton.setText(_translate("MainWindow", "Створити"))
        self.sourceLabel.setText(_translate("MainWindow", "Від:"))
        self.targetLabel.setText(_translate("MainWindow", "До:"))
        self.weightLabel.setText(_translate("MainWindow", "Вага:"))
        self.addEdgeButton.setText(_translate("MainWindow", "Додати ребро"))
        self.pathMethod.setItemText(0, _translate("MainWindow", "Floyd"))
        self.pathMethod.setItemText(1, _translate("MainWindow", "Dijkstra"))
        self.pathMethod.setItemText(2, _translate("MainWindow", "Ford-Bellman"))
        self.pathButton.setText(_translate("MainWindow", "Знайти"))
        self.pathLabel.setText(_translate("MainWindow", "Ребра"))
        self.pathNameLabel.setText(_translate("MainWindow", "Алгоритми пошуку шляху"))
        self.addNodeButton.setText(_translate("MainWindow", "Додати вершину"))
        self.removeNodeButton.setText(_translate("MainWindow", "Видалити"))
        self.pathSourceLabel.setText(_translate("MainWindow", "Від:"))
        self.pathTargetLabel.setText(_translate("MainWindow", "До:"))
        self.removeEdgeButton.setText(_translate("MainWindow", "Видалити ребро"))
        self.graphNameLabel.setText(_translate("MainWindow", "Граф"))
        self.widget.setStyleSheet("background-color: white; border: 1px solid black;")
        self.graphList.setStyleSheet("border: 1px solid black;")

    def __update_graph(self):
        if self.canvas is not None:
            self.layout.removeWidget(self.canvas)

        if self.graph is not None:
            d = Draw(self.graph.adjMatrix, self.graph.size)
            fig = d.draw()
            self.canvas = FigureCanvasQTAgg(fig)
            self.canvas.resize(400, 300)
            self.layout.addWidget(self.canvas)
            self.widget.setLayout(self.layout)
            self.__update_graphList()
        self.widget.update()
        self.centralwidget.update()

    def __size_enter(self):
        size = None
        try:
            size = int(self.graphSizeLine.text())
        except Exception as e:
            print(e)
        if size is not None:
            self.nodes = []
            self.graph = Graph(size)
            for i in range(size):
                self.nodes.append(i)
            self.__update_items()
            self.__update_graph()

    def __add_edge(self):
        if self.graph is None:
            return
        source = int(self.sourceNode.currentText())
        target = int(self.targetNode.currentText())
        try:
            weight = int(self.weightLine.text())
        except Exception as e:
            print(e)
            return
        self.graph.addEdge(source, target, weight)
        self.__update_graph()

    def __remove_edge(self):
        if self.graph is None:
            return
        source = int(self.sourceNode.currentText())
        target = int(self.targetNode.currentText())
        self.graph.removeEdge(source, target)
        self.__update_graph()

    def __add_node(self):
        if self.graph is None:
            self.graph = Graph(1)
            self.nodes.append(0)
        else:
            self.graph.addNode()
            self.nodes.append(self.graph.size - 1)
        self.graph.toString()
        self.__update_items()

    def __remove_node(self):
        if self.graph is None:
            return
        if not len(self.nodes):
            self.graph = None
        else:
            node = int(self.removeNodeSpin.currentText())
            self.graph.removeNode(node)
            self.nodes.remove(node)
            if not len(self.nodes):
                self.graph = None
        self.__update_items()
        self.__update_graph()

    def __update_items(self):
        if self.graph is not None:
            self.graphSizeLine.setText(str(self.graph.size))
        else:
            self.graphSizeLine.setText(str(0))
        self.sourceNode.clear()
        self.targetNode.clear()
        self.pathSourceNode.clear()
        self.pathTargetNode.clear()
        self.removeNodeSpin.clear()
        for i in self.nodes:
            self.sourceNode.addItem(str(i))
            self.targetNode.addItem(str(i))
            self.pathSourceNode.addItem(str(i))
            self.pathTargetNode.addItem(str(i))
            self.removeNodeSpin.addItem(str(i))

    def __update_graphList(self):
        self.graphList.clear()
        self.pathLabel.setText("Ребра")
        self.graphList.setFont(self.font)
        edges = self.graph.getListEdges()
        for i, v in enumerate(edges):
            new_item = QtWidgets.QListWidgetItem(f" Ребро: {v[0]} -> {v[1]} вага: {v[2]}")
            self.graphList.addItem(new_item)
        self.graphList.update()

    def __find_path(self):
        if self.graph is None:
            return
        source = int(self.pathSourceNode.currentText())
        target = int(self.pathTargetNode.currentText())
        if self.pathMethod.currentIndex() == 0:
            path_len, path = self.graph.FloydWarshall(source, target)
        elif self.pathMethod.currentIndex() == 1:
            path_len, path = self.graph.Dijkstra(source, target)
        else:
            path_len, path = self.graph.FordBellman(source, target)
        self.graphList.clear()
        self.pathLabel.setText("Шлях")
        self.graphList.setFont(self.font)
        self.graphList.addItem(f" Метод пошуку:\n {self.pathMethod.currentText()}")
        self.graphList.addItem(f" Із {source} в {target}")
        if path is None:
            if path_len == 0:
                self.graphList.addItem(f" Відстань: {path_len}")
            elif isinf(path_len):
                self.graphList.addItem(f" Шлях не існує")
        else:
            self.graphList.addItem(f" Відстань: {path_len}")
            self.graphList.addItem(" Шлях:")
            add_str = str(" ")
            for i, p in enumerate(path):
                if i != 0:
                    add_str += "->"
                add_str += f"{p}"
            self.graphList.addItem(add_str)
            self.graphList.update()


# UiLoadWindow
class UiLoadWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
        self.label.setMinimumSize(QtCore.QSize(200, 200))
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setObjectName("label")

        # add label to main window
        MainWindow.setCentralWidget(self.centralwidget)

        # set qmovie as label
        self.movie = QtGui.QMovie("graph.gif")
        self.label.setMovie(self.movie)
        self.movie.start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Ui Load Window
    window = QtWidgets.QMainWindow()
    load_window = UiLoadWindow()
    load_window.setupUi(window)
    window.show()
    QtCore.QTimer.singleShot(2000, window.close)
    app.exec_()

    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
