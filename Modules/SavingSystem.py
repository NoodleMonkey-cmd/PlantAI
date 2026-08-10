import json
from pathlib import Path

SAVED_DATA_PATH = Path(__file__).resolve().parent / "Saved_Data.json"

class SavingSystem:
    def __init__(self, animation_handler, point_system, userdata):
        self.animation_handler = animation_handler
        self.point_system = point_system
        self.userdata = userdata

    def save(self):
        username = self.userdata.username
        if SAVED_DATA_PATH.is_file():
            try:
                with open(SAVED_DATA_PATH, "r", encoding="utf-8") as file:
                    saved_data = json.load(file)
                if isinstance(saved_data, dict) and isinstance(saved_data.get("username"), str):
                    username = saved_data["username"]
            except json.JSONDecodeError:
                pass

        self.userdata.username = username
        data = {
            "animation_index": self.animation_handler.Animation_index,
            "points": self.point_system.points,
            "username": self.userdata.username,
            "todaystudytime": self.userdata.todaystudytime_Minutes,
            "pointsearnedtoday": self.userdata.pointsearnedtoday,
            "currentstreak": self.userdata.currentstreak,
            "sessionstoday": self.userdata.sessionstoday,
            "favoritesubject": self.userdata.favoritesubject,
            "currentstage": self.userdata.currentstage,
            "recentsubject": self.userdata.recentsubject,
            "showdesktoppet": self.userdata.showdesktoppet
        }
        try:
            json.dumps(data)
        except (TypeError, ValueError) as error:
            raise TypeError("Flag 8") from error
        with open(SAVED_DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load(self):
        if not SAVED_DATA_PATH.is_file():
            return False
        try:
            with open(SAVED_DATA_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            return False
        if not isinstance(data, dict):
            raise ValueError("Flag 8")

        animation_index = data.get("animation_index")
        points = data.get("points")
        username = data.get("username", self.userdata.username)
        todaystudytime = data.get("todaystudytime")
        pointsearnedtoday = data.get("pointsearnedtoday")
        currentstreak = data.get("currentstreak")
        sessionstoday = data.get("sessionstoday")
        favoritesubject = data.get("favoritesubject")
        currentstage = data.get("currentstage")
        recentsubject = data.get("recentsubject")
        showdesktoppet = data.get("showdesktoppet")

        if (isinstance(animation_index, bool) or not isinstance(animation_index, int)) or (
            isinstance(points, bool) or not isinstance(points, (int, float))
        ):
            raise TypeError("Flag 8")
        if not isinstance(username, str):
            raise TypeError("Flag 8")
        if not 0 <= animation_index < len(self.animation_handler.Animation_Frames) or points < 0:
            raise ValueError("Flag 8")

        self.animation_handler.Animation_index = animation_index
        self.point_system.points = points
        self.userdata.username = username
        self.userdata.todaystudytime_Minutes = todaystudytime
        self.userdata.pointsearnedtoday = pointsearnedtoday
        self.userdata.currentstreak = currentstreak
        self.userdata.sessionstoday = sessionstoday
        self.userdata.favoritesubject = favoritesubject
        self.userdata.currentstage = currentstage
        self.userdata.recentsubject = recentsubject
        self.userdata.showdesktoppet = showdesktoppet
        return True
