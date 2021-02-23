"""
The velocity that's coming in over the messages in kind of noisy
LowPassFilter filters out all the high frequency noise in the velocity

It is basically averaging a history of values
Never got too large because it was dependent on the previous entries as wee
IT just takes the signal that is coming in and averages that with previous part
And it is waiting at according to that tau frequency parameter
"""

class LowPassFilter(object):
    def __init__(self, tau, ts):
        self.a = 1. / (tau / ts + 1.)
        self.b = tau / ts / (tau / ts + 1.);

        self.last_val = 0.
        self.ready = False

    def get(self):
        return self.last_val

    def filt(self, val):
        if self.ready:
            val = self.a * val + self.b * self.last_val
        else:
            self.ready = True

        self.last_val = val
        return val
