import colorgram
from settings import *
import os
import glob
import PIL
import datetime
import pickle

dict_filename = 'dict.pickle'

if __name__ == "__main__":
    # check if dictionary exists
    dict = {}
    try:
        with open(dict_filename, 'rb') as handle:
            dict = pickle.load(handle)
    except FileNotFoundError:
        pass
    cwd = os.getcwd()
    file_list = glob.glob(file_dir + '\*.jpg')

    times = {}
    for file in file_list:
        if file not in dict.keys():
            time_start = datetime.datetime.now()
            colors = colorgram.extract(file, num_colors)
            time_end = datetime.datetime.now()
            times[file] = (time_end - time_start).seconds
            dict[file] = colors
            with open(dict_filename, 'wb') as handle:
                pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            # The file has already been processed, skip
            pass
    print(dict)


    # i = 0
    # for color in colors:
    #     i += color.proportion * 1024

    # colors =