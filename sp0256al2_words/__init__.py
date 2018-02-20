""" SP0256-AL2 join dictionaries """
from sp0256al2_words import miscellaneous, numbers, convert

CLOCK_DICTIONARY = {**miscellaneous.ALLOPHONE_MISC, **numbers.ALLOPHONE_NUMBERS}

# Convert allophones to bytes.
CLOCK_ALLOPHONE_DICTIONARY = convert.convert_to_allophones(CLOCK_DICTIONARY)
