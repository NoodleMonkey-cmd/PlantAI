import json
import time
from pathlib import Path
import time

SAVED_DATA_PATH = Path(__file__).resolve().parent / "Saved_Data.json"

class Userdata:
    def __init__(self):
        self.username = "Jake"
        self.todaystudytime_Minutes = 0
        self.todaystudytime_seconds = 0
        self.points = 0
        self.pointsearnedtoday = 0
        self.currentstreak = 0
        self.sessionstoday = 0
        self.favoritesubject = "Mathematics"
        self.currentstage = "Sprout"
        self.recentsubject = "Physics"
        self.showdesktoppet = 1
        self.plantsize = "Small"
        self.end_session = 0
        self.start_session = 0
        self.last_session_update = 0
        self.last_login = 0
        self.alwaysontop = 0
        self.load()

    def load(self):
        if not SAVED_DATA_PATH.is_file():
            return False
        try:
            with open(SAVED_DATA_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            return False
        if not isinstance(data, dict) or not isinstance(data.get("username"), str):
            return False
        self.username = data["username"]
        self.todaystudytime_Minutes = data["todaystudytime"]
        self.todaystudytime_seconds = data.get(
            "todaystudytime_seconds",
            self.todaystudytime_Minutes * 60,
        )
        self.points = data.get("points", self.points)
        self.pointsearnedtoday = data["pointsearnedtoday"]
        self.currentstreak = data["currentstreak"]
        self.sessionstoday = data["sessionstoday"]
        self.favoritesubject = data["favoritesubject"]
        self.currentstage = data["currentstage"]
        self.recentsubject = data["recentsubject"]
        self.showdesktoppet = data["showdesktoppet"]
        self.plantsize = data.get("plantsize", self.plantsize)
        self.end_session = data.get("end_session", self.end_session)
        self.start_session = data.get("start_session", self.start_session)
        self.last_session_update = data.get(
            "last_session_update",
            self.last_session_update,
        )
        if self.end_session > time.time() and not self.last_session_update:
            self.last_session_update = time.time()

        self.last_login = data["last_login"]
        self.alwaysontop = data["alwaysontop"]
        return True

    def update_username(self, username):
        if not isinstance(username, str):
            raise TypeError("Username must be a string")

        data = {}
        if SAVED_DATA_PATH.is_file():
            try:
                with open(SAVED_DATA_PATH, "r", encoding="utf-8") as file:
                    saved_data = json.load(file)
                if isinstance(saved_data, dict):
                    data = saved_data
            except json.JSONDecodeError:
                pass

        self.username = username
        data["username"] = self.username
        with open(SAVED_DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def save(self, save_points=False):
        data = {}
        if SAVED_DATA_PATH.is_file():
            try:
                with open(SAVED_DATA_PATH, "r", encoding="utf-8") as file:
                    saved_data = json.load(file)
                if isinstance(saved_data, dict):
                    data = saved_data
            except json.JSONDecodeError:
                pass

        saved_points = data.get("points")
        if (
            not save_points
            and not isinstance(saved_points, bool)
            and isinstance(saved_points, (int, float))
            and saved_points >= 0
        ):
            self.points = saved_points

        data.update({
            "username": self.username,
            "todaystudytime": self.todaystudytime_Minutes,
            "todaystudytime_seconds": self.todaystudytime_seconds,
            "points": self.points,
            "pointsearnedtoday": self.pointsearnedtoday,
            "currentstreak": self.currentstreak,
            "sessionstoday": self.sessionstoday,
            "favoritesubject": self.favoritesubject,
            "currentstage": self.currentstage,
            "recentsubject": self.recentsubject,
            "showdesktoppet": self.showdesktoppet,
            "plantsize": self.plantsize,
            "end_session": self.end_session,
            "start_session": self.start_session,
            "last_session_update": self.last_session_update,
            "last_login": self.last_login,
            "alwaysontop": self.alwaysontop
        })

        with open(SAVED_DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_points(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise TypeError("Point amount must be numeric")
        if amount < 0:
            raise ValueError("Point amount cannot be negative")

        if SAVED_DATA_PATH.is_file():
            try:
                with open(SAVED_DATA_PATH, "r", encoding="utf-8") as file:
                    saved_data = json.load(file)
                saved_points = saved_data.get("points", self.points)
                if (
                    not isinstance(saved_points, bool)
                    and isinstance(saved_points, (int, float))
                    and saved_points >= 0
                ):
                    self.points = saved_points
            except json.JSONDecodeError:
                pass

        self.points += amount
        self.pointsearnedtoday += amount
        self.save(save_points=True)
