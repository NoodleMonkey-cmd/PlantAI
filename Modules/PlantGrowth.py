import json
from pathlib import Path

import pygame.time

from Modules.Asset_Loader import scale_to_fit
from Modules.UserData import Userdata

import math

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
        self.bouncing = False
        self.bounce_start = 0
        self.bounce_duration = 400

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
        time = pygame.time.get_ticks() / 1000
        bob = math.sin(time * 3) * 3
        breath = 1 + math.sin(time * 3) * 0.05

        max_size = (250, 340)
        if plant_size == "Small":
            max_size = (200, 200)
        elif plant_size == "Medium":
            max_size = (250, 340)
        elif plant_size == "Large":
            max_size = (340, 420)

        curr_sprite = scale_to_fit(self._current_sprite(), max_size)
        width = curr_sprite.get_width()
        height = int(curr_sprite.get_height() * breath)

        bounce_y = self.get_bounce_offset()

        animated_sprite = pygame.transform.scale(curr_sprite, (width, height))
        rect = animated_sprite.get_rect(center=(180, 225+bob+bounce_y))

        display.blit(animated_sprite, rect)


    def return_index(self):
        return self.Animation_index

    def start_bounce(self):
        self.bouncing = True
        self.bounce_start = pygame.time.get_ticks()

    def get_bounce_offset(self):
        if not self.bouncing:
            return 0

        elapsed = pygame.time.get_ticks() - self.bounce_start

        if elapsed >= self.bounce_duration:
            self.bouncing = False
            return 0

        progress = elapsed / self.bounce_duration
        return -math.sin(progress * math.pi) * 20

    def advance(self):
        if self.Animation_index < len(self.Animation_Frames) - 1:
            self.Animation_index += 1
            return True
        return False
