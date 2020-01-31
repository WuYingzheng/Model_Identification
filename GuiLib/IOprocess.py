
from pyFRF import FRF
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum


freq = 20480



class ResponseType(Enum):
    acceleration = 0
    velocity     = 1
    displacement = 2
    strain       = 3


class FrfImpl:
    a = 0

    def __init__(self, force, resp, t = ResponseType.acceleration):
        frf = FRF(freq, exc=force, resp=resp, exc_window='None', resp_type='a', resp_window='None')
        self.x = frf.get_f_axis()
        self.y = np.abs(frf.get_FRF(form='accelerance'))
