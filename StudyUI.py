import sys
import math
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_studybloom import Ui_MainWindow
from Modules.UserData import Userdata
import time
from datetime import datetime, date

from Modules.PointSystem import Sprout, Sprout_Name

userdata = Userdata()
class StudyBloomWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.setupUi(self)

        self.drag_position = None
        self.ui.TopFrane.installEventFilter(self)

        # Default Page
        self.ui.stackedWidget.setCurrentIndex(1)

        self.CheckNewday()

        # Setting up
        self.ui.Label_Welcome.setText(f"Welcome, {userdata.username}")
        self.ui.Entry_Name.setText(userdata.username)
        self.ui.Entry_Name.editingFinished.connect(self.save_username)

        self.update_study_time_display()

        self.ui.Label_PointsEarnedValue.setText(f"{userdata.pointsearnedtoday}")
        self.ui.Label_StudyLabel_15.setText(f"{userdata.pointsearnedtoday}")

        self.ui.Label_CurrentStreakValue.setText(f"{userdata.currentstreak}")

        self.ui.Label_SessionTodayValue.setText(f"{userdata.sessionstoday}")
        self.ui.Label_StudyLabel_14.setText(f"{userdata.sessionstoday} sessions")

        self.ui.Label_Welcome_2.setText(f"{userdata.favoritesubject}")

        self.ui.Label_Welcome_3.setText(f"{userdata.currentstage}")

        self.ui.Label_Welcome_4.setText(f"{userdata.recentsubject}")

        self.center_summary_card_text()

        self.ui.CheckBox_ShowDesktopPlant.setChecked(userdata.showdesktoppet)
        self.ui.CheckBox_ShowDesktopPlant.toggled.connect(
            self.save_show_desktop_pet
        )

        self.ui.CheckBox_AlwaysOnTop.setChecked(
            userdata.alwaysontop
        )
        self.ui.CheckBox_AlwaysOnTop.toggled.connect(
            self.UpdateAlwaysOnTopToggle
        )

        self.ui.CheckBox_RememberPlantPosition.toggled.connect(
            self.save_remember_plant_position
        )

        self.ui.DropdownMenu_PlantSize.setCurrentText(userdata.plantsize)
        self.ui.DropdownMenu_PlantSize.currentTextChanged.connect(
            self.save_plant_size
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

        self.ui.Button_StartSession.clicked.connect(
            self.StartTimer
        )

        self.ui.Button_RestartSession.clicked.connect(
            self.StartTimer
        )

        self.ui.Button_RestartSession_2.clicked.connect(
            self.StopTimer
        )

        self.ui.Buttom_Close.clicked.connect(
            self.close
        )

        self.ui.Button_Minimize.clicked.connect(
            self.showMinimized
        )

        # Toggles

        # Timer Integration
        self.session_timer = QTimer(self)
        self.session_timer.setTimerType(Qt.TimerType.PreciseTimer)
        self.session_timer.setInterval(100)
        self.session_timer.timeout.connect(self.UpdateTimer)
        self.UpdateTimer()

    def center_summary_card_text(self):
        summary_cards = (
            (
                self.ui.Frame_FavoriteSubject,
                self.ui.Label_SubText_9,
                self.ui.Label_Welcome_2,
            ),
            (
                self.ui.Framel_CurrentFlowerStage,
                self.ui.Label_SubText_11,
                self.ui.Label_Welcome_3,
            ),
            (
                self.ui.Frame_RecentSession,
                self.ui.Label_SubText_13,
                self.ui.Label_Welcome_4,
            ),
        )

        for card, subheading, value in summary_cards:
            for label in (subheading, value):
                geometry = label.geometry()
                label.setGeometry(0, geometry.y(), card.width()-7, geometry.height())
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def UpdateTimer(self):
        current_time = time.time()
        self.record_elapsed_study_time(current_time)

        remaining_seconds = max(0, math.ceil(userdata.end_session - time.time()))

        hours, remaining_seconds = divmod(remaining_seconds, 3600)
        minutes, seconds = divmod(remaining_seconds, 60)

        self.ui.Label_Hour.setText(f"{hours:02}:")
        self.ui.Label_Minute.setText(f"{minutes:02}:")
        self.ui.Label_Second.setText(f"{seconds:02}")

        self.update_study_time_display()

        if userdata.end_session > current_time:
            self.ui.Label_StudyLabel_12.setText("Studying")
            if not self.session_timer.isActive():
                self.session_timer.start()
            userdata.save()
        else:
            self.ui.Label_StudyLabel_12.setText("Not studying")
            self.session_timer.stop()

            if userdata.end_session:
                self.UpdateSubjectStats()
                self.UpdateSession()
                self.UpdateStreak()
                self.UpdatePoints()
                self.UpdateCurrentStage()
                userdata.save(save_points=True)

                self.ui.Label_CurrentStreakValue.setText(f"{userdata.currentstreak}")

                userdata.end_session = 0
                userdata.last_session_update = 0

                userdata.save()

    def record_elapsed_study_time(self, current_time):
        if not userdata.end_session or not userdata.last_session_update:
            return

        count_until = min(current_time, userdata.end_session)
        elapsed_seconds = max(0, count_until - userdata.last_session_update)
        userdata.todaystudytime_seconds += elapsed_seconds
        userdata.todaystudytime_Minutes = int(
            userdata.todaystudytime_seconds // 60
        )
        userdata.last_session_update = count_until

    def update_study_time_display(self):
        total_minutes = int(userdata.todaystudytime_seconds // 60)
        userdata.todaystudytime_Minutes = total_minutes
        hours, minutes = divmod(total_minutes, 60)

        if hours:
            self.ui.Label_StudyTimeValue.setText(f"{hours}h {minutes}")
        else:
            self.ui.Label_StudyTimeValue.setText(f"{minutes}min")

        self.ui.Label_StudyLabel_13.setText(f"{total_minutes} min")

    def StartTimer(self):
        try:
            session_length_minutes = int(self.ui.Lineedit_SessionLength.text())
        except ValueError:
            return

        if session_length_minutes <= 0:
            return

        current_time = time.time()
        self.record_elapsed_study_time(current_time)

        userdata.start_session = session_length_minutes
        userdata.end_session = current_time + (session_length_minutes * 60)
        userdata.last_session_update = current_time
        userdata.save()

        minute_label = "minute" if session_length_minutes == 1 else "minutes"
        self.ui.Label_SmallTimeLimit.setText(
            f"{session_length_minutes} {minute_label}"
        )
        self.UpdateTimer()

    def StopTimer(self):
        self.record_elapsed_study_time(time.time())
        self.session_timer.stop()
        userdata.end_session = 0
        userdata.last_session_update = 0
        userdata.save()
        self.UpdateTimer()

    def UpdateSession(self):
        userdata.sessionstoday += 1
        userdata.save()

        self.ui.Label_SessionTodayValue.setText(f"{userdata.sessionstoday}")
        self.ui.Label_StudyLabel_14.setText(f"{userdata.sessionstoday} sessions")

    def UpdateStreak(self):
        today = datetime.now().date()

        if userdata.last_login == [0, 0, 0]:
            userdata.last_login = [today.year, today.month, today.day]
            userdata.currentstreak = 1
            userdata.save()
            return

        last_login = date(userdata.last_login[0], userdata.last_login[1], userdata.last_login[2])
        day_passed = (today - last_login).days

        if day_passed == 1:
            userdata.currentstreak += 1
        elif day_passed > 1:
            userdata.currentstreak = 1

        userdata.last_login = [today.year, today.month, today.day]
        userdata.save()

    def CheckNewday(self):
        today = datetime.now().date()
        today_list = [today.year, today.month, today.day]

        if userdata.last_daily_reset != today_list:
            userdata.last_daily_reset = today_list

            userdata.sessionstoday = 0
            userdata.pointsearnedtoday = 0
            userdata.todaystudytime_Minutes = 0
            userdata.todaystudytime_seconds = 0

        userdata.save()

    def UpdateSubjectStats(self):
        subject = self.ui.comboBox_subject.currentText()
        minutes = userdata.start_session

        if subject not in userdata.subject_study_time:
            userdata.subject_study_time[subject] = 0

        userdata.recentsubject = subject
        userdata.subject_study_time[subject] += minutes
        userdata.favoritesubject = max(userdata.subject_study_time, key=userdata.subject_study_time.get)

        self.ui.Label_Welcome_2.setText(userdata.favoritesubject)
        self.ui.Label_Welcome_4.setText(userdata.recentsubject)

    def UpdatePoints(self):
        points_earned = userdata.start_session
        userdata.add_points(points_earned)

        self.ui.Label_PointsEarnedValue.setText(f"{userdata.pointsearnedtoday}")
        self.ui.Label_StudyLabel_15.setText(f"{userdata.pointsearnedtoday}")

    def UpdateAlwaysOnTopToggle(self, checked):
        userdata.alwaysontop = checked
        userdata.save()

    def UpdateCurrentStage(self):
        stage_index = sum(
            userdata.points >= required_points
            for required_points in Sprout
        )
        stage_index = min(stage_index, len(Sprout_Name) - 1)
        userdata.currentstage = Sprout_Name[stage_index]
        self.ui.Label_Welcome_3.setText(f"{userdata.currentstage}")

        userdata.save()

    def save_username(self):
        userdata.update_username(self.ui.Entry_Name.text())
        self.ui.Label_Welcome.setText(f"Welcome, {userdata.username}")

    def save_show_desktop_pet(self, checked):
        userdata.showdesktoppet = checked
        userdata.save()

    def save_plant_size(self, plant_size):
        userdata.plantsize = plant_size
        userdata.save()

    def save_remember_plant_position(self, checked):
        userdata.rememberplantposition = checked
        userdata.save()

    def eventFilter(self, obj, event):
        if obj == self.ui.TopFrane:

            if event.type() == event.Type.MouseButtonPress:
                if event.button() == Qt.LeftButton:
                    self.drag_position = (event.globalPosition().toPoint() - self.frameGeometry().topLeft())

            elif event.type() == event.Type.MouseMove:
                if (event.buttons() & Qt.LeftButton and self.drag_position is not None):
                    self.move(event.globalPosition().toPoint() - self.drag_position)

            elif event.type() == event.Type.MouseButtonRelease:
                self.drag_position = None

        return super().eventFilter(obj, event)

app = QApplication(sys.argv)

window = StudyBloomWindow()
window.show()

app.exec()
