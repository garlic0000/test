import cv2 as cv


def main():
    img = cv.imread("D:\GitHubProjects\Microexpression_recognition\emojis\disgusted.png")
    print(img.shape[2])
    return 0


if __name__ == "__main__":
    main()
