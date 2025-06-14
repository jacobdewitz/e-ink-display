import sys, os, time, traceback
picdir = "/home/pi/Desktop/repos/e-Paper/RaspberryPi_JetsonNano/python/pic"
libdir = "/home/pi/Desktop/repos/e-Paper/RaspberryPi_JetsonNano/python/lib" # Set according to your git download
if os.path.exists(libdir): sys.path.append(libdir)
from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont, ImageEnhance