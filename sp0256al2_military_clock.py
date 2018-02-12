import sys

from clock import SimpleClock
from sp0256al2_driver import sp0256al2Driver
from sp0256al2 import clockAllophoneDictionary

PAUSE = [0]

def tryClockAllophone(key):
    try:
        return clockAllophoneDictionary[key], True
    except:
        return key, False


simpleClock = SimpleClock.SimpleClock()
time = simpleClock.MilitaryClock()

print("time: %s" % time)

paragraph = []

for word in time.split():
    wordAsAllophones, wordAsAllophonesFlag = tryClockAllophone(word)

    if wordAsAllophonesFlag:

        if word == '0':
            wordAsAllophones, _ = tryClockAllophone('oh')
        paragraph.extend(wordAsAllophones)
    else:
        tens, units = divmod(int(word), 10)
        wordAsAllophones, _ = tryClockAllophone(str(tens*10))
        paragraph.extend(wordAsAllophones)
        paragraph.extend(PAUSE)
	
        wordAsAllophones, _ = tryClockAllophone(str(units))
        paragraph.extend(wordAsAllophones)

    paragraph.extend(PAUSE)

try:
    print("Start talking.")
    sp0256 = sp0256al2Driver()
    sp0256.playParagraph(paragraph)
except KeyboardInterrupt:
    sp0256.cleanUp();
finally:
    print("Stop talking.")
    sys.exit(0)
