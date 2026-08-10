import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_studybloom import Ui_MainWindow
from Modules.UserData import Userdata

userdata = Userdata()
class StudyBloomWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Default Page
        self.ui.stackedWidget.setCurrentIndex(1)

        # Setting up
        self.ui.Label_Welcome.setText(f"Welcome, {userdata.username}")
        self.ui.Entry_Name.setText(userdata.username)
        self.ui.Entry_Name.editingFinished.connect(self.save_username)

        TodayStudyTime_Minutes = userdata.todaystudytime_Minutes
        if TodayStudyTime_Minutes < 60:
            self.ui.Label_StudyTimeValue.setText(f"{TodayStudyTime_Minutes}min")
        elif TodayStudyTime_Minutes >= 60:
            hr = TodayStudyTime_Minutes // 60
            minu = TodayStudyTime_Minutes - (60 * hr)
            self.ui.Label_StudyTimeValue.setText(f"{hr}h {minu}")

        self.ui.Label_PointsEarnedValue.setText(f"{userdata.pointsearnedtoday}")
        self.ui.Label_StudyLabel_15.setText(f"{userdata.pointsearnedtoday}")

        self.ui.Label_CurrentStreakValue.setText(f"{userdata.currentstreak}")

        self.ui.Label_SessionTodayValue.setText(f"{userdata.sessionstoday}")
        self.ui.Label_StudyLabel_14.setText(f"{userdata.sessionstoday} sessions")

        self.ui.Label_Welcome_2.setText(f"{userdata.favoritesubject}")

        self.ui.Label_Welcome_3.setText(f"{userdata.currentstage}")

        self.ui.Label_Welcome_4.setText(f"{userdata.recentsubject}")

        self.ui.CheckBox_ShowDesktopPlant.setChecked(userdata.showdesktoppet)
        self.ui.CheckBox_ShowDesktopPlant.toggled.connect(
            self.save_show_desktop_pet
        )

        # Buttons
        self.ui.Button_Setting.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Page_Settings)
        )

        self.ui.Button_Summary.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Page_Summary)
        )

        self.ui.Button_Study.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Page_Study)
        )

    def save_username(self):
        userdata.update_username(self.ui.Entry_Name.text())
        self.ui.Label_Welcome.setText(f"Welcome, {userdata.username}")

    def save_show_desktop_pet(self, checked):
        userdata.showdesktoppet = checked
        userdata.save()

app = QApplication(sys.argv)

window = StudyBloomWindow()
window.show()

app.exec()
