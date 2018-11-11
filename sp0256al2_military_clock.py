#!/usr/bin/python3

""" Hawking Talking Military clock demonstration """
import sys

from sp0256al2_clock.simple_clock import SimpleClock
from sp0256al2_driver import Sp0256al2Driver
from sp0256al2_words import CLOCK_ALLOPHONE_DICTIONARY

PAUSE = [0]


def try_clock_allophone(key):
    """Test a clock allophone word exists in the dictionary.

        Keyword arguments:
        key -- string to search

        returns -- (allophone, flag)
        """

    try:
        return CLOCK_ALLOPHONE_DICTIONARY[key], True
    except KeyError:
        return key, False


SIMPLE_CLOCK = SimpleClock()
TIME = SIMPLE_CLOCK.military_clock()

# Test only
# time = '10 0 1 hours'

print("time: %s" % TIME)

PARAGRAPH = []

for word in TIME.split():
    word_as_allophones, word_as_allophones_flag = try_clock_allophone(word)

    if word_as_allophones_flag:
        if word == '0':
            word_as_allophones, _ = try_clock_allophone('oh')
        PARAGRAPH.extend(word_as_allophones)
    else:
        tens, units = divmod(int(word), 10)
        word_as_allophones, _ = try_clock_allophone(str(tens * 10))
        PARAGRAPH.extend(word_as_allophones)
        PARAGRAPH.extend(PAUSE)

        word_as_allophones, _ = try_clock_allophone(str(units))
        PARAGRAPH.extend(word_as_allophones)

    PARAGRAPH.extend(PAUSE)

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
