import sys
import matplotlib.pyplot as plt

# below part is added for my specific problem due to using ros and anaconda
# in the same environment

try:
    sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
except ValueError as e:
    print("ROS idiot imports could not be found.")

import numpy as np, pandas as pd, cv2
import corner_index_taker, bw_converter

if __name__ == '__main__':
    img_path = sys.argv[1].strip(' /,')
    # print(img_path)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    # print(img)
    # cit = corner_index_taker.CIT()
    img = bw_converter.ColorCovert.binary_converter(img)
    
    top_down_corners    = corner_index_taker.CIT.get_begin_end( img, 255 )  # 255 for white
    left_right_corners  = corner_index_taker.CIT.get_begin_end(img.T, 255)
    print(top_down_corners + left_right_corners)

    plt.imshow(img, cmap='gray')
    plt.show()