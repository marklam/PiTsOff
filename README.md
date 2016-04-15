# PiTsOff
Kodi/OSMC screensaver for Raspberry Pi offical touchscreen.

This is a screensaver addon for kodi which can switch the official raspberry pi touchscreen backlight off/on.

It has been tested on OSMC, but it requires at least version 2016.04-1 (because that release has the backlight control overlay included).
It might work on other Kodi installs, provided the underlying operating system has the ``/sys/class/backlight/rpi_backlight/bl_power`` path available.

To install:

1. Using a web browser (on your PC or whatever), download the screensaver.pitsoff-x.x.x.zip file from the project's releases
2. Copy the zip somewhere the Pi can find it
3. From the Add-on page, choose install from zip and locate the zip file, then wait for the installed message
4. From the Appearance settings, select the newly-installed screensaver and choose a timeout

To use it:

1. Wait for the screensaver to start
2. The screen will go black
3. The backlight should swtch off

To switch the screen back on:

1. Touch the screen once
2. Wait a second for the backlight to come on
3. Continue using Kodi/OSMC

If you want a screensaver to turn an HDMI monitor off/on instead, take a look at [pimon](https://github.com/timker/kodi.screensaver.pimon) which was where I got the inspiration & starting point for this project.
