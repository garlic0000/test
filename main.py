import cv2


def test():
    # 文件的路径不要使用中文
    img = cv2.imread('./cat1.jpg')
    gray_img = cv2.imread('./cat1.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('cat', img)
    cv2.imshow('gray_cat', gray_img)
    cv2.imwrite('./gray_cat1.png', gray_img)
    cv2.waitKey(0)
    # waitKey控制着imshow的持续时间
    # 要是imshow之后不跟waitKey,图片会一闪而过
    cv2.destroyWindow('cat')
    cv2.destroyWindow('gray_cat')


if __name__ == "__main__":
    test()
