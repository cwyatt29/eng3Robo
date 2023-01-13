# smoothing.py : platform-independent first-order smoothing filter
# No copyright, 2020-2021, Garth Zeglin.  This file is explicitly placed in the public domain.

class Smoothing:
    def __init__(self, coeff=0.1):
        """Filter to smooth an input signal using a first-order filter.  One state value
         is required.  The smaller the coefficient, the smoother the output."""
        self.coeff = coeff
        self.value = 0

    def update(self, input):
        # compute the error between the input and the accumulator        
        difference = input - self.value

        # apply a constant coefficient to move the smoothed value toward the input        
        self.value += self.coeff * difference  

        return self.value

#--------------------------------------------------------------------------------
class MovingAverage:
    def __init__(self, window_size=5):
        """Filter to smooth a signal by averaging over multiple samples.  The recent
        time history (the 'moving window') is kept in an array along with a
        running total.  The window size determines how many samples are held in
        memory and averaged together.
        """
        self.window_size = window_size
        self.ring = [0] * window_size     # ring buffer for recent time history
        self.oldest = 0                   # index of oldest sample
        self.total  = 0                   # sum of all values in the buffer

    def update(self, input):
        # subtract the oldest sample from the running total before overwriting
        self.total = self.total - self.ring[self.oldest]
  
        # save the new sample by overwriting the oldest sample
        self.ring[self.oldest] = input

        # advance to the next position, wrapping around as needed
        self.oldest += 1
        if self.oldest >= self.window_size:
            self.oldest = 0

        # add the new input value to the running total
        self.total = self.total + input

        # calculate and return the average
        return self.total / self.window_size