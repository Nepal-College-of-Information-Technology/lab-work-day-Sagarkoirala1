## Title: fundamental of digital image and basic image operation in python
---
## Objectives:
1. Load and display  digital images

2. Understand and digital image representation
3. Color to grayscale and binary image translation
4. Image tranformation (Resize,Rotate,Flip)
5. Crop the ROI (Region of interest) in an image

---
## Background Theroy
 * ### Gigital image representation (pixel,resolution):

    A digital image is a two-dimensional representation of a real-world object, stored as a matrix of pixels.
    Each pixel contains intensity information. The resolution of an image refers to the total number of pixels arranged in rows and columns.

    *  Grayscale image : 2D matrix (height × width)

    * Color image :3D matrix (height × width × channels)
 * ### Color models (RGB,Grayscale and Binary)

   #### i. RGB Color Model

    Represents images using Red, Green, and Blue channels.Each pixel is a combination of these three colors.Commonly used in displays, cameras, and digital media.

    Example: (255, 0, 0) → pure red, (0, 255, 0) → pure green.

   #### ii. Grayscale

    Represents images in shades of gray, from black to white.

    * Each pixel has a single intensity value (0 = black, 255 = white).

    * Reduces memory usage compared to RGB.

    * Useful for image processing tasks like edge detection.

   #### iii. Binary (Black & White) Image

    Each pixel has only two possible values: 0 (black) or 1 (white). Often created from grayscale images using thresholding.


 * ### Image file formats
    #### BMP (Bitmap):
    BMP is an uncompressed format that stores images pixel by pixel, giving high quality but very large file sizes, making it less suitable for web use.

    #### JPEG (Joint Photographic Experts Group):
    JPEG uses lossy compression to reduce file size while keeping good quality, making it ideal for photographs and online images.

    #### WebP:
    WebP is a modern format by Google that supports lossy, lossless compression, and transparency, producing smaller files than JPEG, ideal for web graphics.

    #### Grayscale:
    Grayscale images store only intensity values from black to white, reducing memory usage and commonly used in image processing and medical imaging.
 * ### Basic image transformation
    Image transformation involves modifying an image’s size, orientation, or structure without changing its content. Common basic transformations include:
    Resize:
    #### Resizing:
    changes an image’s dimensions to enlarge or shrink it, useful for fitting specific sizes or reducing memory usage.

    #### Rotate:
    Rotation turns an image by a certain angle, like 90° or 180°, to correct orientation or create visual effects.

    #### Flip:
    Flipping mirrors an image horizontally or vertically, commonly used in editing and data augmentation.

    #### Crop (ROI):
    Cropping selects a portion of the image, removing unwanted areas and focusing on important regions.

    #### Translate (Shift) & Scale:
    Translation moves the image along the x or y axis, while scaling proportionally resizes it without distortion.   
 * ### Introduction to openCv:

    OpenCV (Open Source Computer Vision Library) is an open-source library used for computer vision, image processing, and machine learning tasks. It provides a wide range of functions to read, display, and manipulate images and videos, as well as to detect objects, faces, and shapes. OpenCV supports multiple programming languages, including Python, and Java, and works on different platforms like Windows, Linux, and macOS.
---
 ## Procedure
#### Step 1: Import Required Libraries
We had imported the necessary libraries, cv2 for image processing and numpy for array operations.

#### Step 2: Load and Display an Image
We had loaded the image from the file and had displayed it in a window using cv2.imshow().

#### Step 3: Convert Color Image to Grayscale
We had converted the color image to grayscale using cv2.cvtColor() and had displayed the grayscale image.

#### Step 4: Convert Grayscale Image to Binary
We had applied thresholding on the grayscale image to had obtained a binary image and had displayed it.

#### Step 5: Image Transformations
We had resized the image, had rotated it, had flipped it, and had cropped a portion for transformation demonstration.

#### Step 6: Crop ROI (Region of Interest):
we had defined a specific region of interest, had cropped that area from the original image, and had displayed the cropped ROI.

--- 
## Output
* Original image displayed successfully
* Grayscale and binary images obtained
* Image resized, rotated, and flipped correctly
* Region of interest cropped from the image
---

## Conclusion
In this lab, the fundamentals of digital image processing were explored using Python and OpenCV. Core operations such as loading images, converting color models, performing transformations, and extracting regions of interest (ROI) were successfully implemented. These basic techniques provide a foundation for more advanced image processing and computer vision tasks.



