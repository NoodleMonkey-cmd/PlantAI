import json
from pathlib import Path

SAVED_DATA_PATH = Path(__file__).resolve().parent / "Saved_Data.json"


class Userdata:
    def __init__(self):
        self.username = "Jake"
        self.todaystudytime_Minutes = 0
        self.pointsearnedtoday = 0
        self.currentstreak = 0
        self.sessionstoday = 0
        self.favoritesubject = "Mathematics"
        self.currentstage = "Sprout"
        self.recentsubject = "Physics"
        self.showdesktoppet = 1
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
        self.pointsearnedtoday = data["pointsearnedtoday"]
        self.currentstreak = data["currentstreak"]
        self.sessionstoday = data["sessionstoday"]
        self.favoritesubject = data["favoritesubject"]
        self.currentstage = data["currentstage"]
        self.recentsubject = data["recentsubject"]
        self.showdesktoppet = data["showdesktoppet"]
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

    def save(self):
        data = {
            "username": self.username,
            "todaystudytime": self.todaystudytime_Minutes,
            "pointsearnedtoday": self.pointsearnedtoday,
            "currentstreak": self.currentstreak,
            "sessionstoday": self.sessionstoday,
            "favoritesubject": self.favoritesubject,
            "currentstage": self.currentstage,
            "recentsubject": self.recentsubject,
            "showdesktoppet": self.showdesktoppet,
        }

        with open(SAVED_DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)