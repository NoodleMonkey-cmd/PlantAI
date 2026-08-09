from Modules.Dragger import WindowDragger
from Modules.PlantGrowth import Animation
from Modules.PointSystem import PointSystem, Sprout

from pygame._sdl2 import Window
import pygame

pygame.init()
clock = pygame.time.Clock()

display = pygame.display.set_mode((360, 450), pygame.NOFRAME)
display.fill((255, 255, 255))
from Modules.Asset_Loader import Sprout_animation

window = Window.from_display_module()
dragger = WindowDragger(window)

animation_handler = Animation()
animation_handler.create_animation(Sprout_animation, 0)

if len(Sprout) != len(Sprout_animation) - 1:
    raise ValueError("Flag 7")

point_system = PointSystem()

running = True
while running:
    sprite_rect = animation_handler.return_rect()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and sprite_rect.collidepoint(event.pos):
               dragger.start_dragging()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragger.stop_dragging()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                point_system.add_point(100)

                # Point system
                growth_index = animation_handler.return_index()
                if 0 <= growth_index < len(Sprout):
                    required_points = Sprout[growth_index]
                    if point_system.points >= required_points:
                        animation_handler.advance()

    if not running:
        break

    dragger.update()

    # Clear
    display.fill((255, 255, 255))

    # Animations
    animation_handler.update_display(display)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
