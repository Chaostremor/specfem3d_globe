#!/usr/bin/python3

import os


def combine_data(component):
  print(component)

  slices = "./slices.txt"
  input_topo = "./DATABASES_MPI/"
  input_file = "./DATABASES_MPI/"
  output = "./OUTPUT_FILES/"

  os.system("./bin/xcombine_vol_data_vtk {} {} {} {} {} 0".format(slices, component, input_topo, 
                                                                  input_file, output))


def create_slices_file(nslice):
  with open("slices.txt", 'w') as f:
    for i in range(nslice):
      f.write("{}\n".format(i))


def cleanup():
  os.remove("slices.txt")


if __name__ == '__main__':
  
  # Parameters
  nslice = 64
  components = ['vp', 'vs']

  create_slices_file(nslice)

  for component in components:
    combine_data(component)

  cleanup() 
