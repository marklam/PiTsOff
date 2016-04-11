#!/usr/bin/python

import xbmcaddon
import xbmcgui
import xbmc
import sys
import subprocess

addon = xbmcaddon.Addon()
CWD = addon.getAddonInfo('path')
blankCommand   = 'sudo bash -c \'echo 1 > /sys/class/backlight/rpi_backlight/bl_power\''
unblankCommand = 'sudo bash -c \'echo 0 > /sys/class/backlight/rpi_backlight/bl_power\''

class Screensaver(xbmcgui.WindowXMLDialog):

    class ExitMonitor(xbmc.Monitor):

        def __init__(self, exit_callback):
            self.exit_callback = exit_callback

        def onScreensaverDeactivated(self):
            self.exit_callback()

    def onInit(self):
        subprocess.call(blankCommand, shell=True)
        self.exit_monitor = self.ExitMonitor(self.exit)

    def exit(self):
        self.abort_requested = True
        self.exit_monitor = None
        subprocess.call(unblankCommand, shell=True)
        self.close()

if __name__ == '__main__':
    screensaver = Screensaver('script-pitsoff-screensaver.xml', CWD, 'default')
    screensaver.doModal()
    del screensaver
    sys.modules.clear()