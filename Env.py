from Modules.Dragger import WindowDragger
from Modules.SavingSystem import SavingSystem
from Modules.UserData import Userdata
from Modules.PlantGrowth import Animation
from Modules.PointSystem import PointSystem, Sprout, Sprout_Name
from Modules.Asset_Loader import Sprout_animation

from pathlib import Path
from pygame._sdl2 import Window
import pygame, subprocess, sys
import ctypes
import win32gui
import win32con

study_ui_path = str(Path(__file__).resolve().parent / "StudyUI.py")

pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((360, 450), pygame.NOFRAME)

TRANSPARENT_COLOR = (255, 0, 255)
display.fill(TRANSPARENT_COLOR)

last_settings_check = 0
tempcheck = True
study_ui_process = None

window = Window.from_display_module()
# TRANSPARENT COLOR

hwnd = pygame.display.get_wm_info()["window"]

GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
LMA_COLORKEY = 0x00000001

user32 = ctypes.windll.user32
style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
user32.SetWindowLongW(
    hwnd, GWL_EXSTYLE, style | WS_EX_LAYERED
)

transparent_color = 255 | (0 << 8) | (255 << 16)
user32.SetLayeredWindowAttributes(hwnd, transparent_color, 0, LMA_COLORKEY)

dragger = WindowDragger(window)

def AlwaysOnTop(state):
    order = (win32con.HWND_TOPMOST if state else win32con.HWND_NOTOPMOST)

    win32gui.SetWindowPos(
        hwnd, order, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE
    )

animation_handler = Animation()
animation_handler.create_animation(Sprout_animation, 0)
if len(Sprout) != len(Sprout_animation) - 1:
    raise ValueError("Flag 7")

point_system = PointSystem()
plant_click_count = 0

userdata = Userdata()

saving_system = SavingSystem(animation_handler, point_system, userdata)
saving_system.load()
userdata.currentstage = Sprout_Name[animation_handler.return_index()]

userdata.load()
RememberPlantPosition = userdata.rememberplantposition
if RememberPlantPosition:
    window.position = (userdata.savedposition[0], userdata.savedposition[1])

running = True
while running:
    saving_system.load_points()
    current_ticks = pygame.time.get_ticks()
    if current_ticks - last_settings_check >= 500:
        userdata.load()

    current_point = userdata.points
    AlwaysOnTopOption = userdata.alwaysontop
    ShowDesktopPlant = userdata.showdesktoppet
    plantsize = userdata.plantsize

    sprite_rect = animation_handler.return_rect(plantsize)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and sprite_rect.collidepoint(event.pos):
            dragger.start_dragging()
            plant_click_count = (plant_click_count + 1) % 5
            if not plant_click_count:
                if study_ui_process is None or study_ui_process.poll() is not None:
                    study_ui_process = subprocess.Popen([sys.executable, study_ui_path])

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragger.stop_dragging()

            x, y = window.position
            userdata.savedposition = [x, y]
            userdata.save()

    if not running:
        break
    dragger.update()


    display.fill(TRANSPARENT_COLOR)

    if ShowDesktopPlant:
        animation_handler.update_display(display)
    else:
        if study_ui_process is None or study_ui_process.poll() is not None:
            study_ui_process = subprocess.Popen([sys.executable, study_ui_path])

    growth_index = animation_handler.return_index()
    if 0 <= growth_index < len(Sprout) and point_system.points >= Sprout[growth_index]:
        if animation_handler.advance():
            userdata.currentstage = Sprout_Name[animation_handler.return_index()]
            saving_system.save()

    pygame.display.flip()

    # ALWAYS ON TOP
    # print(AlwaysOnTopOption)
    AlwaysOnTop(AlwaysOnTopOption)

    clock.tick(60)

pygame.quit()
saving_system.save()
