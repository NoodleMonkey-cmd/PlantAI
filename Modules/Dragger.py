import ctypes
import sys
from ctypes.wintypes import POINT

class WindowDragger:
    def __init__(self, window):
        if sys.platform != "win32":
            raise OSError("WindowDragger requires Windows")
        self.window = window
        self.dragging = False
        self.offset = (0, 0)
        self.user32 = ctypes.windll.user32

    def get_global_mouse_position(self):
        point = POINT()
        if not self.user32.GetCursorPos(ctypes.byref(point)):
            raise ctypes.WinError()
        return point.x, point.y

    def start_dragging(self):
        global_mouse_x, global_mouse_y = self.get_global_mouse_position()
        window_x, window_y = self.window.position
        self.offset = (global_mouse_x - window_x, global_mouse_y - window_y)
        self.dragging = True

    def stop_dragging(self):
        self.dragging = False

    def update(self):
        if self.dragging:
            global_mouse_x, global_mouse_y = self.get_global_mouse_position()
            self.window.position = (
                global_mouse_x - self.offset[0],
                global_mouse_y - self.offset[1],
            )
