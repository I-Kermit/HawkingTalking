#!/usr/bin/python3

""" Hawking Talking Demonstration. """
import sys
from sp0256al2_driver import Sp0256al2Driver

# How many software engineers does it take to change a light bulb?

S1 = [0x1B, 0x20, 0x03, 0x02, 0x10, 0x07, 0x0B, 0x13, 0x03, 0x02, 0x37, 0x17, 0x28, 0x0D, 0x2E, 0x07, 0x33, 0x03, 0x02, 0x07, 0x0B, 0x0A, 0x0C, 0x0C, 0x0B, 0x13, 0x33, 0x2B, 0x03, 0x02, 0x21, 0x0F, 0x2B, 0x03, 0x02, 0x0C, 0x0D, 0x03, 0x02, 0x0D, 0x14, 0x36, 0x2A, 0x03, 0x02, 0x0D, 0x1F, 0x03, 0x02, 0x32, 0x14, 0x36, 0x0B, 0x0A, 0x03, 0x02, 0x07, 0x14, 0x36, 0x03, 0x02, 0x2D, 0x06, 0x0D, 0x03, 0x02, 0x3F, 0x1E, 0x2D, 0x1C, 0x03, 0x02, 0x04, 0x04, 0x03]


# None. It is a hardware problem!

S2 = [0x38, 0x0F, 0x0B, 0x03, 0x02, 0x04, 0x04, 0x03, 0x0C, 0x0D, 0x03, 0x02, 0x0C, 0x2B, 0x03, 0x02, 0x07, 0x14, 0x36, 0x03, 0x02, 0x1B, 0x1A, 0x33, 0x21, 0x2E, 0x07, 0x33, 0x03, 0x02, 0x09, 0x27, 0x17, 0x1C, 0x2D, 0x07, 0x10, 0x03, 0x02, 0x04, 0x04, 0x03]


# Ha, ha. Thank you, I am in all weak.

S3 = [0x1B, 0x18, 0x18, 0x03, 0x02, 0x04, 0x1B, 0x18, 0x18, 0x03, 0x02, 0x04, 0x04, 0x03, 0x1D, 0x1A, 0x2C, 0x2A, 0x03, 0x02, 0x19, 0x1F, 0x03, 0x02, 0x04, 0x17, 0x06, 0x03, 0x02, 0x1A, 0x10, 0x03, 0x02, 0x0C, 0x0C, 0x0B, 0x03, 0x02, 0x17, 0x2D, 0x03, 0x02, 0x2E, 0x13, 0x29, 0x03, 0x02, 0x04, 0x04, 0x03]

PARAGRAPH = S1 + S2 + S3

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