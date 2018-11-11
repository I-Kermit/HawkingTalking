""" Driver for the SPo256-AL2 speech synthesiser chip """
import RPi.GPIO as GPIO
from gpios import Gpios


class Sp0256al2Driver(object):
    """ SP0256-AL2 driver specifically for the Raspberry Pi """
    TEN_MS_SILENCE = [0x00]

    def __init__(self):
        self.__allophone = Gpios(6)
        self.__address_pins = {'A1': 5, 'A2': 6, 'A3': 13, 'A4': 19, 'A5': 26, 'A6': 21}
        self.__ald_pin = {'ALD': 20}
        self.__lrq_pin = {'LRQ': 16}

        # Use GPIO numbers
        GPIO.setmode(GPIO.BCM)

        # Set-up pin directions.
        for pin in self.__address_pins.values():
            # print('Address pin = ',pin)
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

        GPIO.setup(self.__ald_pin.get('ALD'), GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.__lrq_pin.get('LRQ'), GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def __ald(self):
        GPIO.output(self.__ald_pin.get('ALD'), GPIO.LOW)
        GPIO.output(self.__ald_pin.get('ALD'), GPIO.HIGH)

    def __lrq(self):
        return GPIO.input(self.__lrq_pin.get('LRQ'))

    def __lrq_wait(self):
        while self.__lrq():
            pass

    def __get_channel_list(self):
        return [self.__address_pins['A1'],
                self.__address_pins['A2'],
                self.__address_pins['A3'],
                self.__address_pins['A4'],
                self.__address_pins['A5'],
                self.__address_pins['A6']]

    def play_paragraph(self, paragraph):
        """
        play_paragraph(self, paragraph)
        paragraph: Allophones to send to SP0256-AL2
        """

        for val in paragraph:
            print('.', end='', flush=True)
            self.__allophone.convert_output(val)
            GPIO.output(self.__get_channel_list(), self.__allophone.get_output())
            self.__ald()
            self.__lrq_wait()

        print('')

    def silence(self):
        """
        silence()
        Add this call in your application when keyboard interrupt is received.
        """

        self.play_paragraph(self.TEN_MS_SILENCE)
        print('\nSilence.')

    def cleanup(self):
        GPIO.cleanup()

    @classmethod
    def print_diagnostics(cls):
        """ Diagnostics for the Raspberry Pi GPIOs """
        print('Revision = ', GPIO.RPI_REVISION)
        print('GPIO S/W = ', GPIO.VERSION)
