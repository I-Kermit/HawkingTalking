import RPi.GPIO as GPIO
from gpios import gpios
import threading

class sp0256al2Driver(object):

    def __init__(self):
        self.__allophone = gpios(6)
        self.__addressPins = {'A1':5,'A2':6,'A3':13,'A4':19,'A5':26,'A6':21}
        self.__aldPin      = {'ALD':20}
        self.__lrqPin      = {'LRQ':16}

        # Use GPIO numbers
        GPIO.setmode(GPIO.BCM)

        # Setup pin directions.
        for pin in self.__addressPins.values():
            # print('Address pin = ',pin)
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

        GPIO.setup(self.__aldPin.get('ALD'), GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.__lrqPin.get('LRQ'), GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def __ald(self):
        GPIO.output(self.__aldPin.get('ALD'),GPIO.LOW)
        GPIO.output(self.__aldPin.get('ALD'),GPIO.HIGH)

    def __lrq(self):
        return GPIO.input(self.__lrqPin.get('LRQ'))

    def __lrqWait(self):
        while(self.__lrq()):
            pass

    def __getChannelList(self):
        return [self.__addressPins['A1'], self.__addressPins['A2'], self.__addressPins['A3'], self.__addressPins['A4'], self.__addressPins['A5'], self.__addressPins['A6']]

    def playParagraph(self, paragraph):
        lock = threading.Lock()
        # Use GPIO numbers
        GPIO.setmode(GPIO.BCM)

        for val in paragraph:
            print('.', end='', flush=True)
            with lock:
                self.__allophone.convertOutput(val)
                GPIO.output(self.__getChannelList(), self.__allophone.getOutput())
                self.__ald()
                self.__lrqWait()

        GPIO.cleanup()
        print('')

    def cleanUp(self):
        print('')
        print('Cleaning up.')
        GPIO.cleanup()
        
    def printDiagnostics(self):
        print ('Revision = ',GPIO.RPI_REVISION)
        print ('GPIO S/W = ',GPIO.VERSION)
