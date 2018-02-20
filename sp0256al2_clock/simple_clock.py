""" SP0256-AL2 speaking clock """
import time

class SimpleClock(object):
    """description of class"""

    def __init__(self):
        pass
        # print("__init__")

    @classmethod
    def __get_time(cls):
        """
        get_time()
        return (hour, minute)
        """
        localtime = time.localtime(time.time())
        # tm_hour=3, tm_min=4,
        return (localtime[3], localtime[4])

    def normal_clock(self):
        """ TODO: NOT FINISHED! """
        hour, minute = self.__get_time()

        time_in_text = ''
        hour_tens, hour_units = divmod(hour, 10)
        minute_tens, minute_units = divmod(minute, 10)

        return time_in_text

    def military_clock(self):
        """
        military_clock()
        return: string formatted in military time.
        """
        hour, minute = self.__get_time()

        time_in_text = ''
        hour_tens, hour_units = divmod(hour, 10)
        minute_tens, minute_units = divmod(minute, 10)

        if hour == 0 and minute == 0:
            time_in_text = '{0:d} 100 hours'.format(hour)
        elif hour < 10 and minute == 0:
            time_in_text = '{0:d} {1:d} 100 hours'.format(hour_tens, hour_units)
        elif hour > 10 and minute == 0:
            time_in_text = '{0:d} 100 hours'.format(hour)
        elif hour < 10 and minute < 10:
            time_in_text = '{0:d} {1:d} {2:d} {3:d} hours'.format(hour_tens, \
                                                                  hour_units, \
                                                                  minute_tens, \
                                                                  minute_units)
        elif hour < 10 and minute >= 10:
            time_in_text = '{0:d} {1:d} {2:d} hours'.format(hour_tens, hour_units, minute)
        elif hour >= 10 and minute < 10:
            time_in_text = '{0:d} {1:d} {2:d} hours'.format(hour, minute_tens, minute_units)
        else:
            time_in_text = '{0:d} {1:d} hours'.format(hour, minute)

        return time_in_text
