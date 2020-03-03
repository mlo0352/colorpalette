# Directory to the image you want to process
file_dir = ""

# Number of colors to extract per image
num_colors = 8

# Each image takes a long time to process - to ensure no time is wasted, the values are saved at every step in case
# there's a failure or you add new images to process and don't want to waste time re-processing, this is the filename
dict_filename = 'dict.pickle'

# Image width in pixels
img_w = 3840

# Image height multiplier (each row representing an image will be this tall)
img_h_m = int(3840 / num_colors)

image_out = 'colors.jpg'
