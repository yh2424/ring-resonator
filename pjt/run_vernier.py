import numpy as np
from matplotlib import pyplot as plt
from src import mrr_function as mrr


#Global
wavelength_span = 100
wavelength_number_of_pts = 100001

#Ring 1
gamma = 0.99 # through coefficient
alpha = 0.99 # loss coefficient(field ratio after one round trip)
radius = 40 # in um

input_parameters = {'radius'                :radius*1e-6,
                    'r1'                    : gamma,
                    'r2'                    : gamma,
                    'wavelength_center'     : 1550*1e-9,
                    'wavelength_span'       : wavelength_span*1e-9,
                    'wavelength_number_of_pts' : wavelength_number_of_pts,
                    'non_linear'            : 0,
                    'neff'                  : 2.6,
                    'alpha'                 : alpha,
                    'cmt_or_rtt'            : 2,           # 1: CMT, 2: RTT
                    'narrow_or_broad'       : 2,        # 1: narrow-band spectrum, 2: broad-band spectrum
                    'lin_or_log'            : 1,
                    'ShowOverview'          : False
                    }

ring1 = mrr.simulation(input_parameters)


#Ring 2
gamma = 0.9 # through coefficient
alpha = 0.99 # loss coefficient(field ratio after one round trip)
radius = 44.0 # in um

input_parameters = {'radius'                :radius*1e-6,
                    'r1'                    : gamma,
                    'r2'                    : gamma,
                    'wavelength_center'     : 1550*1e-9,
                    'wavelength_span'       : wavelength_span*1e-9,
                    'wavelength_number_of_pts' : wavelength_number_of_pts,
                    'non_linear'            : 0,
                    'neff'                  : 2.6,
                    'alpha'                 : alpha,
                    'cmt_or_rtt'            : 2,           # 1: CMT, 2: RTT
                    'narrow_or_broad'       : 2,        # 1: narrow-band spectrum, 2: broad-band spectrum
                    'lin_or_log'            : 1,
                    'ShowOverview'          : False
                    }

ring2 = mrr.simulation(input_parameters)
# print (ring2)

# plt.plot(ring1[0], 10*np.log(ring1[2]))
# plt.plot(ring1[0], 10*np.log(ring2[2]))
plt.plot(ring1[0], 10*np.log(ring1[2]*ring2[2]))
plt.ylabel("Transmission [dB]")
plt.xlabel("Wavelength [nm]")
plt.show()