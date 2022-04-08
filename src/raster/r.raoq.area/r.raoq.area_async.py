#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:47:42 2022

@author: lucadelu
"""

############################################################################
#
# MODULE:     r.raoq.area
# AUTHOR(S):  Luca Delucchi, Michele Torresani
# PURPOSE:    It calculates the Rao's Q value for the considered area
#
# COPYRIGHT: (C) 2022 by Luca Delucchi
#
#        This program is free software under the GNU General Public
#        License (>=v2). Read the file COPYING that comes with GRASS
#        for details.
#
#############################################################################

#%module
#% description: Calculate the Rao's Q value for the considered area
#% keyword: raster
#%end
#%option
#% key: input
#% type: string
#% gisprompt: old,cell,raster
#% key_desc: name
#% description: Name of input raster map
#% required: yes
#%end
#%option
#% key: nprocs
#% type: integer
#% required: no
#% multiple: no
#% description: Number of processes which will be used for parallel calculation
#% answer: 1
#%end
#%flag
#% key: g
#% description: Print output value in shell script style
#%end

import sys
import multiprocessing as mp
import numpy as np
import grass.script as grass

array = None


def forloop(x, v):
    v.extend([np.abs(x - y) for y in array.flat])


def main():
    global array
    global vals
    from grass.pygrass.raster import RasterRow

    nprocs = int(options["nprocs"])
    if nprocs < 1:
        grass.fatal("nprocs value should >= 1")
    map_in = RasterRow(options["input"])
    map_in.open("r")
    array = np.array(map_in)
    # array[array==-2147483648] = np.NaN
    number = np.count_nonzero(array)
    number2 = pow(number, 2)
    if nprocs == 1:
        vals = [np.abs(x - y) for x in array.flat for y in array.flat]
    elif nprocs > 1:
        manager = mp.Manager()
        vals = manager.list()
        pool = mp.Pool(nprocs)
        listarray = list(array.flat)
        for l in listarray:
            pool.apply_async(forloop, args=[l, vals])
        pool.close()
        # pool.join()
    out = sum(vals) / number2
    if flags["g"]:
        print(f"raoq={out}")
    else:
        print(f"The Rao's Q value is {out}")


if __name__ == "__main__":
    options, flags = grass.parser()
    sys.exit(main())
