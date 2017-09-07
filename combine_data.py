"""
File: combine_data.py
Author: Uno Vaaland
Description: Combines volumetric data files from the processees into a single mesh file. 
"""


import os
import glob


def combine_data(component):

    slices = "./slices.txt"
    input_topo = "./DATABASES_MPI/"
    input_file = "./DATABASES_MPI/"
    output = "./OUTPUT_FILES/"
    print("  Combining data for component: {}".format(component))
    os.system("./bin/xcombine_vol_data_vtk {} {} {} {} {} 0".format(slices, component, input_topo, 
                                                                  input_file, output))


def create_slices_file(nslice):

    with open("slices.txt", 'w') as f:
        for i in range(nslice):
            f.write("{}\n".format(i))


def cleanup():

    os.remove("slices.txt")


if __name__ == '__main__':
  
    try:
        nslice = len(glob.glob1("DATABASES_MPI/", "*_vp.bin"))//3
    except Exception:
        nslice = 144
    components = ['vp', 'vs']

    create_slices_file(nslice)

    for component in components:
        combine_data(component)

    cleanup() 
