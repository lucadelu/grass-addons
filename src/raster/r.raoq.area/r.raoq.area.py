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

inarray = None


def forloop(arr):
    return [np.array(np.sum(np.abs(y - inarray))) for y in arr]


def main():
    global inarray
    from grass.pygrass.raster import RasterRow

    nprocs = int(options["nprocs"])
    if nprocs < 1:
        grass.fatal("nprocs value should >= 1")
    map_in = RasterRow(options["input"])
    map_in.open("r")

    iarray = np.array(map_in)
    bolnan = [iarray == -2147483648]
    # iarray[bolnan] = np.nan
    number = np.count_nonzero(iarray)
    number2 = pow(number, 2)

    if nprocs == 1:
        # vals = [np.abs(y - x) for x in inarray.flat for y in inarray.flat]
        # vals = np.array([np.abs(y - inarray.flat) for y in inarray.flat])
        out = []
        for y in iarray.flat:
            out.append(np.sum(np.abs(y - iarray.flat)))
        vals = np.array(out)
    elif nprocs > 1:
        if map_in.mtype == "CELL":
            atype = "I"
            ntype = np.uint8
        elif map_in.mtype == "FCELL":
            atype = "f"
            ntype = np.float
        else:
            atype = "d"
            ntype = np.double
        inarray = mp.Array(atype, iarray.flat)
        manager = mp.Manager()
        vals = manager.list()
        pool = mp.Pool(nprocs)
        arraysplit = np.array_split(inarray, nprocs)
        out = pool.map(forloop, arraysplit)
        pool.close()
        pool.join()
        vals = np.concatenate(out)
    out = np.sum(vals) / number2
    if flags["g"]:
        print(f"raoq={out}")
    else:
        print(f"The Rao's Q value is {out}")


if __name__ == "__main__":
    options, flags = grass.parser()
    sys.exit(main())
