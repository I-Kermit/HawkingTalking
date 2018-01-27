class gpios(object):

    def __init__(self, noOfBits):

        self.__MIN = 0
        self.__MAX = (2**noOfBits) - 1
        self.__listBits = []
        self.__noOfBits = noOfBits

    # Convert value to bits in a list.
    def convertOutput(self,value):

        if( value < self.__MIN or value > self.__MAX):
            raise ValueError('value {0} is out of range' % value)

        # Convert to binary without 0b prefix
        fmt = '{0:0%db}' % self.__noOfBits
        binaryVal = fmt.format(value)
        # Reverse string
        binaryValReversed = binaryVal[::-1]
        # Place each bit in the list.
        self.__listBits = [int(x) for x in binaryValReversed]

    # Return decoded value.
    def getOutput(self):
        return self.__listBits
