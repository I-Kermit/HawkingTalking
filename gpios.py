"""
Class Gpios creates a list representation of a binary value.
This is specifically for the Raspberry Pi function GPIO.output.
"""


class Gpios(object):
    """ The list size is determined by noOfBits. """

    def __init__(self, no_of_bits):
        self.__min = 0
        self.__max = (2 ** no_of_bits) - 1
        self.__list_bits = []
        self.__no_of_bits = no_of_bits

    def convert_output(self, value):
        """ Convert value to bits in a list. """

        if value < self.__min or value > self.__max:
            raise ValueError('value {0} is out of range' % value)

        # Convert to binary without 0b prefix
        fmt = '{0:0%db}' % self.__no_of_bits
        binary_val = fmt.format(value)
        # Reverse string
        binary_val_reversed = binary_val[::-1]
        # Place each bit in the list.
        self.__list_bits = [int(x) for x in binary_val_reversed]

    def get_output(self):
        """ Return decoded value."""

        return self.__list_bits
