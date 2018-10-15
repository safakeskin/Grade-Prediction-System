def crop_image(image):
    x_shape, y_shape, _ = image.shape
    return image[int(x_shape * 17/40) :int(x_shape * 34.3 / 40), int(y_shape * 1/20): int(y_shape * 19/20)]

if __name__ == '__main__':
    import cv2, sys
    image_file = sys.argv[1].strip()

    image = cv2.imread(image_file)
    # cv2.imshow('uncropped',image)
    # cv2.waitKey(0)

    print("Image size is:" + str(image.shape))

    image = image[1800:3200, 250:2342]
    print("New image size is:" + str(image.shape))

    cv2.namedWindow('cropped',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('cropped',1600,900)
    cv2.imshow('cropped',image)
    cv2.waitKey(0)
