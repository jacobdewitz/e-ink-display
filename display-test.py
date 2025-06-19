import sys, os, time, traceback
picdir = "/home/karisnemik/repos/e-Paper/RaspberryPi_JetsonNano/python/pic"
libdir = "/home/karisnemik/repos/e-Paper/RaspberryPi_JetsonNano/python/lib" # Set according to your git download
if os.path.exists(libdir): sys.path.append(libdir)
from waveshare_epd import epd7in5_V2
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

epd = epd7in5_V2.EPD()
epd.init()
epd.Clear()

font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
font36 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 36)

Himage = Image.open(os.path.join(picdir, '7in5_V2.bmp'))
Himage = Image.new('1', (epd.width, epd.height), 100)
draw = ImageDraw.Draw(Himage)

# make the dashboard sections
draw.text((20, 20), "Jake's Dashboard", font=font24, fill=0)
# top left
draw.rectangle((0, 0, 350, 200), outline=0, width=4)
# top right
draw.rectangle((346, 0, 795, 200), outline=0, width=4)
# bottom middle
draw.rectangle((225, 198, 650, 475), outline=0, width=4)

# draw.arc((140, 50, 190, 100), 0, 360, fill=0)

epd.init_part()

# draw border around the whole frame
draw.rectangle((0, 0, 795, 475), outline=0, width=3)


while (True):
    draw.rectangle((30, 90, 160, 180), fill=255)
    draw.text((20, 100), time.strftime('%I:%M'), font=font36, fill=0)
    epd.display_Partial(epd.getbuffer(Himage), 0, 0, epd.width, epd.height)
    time.sleep(60)