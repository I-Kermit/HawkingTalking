""" Convert SP0256-AL2 allophones to dictionary """
from sp0256al2_words import allophones

def convert_to_allophones(dictionary_of_words):
    """ convert_to_allophones(dictionary_of_words) """
    converted_words = {}

    for key, value in dictionary_of_words.items():
        connverted_list = []
        for allophone in value.split():
            try:
                connverted_list.append(allophones.VALUES[allophone])
            except:
                raise ValueError("Allophone does not exist %s " % allophone)
        converted_words[key] = connverted_list

    return converted_words
