from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QDial, QWidget, QMainWindow, QLabel, QVBoxLayout
import sys


#QT_QPA_PLATFORM = 'wayland'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SitLess")
        #button = QPushButton("Click Me")
        self.setMinimumSize(QSize(400,300))
        self.setCentralWidget(self.Dial_Components())

    def Dial_Components(self):
        container = QWidget()
        layout = QVBoxLayout()

        dial = QDial(self)
        dial.setGeometry(100, 100, 100, 100)
        dial.setNotchesVisible(True)
        dial.setMaximum(0)

        dial.setSingleStep(5)
        dial.setWrapping(False)
        dial.notchSize()

        #Label information 
        label = QLabel("Set how long do you want to reminded?")
        label.setGeometry(200, 200, 200, 200)
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(dial)
        layout.addWidget(label)

        container.setLayout(layout)
        return container

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()