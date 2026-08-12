import pygame
from pathlib import Path

SPRITE_PATH = Path(__file__).resolve().parent / "Assets" / "Sprout.png"
SessionComplete = Path(__file__).resolve().parent / "Assets" / "SessionComplete.png"
if not SPRITE_PATH.is_file():
    raise FileNotFoundError(f"Sprout sprite sheet not found: {SPRITE_PATH}")

Sprout_sheet = pygame.image.load(str(SPRITE_PATH))
if pygame.display.get_surface() is not None:
    Sprout_sheet = Sprout_sheet.convert_alpha()


def remove_partial_alpha(sprite, alpha_threshold=128):
    sprite = sprite.copy()

    for x in range(sprite.get_width()):
        for y in range(sprite.get_height()):
            red, green, blue, alpha = sprite.get_at((x, y))
            if alpha < alpha_threshold:
                sprite.set_at((x, y), (red, green, blue, 0))
            else:
                sprite.set_at((x, y), (red, green, blue, 255))

    return sprite


def get_sprite(x, y, width, height, sprite_sheet):
    sheet_width, sheet_height = sprite_sheet.get_size()
    if x < 0 or y < 0 or width <= 0 or height <= 0:
        raise ValueError("Flag 1")
    if x + width > sheet_width or y + height > sheet_height:
        raise ValueError("Flag 2")
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)
    sprite.blit(sprite_sheet, (0, 0), (x, y, width, height))
    return remove_partial_alpha(sprite)


def scale_to_fit(sprite, max_size):
    original_width, original_height = sprite.get_size()
    scale_factor = min(max_size[0] / original_width, max_size[1] / original_height)
    return pygame.transform.scale(
        sprite,
        (
            max(1, int(original_width * scale_factor)),
            max(1, int(original_height * scale_factor)),
        ),
    )


SessionComplete = remove_partial_alpha(scale_to_fit(pygame.image.load(str(SessionComplete)), (200, 200)))

Sprout_Animation_one = get_sprite(363, 185, 300, 135, Sprout_sheet)
Sprout_Animation_two = get_sprite(363, 449, 299, 211, Sprout_sheet)
Sprout_Animation_three = get_sprite(362, 753, 302, 271, Sprout_sheet)
Sprout_Animation_four = get_sprite(310, 1089, 406, 316, Sprout_sheet)

Sprout_animation = [Sprout_Animation_one, Sprout_Animation_two, Sprout_Animation_three, Sprout_Animation_four]