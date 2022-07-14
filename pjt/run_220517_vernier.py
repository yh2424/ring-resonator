# Linewidth 50kHz 를 위한 Q값 계산

import numpy as np
from matplotlib import pyplot as plt
from src import mrr_function as mrr

gamma = 0.92 # through coefficient
# alpha = 0.999855 # loss coefficient(field ratio after one round trip)
radius = 50 # in um
loss = 1.0#dB/cm
alpha = np.exp(-loss/4.34*2*np.pi*radius*1e-6)
print (alpha)
wavelength_span = 150.0

input_parameters = {'radius'                :radius*1e-6,
                    'r1'                    : gamma,
                    'r2'                    : gamma,
                    'wavelength_center'     : 1550*1e-9,
                    'wavelength_span'       : wavelength_span*1e-9,
                    'wavelength_number_of_pts' : 1000001,
                    'non_linear'            : 0,
                    'neff'                  : 2.6,
                    'alpha'                 : alpha,
                    'cmt_or_rtt'            : 2,    # 1: CMT, 2: RTT
                    'narrow_or_broad'       : 2,    # 1: narrow-band spectrum, 2: broad-band spectrum
                    'lin_or_log'            : 1,
                    'ShowOverview': False
                    }

ring1 = mrr.simulation(input_parameters)
# print (ring1)



#Ring 2
gamma = gamma # through coefficient
radius = 52.5 # in um
loss = 1 #dB/cm
alpha = np.exp(-loss/4.34*2*np.pi*radius*1e-6)
print (alpha)

input_parameters = {'radius'                :radius*1e-6,
                    'r1'                    : gamma,
                    'r2'                    : gamma,
                    'wavelength_center'     : 1550*1e-9,
                    'wavelength_span'       : wavelength_span*1e-9,
                    'wavelength_number_of_pts' : 1000001,
                    'non_linear'            : 0,
                    'neff'                  : 2.6,
                    'alpha'                 : alpha,
                    'cmt_or_rtt'            : 2,    # 1: CMT, 2: RTT
                    'narrow_or_broad'       : 2,    # 1: narrow-band spectrum, 2: broad-band spectrum
                    'lin_or_log'            : 1,
                    'ShowOverview': False
                    }

ring2 = mrr.simulation(input_parameters)
# print (ring2)

plt.plot(ring1[0], 10*np.log(ring1[2]))
plt.plot(ring1[0], 10*np.log(ring2[2]))
plt.plot(ring1[0], 10*np.log(ring1[2]*ring2[2]))
plt.ylabel("Transmission [dB]")

# plt.plot(ring1[0], (ring1[2]))
# plt.plot(ring1[0], (ring2[2]))
# plt.plot(ring1[0], (ring1[2]*ring2[2]))
# plt.ylabel("Transmission [a.u.]")

plt.xlabel("Wavelength [nm]")
plt.show()