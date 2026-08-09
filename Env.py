from Modules.Dragger import WindowDragger as D
from Modules.PlantGrowth import Animation as A
from Modules.PointSystem import PointSystem as P, Sprout as S
from Modules.SavingSystem import SavingSystem as V

from pathlib import Path as _P
from pygame._sdl2 import Window as W
import pygame, subprocess, sys

U = str(_P(__file__).resolve().parent / "StudyUI.py")
pygame.init()
ck = pygame.time.Clock()
dp = pygame.display.set_mode((360, 450), pygame.NOFRAME)
dp.fill((255, 255, 255))
from Modules.Asset_Loader import Sprout_animation as SA
wn = W.from_display_module()
dg = D(wn)
an = A()
an.set(SA, 0)
if len(S) != len(SA) - 1:
    raise ValueError("Flag 7")
ps = P()
c = 0
v = V(an, ps)
v.ld()
run = True
while run:
    r = an.rc()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
        elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and r.collidepoint(ev.pos):
            dg.grab()
            c = (c + 1) % 5
            if not c:
                subprocess.Popen([sys.executable, U])
        elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
            dg.drop()
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
            ps.ap(100)
            i = an.ix()
            if 0 <= i < len(S) and ps.pts >= S[i]:
                an.nxt()
    if not run:
        break
    dg.tick()
    dp.fill((255, 255, 255))
    an.dr(dp)
    pygame.display.flip()
    ck.tick(60)
pygame.quit()
v.sv()
