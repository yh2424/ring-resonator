import numpy as np
from matplotlib import pyplot as plt
from src import utility as ut

c = 299792458


def simulation(input_parameters):


    # Input parameters
    radius = input_parameters['radius']
    r1 = input_parameters['r1']
    k1 = np.sqrt(1-r1**2)
    print ('k1^2 : ' +  str(k1**2))
    r2 = input_parameters['r2']
    k2 = np.sqrt(1-r2**2)
    print ('k2^2 : ' +  str(k2**2))
    wavelength_center = input_parameters['wavelength_center']



    # def qfactor(transmission, lambda_range_temp):
    #
    #     max_power = np.max(transmission)
    #     max_index = list(transmission).index(max_power)
    #     wavelength_res = lambda_range_temp[max_index]
    #
    #     delta = np.abs(transmission - max_power / 2)
    #     # plt.plot(lambda_range_temp*1e9, delta**2)
    #
    #     min_left = min(delta[:max_index])
    #     min_left_index = list(delta).index(min_left)
    #     min_right = min(delta[max_index:])
    #     min_right_index = list(delta).index(min_right)
    #
    #
    #     linewidth_wavelength = (lambda_range_temp[min_right_index] - lambda_range_temp[min_left_index])
    #
    #     print('Q-factor (wavelengt_res/FWHM):', wavelength_res / linewidth_wavelength)
    #
    #     print('linewidth [nm]:', linewidth_wavelength * 1e9)
    #     linewidth_frequency = linewidth_wavelength * c / (wavelength_center) ** 2
    #     print('linewidth [GHz]:', linewidth_frequency / 1e9)
    #
    #     return 0

    # Resonance wavelength @ Vpp / 2
    Length = 2 * np.pi * radius
    lambda_range = np.linspace(wavelength_center - input_parameters['wavelength_span']/2,
                               wavelength_center + input_parameters['wavelength_span']/2, input_parameters['wavelength_number_of_pts'])


    neff = input_parameters['neff']
    b = input_parameters['alpha']

    if input_parameters['narrow_or_broad'] == 1:
        m = round(neff * 2 * np.pi * radius / (wavelength_center))
        lambda_resonance  = neff*Length/m

        # 3 nm span around center wavelength
        lambda_range_temp = np.linspace(lambda_resonance - 1.5 * 1e-9, lambda_resonance + 1.5 * 1e-9,
                                        input_parameters['wavelength_number_of_pts'])

        w = 2 * np.pi * c/ lambda_range_temp
    elif input_parameters['narrow_or_broad'] == 2:
        lambda_range_temp = lambda_range
        w = 2 * np.pi* c/ lambda_range_temp


    if input_parameters['cmt_or_rtt'] == 1:
        print ("Coupled mode theory")

        m = round(neff * 2 * np.pi * radius / (wavelength_center))
        w0 = 2 * np.pi * c / (neff * Length / m)

        tau_l = 2 * neff * Length / ((1 - b**2) * c)
        tau_e1 = 2 * neff * Length / ((1 - r1**2) * c)

        if r2 == 1:
            tau_e = 1 / (1 / tau_e1)
            tau = 1 / (1 / tau_l + 1 / tau_e1)
            E_through   = (1j * (w-w0) + (1 / tau) - (2 / tau_e1))/ (1j * (w-w0) + (1 / tau))
            E_drop      = 0
        else:
            tau_e2 = 2 * neff * Length / ((1 - r2**2) * c)
            tau_e = 1 / (1 / tau_e1 + 1 / tau_e2)
            tau = 1 / (1 / tau_l + 1 / tau_e1 + 1 / tau_e2)
            E_through   = (1j * (w-w0) + (1 / tau) - (2 / tau_e1))/ (1j * (w-w0) + (1 / tau))
            E_drop      = (-1 * np.sqrt(2 / tau_e1 * 2 / tau_e2))/ (1j * (w-w0) + 1 / tau)

        Q = tau * w0 / 2 #CMT
        print ('Q-factor (CMT):', Q)

    elif input_parameters['cmt_or_rtt'] == 2:
        print ("Round trip theory")

        theta = 2 * np.pi * neff/ lambda_range_temp * Length
        E_through = (r1 - b * r2 * np.exp(-1j * theta))/ (1 - r1 * b * r2 * np.exp(-1j * theta))
        E_drop = -np.sqrt((1 - r1 ** 2) * (1 - r2 ** 2) * b) * np.exp(-1j * theta / 2)/ (1 - r1 * r2 * b * np.exp(-1j * theta))




    transmission_through = np.abs(E_through)**2
    transmission_drop = np.abs(E_drop)**2

    if input_parameters['ShowOverview'] == True:
        if input_parameters['lin_or_log'] == 1:
            plt.plot(lambda_range_temp*1e9, transmission_through)
            plt.plot(lambda_range_temp*1e9, transmission_drop)
            plt.ylabel("Transmission")
        elif input_parameters['lin_or_log'] == 2:
            plt.plot(lambda_range_temp * 1e9, 10*np.log(transmission_through))
            plt.plot(lambda_range_temp * 1e9, 10*np.log(transmission_drop))
            plt.ylabel("Transmission [dB]")

    ut.qfactor(transmission_drop,lambda_range_temp,c,wavelength_center)

    # if input_parameters['narrow_or_broad'] == 1:
    #     qfactor(transmission_drop, lambda_range_temp)
    #
    #
    # elif input_parameters['narrow_or_broad'] == 2:
    #     print ("Too many peaks: change option to narrow")


    plt.xlabel("Wavelength [nm]")

    if input_parameters['ShowOverview'] == True:
        plt.show()

    return lambda_range_temp*1e9, transmission_through, transmission_drop


