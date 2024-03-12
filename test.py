import cv2
import numpy as np


def pwline_rescale_intensity(image, r1, s1, r2, s2):
    if np.logical_and(r1 >= r2, s1 >= s2):
        print("the control point is invalid")
        exit()
    lut = np.zeros(256, np.uint8)
    for i in range(256):
        if i < r1:
            lut[i] = i * (s1 / r1)
        elif i <= r2:
            lut[i] = (i - r1) * (s2 - s1) / (r2 - r1) + s1
        else:
            lut[i] = (i - r2) * (255.0 - s2) / (255.0 - r2) + s2
    img_out = lut[image]
    return img_out, lut


def main():
    img = cv2.imread('./gray_cat1.png')
    r1 = 80
    s1 = 10
    r2 = 150
    s2 = 220
    img_pw, lut = pwline_rescale_intensity(img, r1, s1, r2, s2)
    cv2.imshow("cat", img_pw)
    cv2.imshow("cat1", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
