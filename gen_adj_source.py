"""
File: gen_adj_source.py
Author: Uno Vaaland
Description: A program for preparing adjoint sources from the seismograms
             produced by the forward simulation.
"""


import sys, os
from shutil import copyfile


def GenerateAdjointSource(station):

    adj_source = os.path.basename(station)[:-10] + ".adj"
    copyfile(station, "./SEM/" + adj_source)
    print("Generated adjoint source: {}".format(adj_source))


if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print("usage: python gen_adj_source.py [station_file_names]")
        sys.exit()

    stations = sys.argv[1:]
    for station in stations:
          if os.path.isfile(station):
                GenerateAdjointSource(station)
          else:
                print("File does not exist: {}".format(station))
