import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_studybloom import Ui_MainWindow

class StudyBloomWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Default Page
        self.ui.stackedWidget.setCurrentIndex(1)

        # Buttons
        self.ui.Button_Setting.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Page_Settings)
        )

        self.ui.Button_Summary.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Page_Summary)
        )


app = QApplication(sys.argv)

window = StudyBloomWindow()
window.show()

app.exec()