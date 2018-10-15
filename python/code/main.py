import sys, cv2
import image_crop as cropper
import image_alignment as aligner

if __name__ == '__main__':
    # Read reference image
    refFilename = sys.argv[1]
    print("Reading reference image : ", refFilename)
    imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)

    # Read image to be aligned
    imFilename = sys.argv[2]
    print("Reading image to align : ", imFilename)
    im = cv2.imread(imFilename, cv2.IMREAD_COLOR)

    blur = cv2.GaussianBlur(im,(5,5),0)

    print("Aligning images ...")
    # Registered image will be resotred in imReg.
    # The estimated homography will be stored in h.
    imReg, h = aligner.alignImages(im, imReference)

    # Print estimated homography
    print("Estimated homography : \n",  h)  

    # Write aligned image to disk.
    outFilename = refFilename.split('/')[-1].strip('.jpg') + "_aligned.jpg"
    print("Saving aligned image : " + outFilename + " into specified folder: " + sys.argv[3])
    cv2.imwrite(sys.argv[3]+outFilename, imReg)

    print("Image is being cropped ...")
    last_image = cropper.crop_image(imReg)

    croppedFileName = refFilename.split('/')[-1].strip('.jpg') + "_aligned_and_cropped.jpg"
    print("Saving cropped image: " + croppedFileName + " into specified folder: " + sys.argv[3])
    cv2.imwrite(sys.argv[3]+croppedFileName, last_image)

    
