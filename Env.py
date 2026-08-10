from Modules.Dragger import WindowDragger
from Modules.PlantGrowth import Animation
from Modules.PointSystem import PointSystem, Sprout
from Modules.SavingSystem import SavingSystem
from Modules.Asset_Loader import Sprout_animation
from Modules.UserData import Userdata

from pathlib import Path
from pygame._sdl2 import Window
import pygame, subprocess, sys

study_ui_path = str(Path(__file__).resolve().parent / "StudyUI.py")

pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((360, 450), pygame.NOFRAME)
display.fill((255, 255, 255))

window = Window.from_display_module()
dragger = WindowDragger(window)

animation_handler = Animation()
animation_handler.create_animation(Sprout_animation, 0)
if len(Sprout) != len(Sprout_animation) - 1:
    raise ValueError("Flag 7")

point_system = PointSystem()
plant_click_count = 0

userdata = Userdata()

saving_system = SavingSystem(animation_handler, point_system, userdata)
saving_system.load()

running = True
while running:
    sprite_rect = animation_handler.return_rect()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and sprite_rect.collidepoint(event.pos):
            dragger.start_dragging()
            plant_click_count = (plant_click_count + 1) % 5
            if not plant_click_count:
                subprocess.Popen([sys.executable, study_ui_path])

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragger.stop_dragging()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            point_system.add_point(100)
            growth_index = animation_handler.return_index()
            if 0 <= growth_index < len(Sprout) and point_system.points >= Sprout[growth_index]:
                animation_handler.advance()
            saving_system.save()

    if not running:
        break
    dragger.update()
    display.fill((255, 255, 255))
    animation_handler.update_display(display)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
saving_system.save()
