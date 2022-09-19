from __future__ import print_function
import numpy as np
import cv2
import numpy as np
import os

#np.seterr(divide='ignore', invalid='ignore')

def rgb2ii(img, alpha):
    """Convert RGB image to illumination invariant image."""
    ii_image = (0.5 + np.log((img[:, :, 1] / float(255))+ 1e-5) -
                alpha * np.log((img[:, :, 2] / float(255))+ 1e-5) -
                (1 - alpha) * np.log((img[:, :, 0] / float(255))+ 1e-5))


    return ii_image

if __name__ == "__main__":
    directory_name=""  
    baocun_wenjianjia="" 
    for filename in os.listdir(directory_name):
        if filename.endswith(('jpg')):
            print(' pic： '+filename)
            source_img = cv2.imread(directory_name+'/'+filename,
                            cv2.IMREAD_UNCHANGED)

            a = 0.333  # Camera alpha
            invariant_img = rgb2ii(source_img, a)
            invariant_img /= np.amax(invariant_img)

            #cv2.imshow("RGB Image", source_img)
            print(' pic： ' + filename)
            cv2.imwrite(baocun_wenjianjia+'/'+filename, invariant_img*255)



