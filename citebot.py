import random
from Adafruit_Thermal import *

p = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

# p=printer.ThermalPrinter(serialport="/dev/ttyAMA0")

poemtitle = ['title1', 'title2', 'title3', 'title4']

poemtext = ['text1', 'text2', 'text3', 'text4']

poemauthor = ['author1', 'author2', 'author3', 'author4']

# this chooses a random poem number between 0 and 3
# (in the poem lists the 1st poem is poem number 0)
poem = random.randrange(0,4)

p.bold_on()
p.inverse_on()
p.print_text(poemtitle[poem])
p.linefeed()
p.inverse_off()
p.bold_off()
p.justify("L")
p.print_text(poemtext[poem])
p.linefeed()
p.justify("R")
p.print_text(poemauthor[poem])
p.justify("L")
p.linefeed()

# qr
#import Image, ImageDraw
#i = Image.open("bmw-qr.png")
#data = list(i.getdata())
#w, h = i.size
#p.print_bitmap(data, w, h, True)
#p.linefeed()

#hashtag
p.font_b_on()
p.print_text("#CiteherWork")
p.font_b_off()
p.linefeed()
p.linefeed()
p.linefeed()