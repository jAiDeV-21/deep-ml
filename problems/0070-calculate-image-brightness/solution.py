import numpy as np

def calculate_brightness(img):
   try:
      img = np.array(img)
	  if len(img) == 0 or (img.shape[0] != img.shape[1]):
		return -1
      is_row_pixel_valid = np.apply_along_axis(
         lambda row: np.all(row >= 0) and np.all(row <= 255), 1, img
      )
      is_img_valid = np.all(is_row_pixel_valid)
      return round(np.mean(img), 2)
   except ValueError as e:
      return -1