from pytorchcvtcolor import CvtColor
from pytorchcvtcolor.image import image_to_tensor,tensor_to_image
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/Users/shashimalsenarath/Documents/check.png")
cvt = CvtColor()
tensor = image_to_tensor(img)
out = cvt(tensor/ 255.,"COLOR_RGB2YCBCR")
out = cvt(out,"COLOR_YCBCR2RGB")
image = tensor_to_image(out)
cv2.imshow("p",image)
cv2.waitKey()

