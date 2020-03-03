import colorgram
from settings import *
import os
import glob
from PIL import Image, ImageDraw
import datetime
import pickle


if __name__ == "__main__":
    # check if dictionary pickle exists
    fdict = {}
    try:
        with open(dict_filename, 'rb') as handle:
            fdict = pickle.load(handle)
    except FileNotFoundError:
        pass
    cwd = os.getcwd()
    file_list = glob.glob(file_dir + '\*.jpg')

    times = {}
    for file in file_list:
        if file not in fdict.keys():
            time_start = datetime.datetime.now()
            colors = colorgram.extract(file, num_colors)
            time_end = datetime.datetime.now()
            times[file] = (time_end - time_start).seconds
            fdict[file] = colors
            with open(dict_filename, 'wb') as handle:
                pickle.dump(fdict, handle, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            # The file has already been processed, skip
            pass

    im = Image.new('RGB', (img_w, len(fdict.keys()) * img_h_m), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    i_vals = zip(range(len(fdict.keys())), fdict.values())
    for i, value in i_vals:
        print(i, value)
        total_proportion = 0
        for j, color in zip(range(num_colors), value):
            draw.rectangle(
                (
                    int(total_proportion * img_w),
                    i*img_h_m,
                    int((total_proportion + color.proportion) * img_w),
                    (i+1)*img_h_m
                ),
                fill=color.rgb)
            total_proportion += color.proportion

    im.save(image_out, quality=100)
