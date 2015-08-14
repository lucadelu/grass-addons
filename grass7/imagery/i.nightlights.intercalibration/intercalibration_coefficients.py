# -*- coding: utf-8 -*-
"""
@author: nik | Created on Wed Feb 25 23:20:05 2015

Regression coefficients derived from models for
Inter-Satellite Calibration  of  DMSP-OLS Night-Time Light Time Series 

Elvidge 2009, 2014:  dn_adjusted = C0 + C1 × dn + C2 × dn^2
Liu 2012:  dn_calibrated = a * dn^2 + b * dn + c
Wu 2013:  dn_calibrated + 1 = a * (dn + 1)^b
"""

CITATIONS = {
    'ELVIDGE2009':
    ('Elvidge, Christopher D., Daniel Ziskin, '
     'Kimberly E. Baugh, Benjamin T. Tuttle, Tilottama Ghosh, Dee W. Pack, '
     'Edward H. Erwin, and Mikhail Zhizhin. “A Fifteen Year Record of '
     'Global Natural Gas Flaring Derived from Satellite Data.” Energies 2, '
     'no. 2 (August 7, 2009): 595–622.'),
    'ELVIDGE2014':
    ('Elvidge, Christopher D., Feng-Chi Hsu, '
     'Kimberly E. Baugh, and Tilottama Ghosh. “National Trends in '
     'Satellite-Observed Lighting.” Global Urban Monitoring and '
     'Assessment Through Earth Observation (2014): 97.'),
    'LIU2012':
    ('Liu, Zhifeng, Chunyang He, Qiaofeng Zhang, '
     'Qingxu Huang, and Yang Yang. '
     '"Extracting the Dynamics of Urban Expansion in China Using DMSP-OLS '
     'Nighttime Light Data from 1992 to 2008." '
     'Landscape and Urban Planning 106, no. 1 (May 2012): 62-72.'),
    'WU2013':
    ('Jiansheng Wu, Shengbin He, Jian Peng, Weifeng Li '
     '& Xiaohong Zhong (2013). '
     'Intercalibration of DMSP-OLS night-time light data by the invariant '
     'region method, International Journal of Remote Sensing, 34:20, '
     '7356-7368. DOI:10.1080/01431161.2013.820365')}

COEFFICIENTS = {
 'ELVIDGE2009': {'F12': {'1994': (0.1651, 1.1244, -0.0018, 0.915),
   '1995': (0.4103, 1.2116, -0.0035, 0.937),
   '1996': (0.2228, 1.27, -0.004, 0.944),
   '1997': (-0.0008, 1.1651, -0.0023, 0.945),
   '1998': (0.1535, 1.0451, -0.0009, 0.956),
   '1999': (0.0, 1.0, 0.0, 1.0)},
  'F14': {'1997': (0.0291, 1.6568, -0.0103, 0.941),
   '1998': (0.1831, 1.598, -0.0096, 0.972),
   '1999': (-0.1674, 1.5116, -0.0078, 0.971),
   '2000': (0.1061, 1.3877, -0.0059, 0.972),
   '2001': (-0.2595, 1.3467, -0.0053, 0.963),
   '2002': (0.4486, 1.1983, -0.0035, 0.927),
   '2003': (-0.2768, 1.2838, -0.0044, 0.938)},
  'F15': {'2000': (0.1029, 1.0845, -0.001, 0.97),
   '2001': (-0.4365, 1.085, -0.0009, -0.959),
   '2002': (-0.2173, 0.9715, 0.0008, 0.966),
   '2003': (-0.2244, 1.5238, -0.0079, 0.936),
   '2004': (-0.3657, 1.3772, -0.0056, 0.948),
   '2005': (-0.6201, 1.3504, -0.0049, 0.934),
   '2006': (-0.6005, 1.3551, -0.0049, 0.939),
   '2007': (-0.1615, 1.396, -0.0054, 0.947),
   '2008': (0.5031, 0.937, 0.0004, 0.92)},
  'F16': {'2004': (-0.4436, 1.2081, -0.003, 0.95),
   '2005': (-0.2375, 1.4249, -0.0063, 0.937),
   '2006': (0.0287, 1.1338, -0.0013, 0.938),
   '2007': (0.321, 0.9216, 0.0013, 0.949),
   '2008': (-0.1203, 1.0155, -0.0001, 0.946)}},
 'ELVIDGE2014': {'F10': {'1992': (-2.057, 1.5903, -0.009, 0.9075),
   '1993': (-1.0582, 1.5983, -0.0093, 0.936),
   '1994': (-0.3458, 1.4864, -0.0079, 0.9243)},
  'F12': {'1994': (-0.689, 1.177, -0.0025, 0.9071),
   '1995': (-0.0515, 1.2293, -0.0038, 0.9178),
   '1996': (-0.0959, 1.2727, -0.004, 0.9319),
   '1997': (-0.3321, 1.1782, -0.0026, 0.9245),
   '1998': (-0.0608, 1.0648, -0.0013, 0.9536),
   '1999': (0.0, 1.0, 0.0, 1.0)},
  'F14': {'1997': (-1.1323, 1.7696, -0.0122, 0.9101),
   '1998': (-0.1917, 1.6321, -0.0101, 0.9723),
   '1999': (-0.1557, 1.5055, -0.0078, 0.9717),
   '2000': (1.0988, 1.3155, -0.0053, 0.9278),
   '2001': (0.1943, 1.3219, -0.0051, 0.9448),
   '2002': (1.0517, 1.1905, -0.0036, 0.9203),
   '2003': (0.739, 1.2416, -0.004, 0.9432)},
  'F15': {'2000': (0.1254, 1.0452, -0.001, 0.932),
   '2001': (-0.7024, 1.1081, -0.0012, 0.9593),
   '2002': (0.0491, 0.9568, 0.001, 0.9658),
   '2003': (0.2217, 1.5122, -0.008, 0.9314),
   '2004': (0.5751, 1.3335, -0.0051, 0.9479),
   '2005': (0.6367, 1.2838, -0.0041, 0.9335),
   '2006': (0.8261, 1.279, -0.0041, 0.9387),
   '2007': (1.3606, 1.2974, -0.0045, 0.9013)},
  'F16': {'2004': (0.2853, 1.1955, -0.0034, 0.9039),
   '2005': (-0.0001, 1.4159, -0.0063, 0.939),
   '2006': (0.1065, 1.1371, -0.0016, 0.9199),
   '2007': (0.6394, 0.9114, 0.0014, 0.9511),
   '2008': (0.5564, 0.9931, 0.0, 0.945),
   '2009': (0.9492, 1.0683, -0.0016, 0.8918),
   '2010': (2.343, 0.5102, 0.0065, 0.8462),
   '2011': (1.8956, 0.7345, 0.003, 0.9095),
   '2012': (1.875, 0.6203, 0.0052, 0.9392)},
  'F18': {'2004': (0.2853, 1.1955, -0.0034, 0.9039),
   '2005': (-0.0001, 1.4159, -0.0063, 0.939),
   '2006': (0.1065, 1.1371, -0.0016, 0.9199),
   '2007': (0.6394, 0.9114, 0.0014, 0.9511),
   '2008': (0.5564, 0.9931, 0.0, 0.945),
   '2009': (0.9492, 1.0683, -0.0016, 0.8918),
   '2010': (2.343, 0.5102, 0.0065, 0.8462),
   '2011': (1.8956, 0.7345, 0.003, 0.9095),
   '2012': (1.875, 0.6203, 0.0052, 0.9392)}},
 'LIU2012': {'F10': {'1992': (0.0029, 0.9699, -0.4454, 0.899),
   '1993': (0.003, 1.0904, -0.5829, 0.9027),
   '1994': (0.0056, 0.9038, -0.0699, 0.885)},
  'F12': {'1994': (0.0028, 1.0569, -0.4794, 0.8984),
   '1995': (0.0088, 0.5959, 1.6317, 0.8623),
   '1996': (0.0097, 0.5674, 1.5939, 0.8319),
   '1997': (0.0092, 0.4851, 1.9491, 0.8386),
   '1998': (0.0105, 0.3659, 2.3604, 0.8429),
   '1999': (0.009, 0.5033, 2.1102, 0.9119)},
  'F14': {'1997': (0.0015, 1.0296, 0.7414, 0.8318),
   '1998': (0.0056, 0.8389, 0.7931, 0.8584),
   '1999': (0.001, 1.0659, 0.7002, 0.9186),
   '2000': (0.0057, 0.7197, 1.3015, 0.9325),
   '2001': (0.0012, 0.9877, 0.2367, 0.9576),
   '2002': (-0.003, 1.1597, 0.4874, 0.899),
   '2003': (-0.0083, 1.5049, -0.5827, 0.9629)},
  'F15': {'2000': (0.0085, 0.503, 2.1202, 0.8845),
   '2001': (0.0019, 0.9849, -0.4446, 0.9166),
   '2002': (0.0009, 0.9596, -0.5467, 0.9632),
   '2003': (-0.0125, 1.7694, -0.9178, 0.9221),
   '2004': (-0.0074, 1.4864, 0.1417, 0.9643),
   '2005': (-0.0041, 1.3075, 0.3526, 0.9212),
   '2006': (-0.0049, 1.315, 0.8122, 0.9674),
   '2007': (-0.004, 1.2713, 0.4571, 0.977),
   '2008': (0.0016, 0.8727, 0.2472, 0.9487)},
  'F16': {'2004': (-0.0005, 1.071, 0.2026, 0.9263),
   '2005': (-0.0032, 1.2913, -0.5429, 0.9649),
   '2006': (-0.0048, 1.2948, 0.0273, 0.9717),
   '2007': (0.0, 1.0, 0.0, 1.0),
   '2008': (0.0014, 0.9151, 0.7329, 0.9864)}},
 'WU2013': {'F10': {'1992': (0.8959, 1.031, 0.9492),
   '1993': (0.6821, 1.1181, 0.8731),
   '1994': (0.9127, 1.064, 0.9112)},
  'F12': {'1994': (0.4225, 1.3025, 0.8559),
   '1995': (0.3413, 1.3604, 0.9275),
   '1996': (0.9247, 1.0576, 0.9541),
   '1997': (0.3912, 1.3182, 0.9042),
   '1998': (0.9734, 1.0312, 0.9125),
   '1999': (1.2743, 0.9539, 0.8846)},
  'F14': {'1997': (1.3041, 0.9986, 0.8945),
   '1998': (0.9824, 1.107, 0.9589),
   '1999': (1.0347, 1.0904, 0.9479),
   '2000': (0.9885, 1.0702, 0.9047),
   '2001': (0.9282, 1.0928, 0.9706),
   '2002': (0.9748, 1.0857, 0.9752),
   '2003': (0.9144, 1.1062, 0.9156)},
  'F15': {'2000': (0.8028, 1.0855, 0.9242),
   '2001': (0.8678, 1.0646, 0.87),
   '2002': (0.7706, 1.092, 0.8854),
   '2003': (0.9852, 1.1141, 0.9544),
   '2004': (0.864, 1.1671, 0.9352),
   '2005': (0.5918, 1.2894, 0.9322),
   '2006': (0.9926, 1.1226, 0.9145),
   '2007': (1.1823, 1.085, 0.9041)},
  'F16': {'2004': (0.7638, 1.1507, 0.9123),
   '2005': (0.6984, 1.2292, 0.862),
   '2006': (0.9028, 1.1306, 0.9412),
   '2007': (0.8864, 1.1112, 0.9576),
   '2008': (0.9971, 1.0977, 0.9653),
   '2009': (1.4637, 0.9858, 0.8735),
   '2010': (0.8114, 1.0849, 0.9542)},
  'F18': {'2004': (0.7638, 1.1507, 0.9123),
   '2005': (0.6984, 1.2292, 0.862),
   '2006': (0.9028, 1.1306, 0.9412),
   '2007': (0.8864, 1.1112, 0.9576),
   '2008': (0.9971, 1.0977, 0.9653),
   '2009': (1.4637, 0.9858, 0.8735),
   '2010': (0.8114, 1.0849, 0.9542)}}
}

# reusable & stand-alone
if __name__ == "__main__":
    print ('Citations and coefficients for inter-satellite DMSP-OLS NightTime '
           'Lights Time Series calibration models')
    print CITATIONS
