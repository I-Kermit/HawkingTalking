#!/usr/bin/python3

""" Hawking Talking Demonstration. """
import sys
import time
from sp0256al2_driver import Sp0256al2Driver

# Allophones
PARAGRAPH = [x for x in range(0x40)]
END = [0]

SP0256 = None

try:
    print("Start talking.")
    SP0256 = Sp0256al2Driver()

    for allophone in range(0x40):
        SP0256.play_paragraph([allophone])
    SP0256.play_paragraph(PARAGRAPH + [0])
    time.sleep(1)
    SP0256.play_paragraph(PARAGRAPH + [0])
except KeyboardInterrupt:
    SP0256.silence()
finally:
    print("Stop talking.")
    SP0256.cleanup()
    sys.exit(0)
