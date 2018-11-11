#!/usr/bin/python3
""" Hawking Talking Demonstration. """
import sys
from sp0256al2_driver import Sp0256al2Driver

# Hello world.
S1 = [0x1B, 0x07, 0x2D, 0x35, 0x03, 0x02, 0x2E, 0x34, 0x2D, 0x15, 0x03, 0x02]

PARAGRAPH = S1

SP0256 = None

try:
    print("Start talking.")
    SP0256 = Sp0256al2Driver()
    SP0256.play_paragraph(PARAGRAPH)
except KeyboardInterrupt:
    SP0256.silence()
finally:
    print("Stop talking.")
    SP0256.cleanup()
    sys.exit(0)
