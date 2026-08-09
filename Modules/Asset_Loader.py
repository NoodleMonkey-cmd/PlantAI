import pygame
from pathlib import Path as _P

SP = _P(__file__).resolve().parent / "Assets" / "Sprout.png"
if not SP.is_file():
    raise FileNotFoundError(f"Sprout sprite sheet not found: {SP}")

S = pygame.image.load(str(SP)).convert_alpha()


def g(x, y, w, h, sheet):
    sw, sh = sheet.get_size()
    if x < 0 or y < 0 or w <= 0 or h <= 0:
        raise ValueError("Flag 1")
    if x + w > sw or y + h > sh:
        raise ValueError("Flag 2")
    s = pygame.Surface((w, h), pygame.SRCALPHA)
    s.blit(sheet, (0, 0), (x, y, w, h))
    return s


def sc(sprite, mx):
    ow, oh = sprite.get_size()
    f = min(mx[0] / ow, mx[1] / oh)
    return pygame.transform.scale(sprite, (max(1, int(ow * f)), max(1, int(oh * f))))


Sprout_Animation_one = g(430, 192, 254, 112, S)
Sprout_Animation_two = g(429, 447, 254, 178, S)
Sprout_Animation_three = g(430, 720, 254, 227, S)
Sprout_Animation_four = g(387, 1036, 340, 266, S)

Sprout_animation = [Sprout_Animation_one, Sprout_Animation_two, Sprout_Animation_three, Sprout_Animation_four]
