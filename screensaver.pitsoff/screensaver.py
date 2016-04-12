#!/usr/bin/python

#	 PiTsOff
#    Copyright (C) 2016  Mark Lambert
#  
#    This program is free software; you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation; either version 2 of the License, or  
#    (at your option) any later version.  
#  
#    This program is distributed in the hope that it will be useful,  
#    but WITHOUT ANY WARRANTY; without even the implied warranty of  
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the  
#    GNU General Public License for more details.  
#  
#    You should have received a copy of the GNU General Public License along  
#    with this program; if not, write to the Free Software Foundation, Inc.,  
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.  
#  

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