from src import mrr_function as mrr

gamma = 0.95 # through coefficient
alpha = 0.978 # loss coefficient(field ratio after one round trip)
radius = 30 # in um


input_parameters = {'radius'                :radius*1e-6,
                    'r1'                    : gamma,
                    'r2'                    : gamma,
                    'wavelength_center'     : 1550*1e-9,
                    'wavelength_span'       : 50*1e-9,
                    'wavelength_number_of_pts' : 60001,
                    'non_linear'            : 0,
                    'neff'                  : 2.6,
                    'alpha'                 : alpha,
                    'cmt_or_rtt'            : 2,           # 1: CMT, 2: RTT
                    'narrow_or_broad'       : 2,        # 1: narrow-band spectrum, 2: broad-band spectrum
                    'lin_or_log'            : 1,
                    'ShowOverview': True

                    }

ring1 = mrr.simulation(input_parameters)
print (ring1)


