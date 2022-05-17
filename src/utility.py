import numpy as np
from matplotlib import pyplot as plt

c = 299792458


def qfactor(transmission, lambda_range_temp,c, wavelength_center):
    max_power = np.max(transmission)
    max_index = list(transmission).index(max_power)
    wavelength_res = lambda_range_temp[max_index]

    delta = np.abs(transmission - max_power / 2)
    # plt.plot(lambda_range_temp*1e9, delta**2)

    min_left = min(delta[:max_index])
    min_left_index = list(delta).index(min_left)
    min_right = min(delta[max_index:])
    min_right_index = list(delta).index(min_right)

    linewidth_wavelength = (lambda_range_temp[min_right_index] - lambda_range_temp[min_left_index])

    print('Q-factor (wavelengt_res/FWHM):', wavelength_res / linewidth_wavelength)

    print('linewidth [nm]:', linewidth_wavelength * 1e9)
    linewidth_frequency = linewidth_wavelength * c / (wavelength_center) ** 2
    print('linewidth [GHz]:', linewidth_frequency / 1e9)

    return 0
