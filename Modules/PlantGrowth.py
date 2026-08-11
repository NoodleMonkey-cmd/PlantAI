import json
from pathlib import Path

from Modules.Asset_Loader import scale_to_fit
from Modules.UserData import Userdata

def add_animation(data):
    try:
        json.dumps(data)
    except (TypeError, ValueError) as error:
        raise TypeError("Flag 3") from error
    save_path = Path(__file__).resolve().parent / "Saved_Animation.json"
    with open(save_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

class Animation:
    def __init__(self):
        self.Animation_Frames = []
        self.Animation_index = 0

    def create_animation(self, Animation_Frames, Animation_index):
        if not Animation_Frames:
            raise ValueError("Flag 4")
        if not 0 <= Animation_index < len(Animation_Frames):
            raise ValueError("Flag 4")
        self.Animation_Frames = Animation_Frames
        self.Animation_index = Animation_index

    def _current_sprite(self):
        if not self.Animation_Frames:
            raise ValueError("Flag 5")
        if not 0 <= self.Animation_index < len(self.Animation_Frames):
            raise IndexError("Flag 5")
        return self.Animation_Frames[self.Animation_index]

    def return_rect(self, size):
        if size == "Small":
            return scale_to_fit(self._current_sprite(), (200, 200)).get_rect(center=(180, 225))
        elif size == "Medium":
            return scale_to_fit(self._current_sprite(), (250, 340)).get_rect(center=(180, 225))
        elif size == "Large":
            return scale_to_fit(self._current_sprite(), (340, 420)).get_rect(center=(180, 225))

    def update_display(self, display):
        userdata = Userdata()
        userdata.load()

        plant_size = userdata.plantsize


        if plant_size == "Small":
            display.blit(scale_to_fit(self._current_sprite(), (200, 200)), self.return_rect("Small"))
        elif plant_size == "Medium":
            display.blit(scale_to_fit(self._current_sprite(), (250, 340)), self.return_rect("Medium"))
        elif plant_size == "Large":
            display.blit(scale_to_fit(self._current_sprite(), (340, 420)), self.return_rect("Large"))

    def return_index(self):
        return self.Animation_index

    def advance(self):
        if self.Animation_index < len(self.Animation_Frames) - 1:
            self.Animation_index += 1
            return True
        return False
