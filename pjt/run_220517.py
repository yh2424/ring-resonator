# Linewidth 50kHz 를 위한 Q값 계산

from src import mrr_function as mrr
from src import input_parameters
import numpy as np

gamma = 0.9 # through coefficient
# alpha = 0.999855 # loss coefficient(field ratio after one round trip)
radius = 50 # in um
loss = 1.0 #dB/cm
alpha = np.exp(-loss/4.34*2*np.pi*radius*1e-6)
print ('alpha:', alpha)


input_parameters = {'radius'                :radius*1e-6,
                    'r1'                    : gamma,
                    'r2'                    : gamma,
                    'wavelength_center'     : 1550*1e-9,
                    'wavelength_span'       : 5.0*1e-9,
                    'wavelength_number_of_pts' : 1000001,
                    'non_linear'            : 0,
                    'neff'                  : 2.6,
                    'alpha'                 : alpha,
                    'cmt_or_rtt'            : 2,    # 1: CMT, 2: RTT
                    'narrow_or_broad'       : 1,    # 1: narrow-band spectrum, 2: broad-band spectrum
                    'lin_or_log'            : 1,
                    'ShowOverview': True
                    }

ring1 = mrr.simulation(input_parameters)
# print (ring1)


