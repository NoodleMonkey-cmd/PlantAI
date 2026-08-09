import json
import os

def add_animation(data):
    try:
        json.dumps(data)
    except (TypeError, ValueError) as error:
        raise TypeError("Flag 3") from error

    save_path = os.path.join(os.path.dirname(__file__), "Saved_Animation.json")
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

    def return_rect(self):
        current_sprite = self._current_sprite()
        return current_sprite.get_rect(center=(180, 225))

    def update_display(self, display):
        current_sprite = self._current_sprite()
        rect = self.return_rect()

        display.blit(current_sprite, rect)

    def return_index(self):
        return self.Animation_index

    def advance(self):
        if self.Animation_index < len(self.Animation_Frames) - 1:
            self.Animation_index += 1
            return True
        return False
