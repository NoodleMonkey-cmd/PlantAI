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
        plantsize = self.userdata.plantsize
        end_session = self.userdata.end_session
        start_session = self.userdata.start_session
        last_session_update = self.userdata.last_session_update
        todaystudytime = self.userdata.todaystudytime_Minutes
        todaystudytime_seconds = self.userdata.todaystudytime_seconds
        if SAVED_DATA_PATH.is_file():
            try:
                with open(SAVED_DATA_PATH, "r", encoding="utf-8") as file:
                    saved_data = json.load(file)
                if isinstance(saved_data, dict) and isinstance(saved_data.get("username"), str):
                    username = saved_data["username"]
                if isinstance(saved_data, dict) and isinstance(saved_data.get("plantsize"), str):
                    plantsize = saved_data["plantsize"]
                if isinstance(saved_data, dict) and isinstance(saved_data.get("end_session"), (int, float)):
                    end_session = saved_data["end_session"]
                if isinstance(saved_data, dict) and isinstance(saved_data.get("start_session"), (int, float)):
                    start_session = saved_data["start_session"]
                if isinstance(saved_data, dict) and isinstance(saved_data.get("last_session_update"), (int, float)):
                    last_session_update = saved_data["last_session_update"]
                if isinstance(saved_data, dict) and isinstance(saved_data.get("todaystudytime"), (int, float)):
                    todaystudytime = saved_data["todaystudytime"]
                if isinstance(saved_data, dict) and isinstance(saved_data.get("todaystudytime_seconds"), (int, float)):
                    todaystudytime_seconds = saved_data["todaystudytime_seconds"]
            except json.JSONDecodeError:
                pass

        self.userdata.username = username
        self.userdata.plantsize = plantsize
        self.userdata.end_session = end_session
        self.userdata.start_session = start_session
        self.userdata.last_session_update = last_session_update
        self.userdata.todaystudytime_Minutes = todaystudytime
        self.userdata.todaystudytime_seconds = todaystudytime_seconds
        data = {
            "animation_index": self.animation_handler.Animation_index,
            "points": self.point_system.points,
            "username": self.userdata.username,
            "todaystudytime": self.userdata.todaystudytime_Minutes,
            "todaystudytime_seconds": self.userdata.todaystudytime_seconds,
            "pointsearnedtoday": self.userdata.pointsearnedtoday,
            "currentstreak": self.userdata.currentstreak,
            "sessionstoday": self.userdata.sessionstoday,
            "favoritesubject": self.userdata.favoritesubject,
            "currentstage": self.userdata.currentstage,
            "recentsubject": self.userdata.recentsubject,
            "showdesktoppet": self.userdata.showdesktoppet,
            "plantsize": self.userdata.plantsize,
            "end_session": self.userdata.end_session,
            "start_session": self.userdata.start_session,
            "last_session_update": self.userdata.last_session_update,
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

        animation_index = data.get("animation_index", self.animation_handler.Animation_index)
        points = data.get("points", self.point_system.points)
        username = data.get("username", self.userdata.username)
        todaystudytime = data.get(
            "todaystudytime",
            self.userdata.todaystudytime_Minutes,
        )
        todaystudytime_seconds = data.get(
            "todaystudytime_seconds",
            todaystudytime * 60,
        )
        pointsearnedtoday = data.get("pointsearnedtoday")
        currentstreak = data.get("currentstreak")
        sessionstoday = data.get("sessionstoday")
        favoritesubject = data.get("favoritesubject")
        currentstage = data.get("currentstage")
        recentsubject = data.get("recentsubject")
        showdesktoppet = data.get("showdesktoppet")
        plantsize = data.get("plantsize", self.userdata.plantsize)
        end_session = data.get("end_session", self.userdata.end_session)
        start_session = data.get("start_session", self.userdata.start_session)
        last_session_update = data.get(
            "last_session_update",
            self.userdata.last_session_update,
        )

        if (isinstance(animation_index, bool) or not isinstance(animation_index, int)) or (
            isinstance(points, bool) or not isinstance(points, (int, float))
        ):
            raise TypeError("Flag 8")
        if not isinstance(username, str):
            raise TypeError("Flag 8")
        if not isinstance(plantsize, str):
            raise TypeError("Flag 8")
        if isinstance(end_session, bool) or not isinstance(end_session, (int, float)):
            raise TypeError("Flag 8")
        if (
            isinstance(todaystudytime, bool)
            or not isinstance(todaystudytime, (int, float))
            or isinstance(todaystudytime_seconds, bool)
            or not isinstance(todaystudytime_seconds, (int, float))
            or isinstance(start_session, bool)
            or not isinstance(start_session, (int, float))
            or isinstance(last_session_update, bool)
            or not isinstance(last_session_update, (int, float))
        ):
            raise TypeError("Flag 8")
        if not 0 <= animation_index < len(self.animation_handler.Animation_Frames) or points < 0:
            raise ValueError("Flag 8")
        if todaystudytime < 0 or todaystudytime_seconds < 0:
            raise ValueError("Flag 8")

        self.animation_handler.Animation_index = animation_index
        self.point_system.points = points
        self.userdata.username = username
        self.userdata.todaystudytime_Minutes = todaystudytime
        self.userdata.todaystudytime_seconds = todaystudytime_seconds
        self.userdata.pointsearnedtoday = pointsearnedtoday
        self.userdata.currentstreak = currentstreak
        self.userdata.sessionstoday = sessionstoday
        self.userdata.favoritesubject = favoritesubject
        self.userdata.currentstage = currentstage
        self.userdata.recentsubject = recentsubject
        self.userdata.showdesktoppet = showdesktoppet
        self.userdata.plantsize = plantsize
        self.userdata.end_session = end_session
        self.userdata.start_session = start_session
        self.userdata.last_session_update = last_session_update
        return True
