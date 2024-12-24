import ctypes
import ctypes.wintypes

class ScreenGeometry :
    def __init__(self):
        self.user32 = ctypes.windll.user32        
        self.working_area = ctypes.wintypes.RECT()
        ctypes.windll.user32.SystemParametersInfoW(48, 0, ctypes.byref(self.working_area), 0)

    def GetScreenSize(self):
        self.scr_width = self.user32.GetSystemMetrics(0)
        self.scr_height = self.user32.GetSystemMetrics(1)
        return [self.scr_width, self.scr_height]

    def GetUsableScreenSize(self):
        self.usable_width = self.working_area.right - self.working_area.left
        self.usable_height = self.working_area.bottom - self.working_area.top
        return [self.usable_width, self.usable_height]
    