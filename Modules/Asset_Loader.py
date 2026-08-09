import pygame
from pathlib import Path

SPRITE_PATH = Path(__file__).resolve().parent / "Assets" / "Sprout.png"
if not SPRITE_PATH.is_file():
    raise FileNotFoundError(f"Sprout sprite sheet not found: {SPRITE_PATH}")

Sprout_sheet = pygame.image.load(str(SPRITE_PATH)).convert_alpha()

# Functions

def get_sprite(x, y, width, height, sprite_sheet):
    sheet_width, sheet_height = sprite_sheet.get_size()
    if x < 0 or y < 0 or width <= 0 or height <= 0:
        raise ValueError("Flag 1")
    if x + width > sheet_width or y + height > sheet_height:
        raise ValueError("Flag 2")

    sprite = pygame.Surface((width, height), pygame.SRCALPHA)
    sprite.blit(sprite_sheet, (0, 0), (x, y, width, height))
    return sprite

def scale_to_fit(sprite, max_size):
    original_width, original_height = sprite.get_size()
    scale_factor = min(max_size[0] / original_width, max_size[1] / original_height)
    new_size = (
        max(1, int(original_width * scale_factor)),
        max(1, int(original_height * scale_factor)),
    )
    return pygame.transform.scale(sprite, new_size)

# Sprite Locations

Sprout_Animation_one = get_sprite(430, 192, 254, 112, Sprout_sheet)
Sprout_Animation_two = get_sprite(429, 447, 254, 178, Sprout_sheet)
Sprout_Animation_three = get_sprite(430, 720, 254, 227, Sprout_sheet)
Sprout_Animation_four = get_sprite(387, 1036, 340, 266, Sprout_sheet)

Sprout_animation = [Sprout_Animation_one, Sprout_Animation_two, Sprout_Animation_three, Sprout_Animation_four]
