import numpy as np

class Sample(object):
    signum = 0
    samplecnt = 0
    time = None
    sample = None

    def __init__(self, file=None, signum=1, samplecnt=0, sample=None):
        if file:
            fd = open(file, 'r')
            self.samplecnt = sum(1 for line in fd)
            fd.seek(0, 0)
            self.signum = len(fd.readline().split()) - 1
            self.time = np.zeros(self.samplecnt, dtype = float)
            self.sample = np.zeros((self.signum, self.samplecnt), dtype = float)
            fd.seek(0, 0)
            for idx, line in enumerate(fd):
                iterns = line.split()
                self.time[idx] = iterns[0]
                for sig in range(0, self.signum):
                    self.sample[sig][idx] = iterns[sig+1]
        else:
            self.signum = signum
            self.samplecnt = samplecnt
            self.time = np.zeros(samplecnt, dtype=float)
            self.sample = sample.copy()
