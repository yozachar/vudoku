import cv2 as cv
import numpy as np


def rescaleFrame(frame, scale=1.0, flag=False):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    tr_dimensions = frame.shape[:2]
    sc_dimensions = (width, height)
    return cv.resize(src=frame, dsize=sc_dimensions, interpolation=cv.INTER_CUBIC) if flag else tr_dimensions


def preprocessingFrame(frame, superimposed):
    # scaled_sdk = rescaleFrame(frame=frame)
    gray_sdk = cv.cvtColor(src=frame, code=cv.COLOR_BGR2GRAY)
    gaussian_sdk = cv.GaussianBlur(
        src=gray_sdk, ksize=(5, 5), sigmaX=cv.BORDER_DEFAULT)
    adaptive_sdk = cv.adaptiveThreshold(
        src=gaussian_sdk, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv.THRESH_BINARY, blockSize=5, C=2)
    superimposed = cv.bitwise_not(src=adaptive_sdk)
    dilated_sdk = cv.dilate(src=superimposed, kernel=(5, 5), iterations=1)
    return dilated_sdk


def perspectiveTransform(image, corners):
    # Order points in clockwise order
    # Separate corners into individual points
    # Index 0 - top-right
    #       1 - top-left
    #       2 - bottom-left
    #       3 - bottom-right
    ordered_corners = [(corner[0][0], corner[0][1]) for corner in corners]
    top_r, top_l, bottom_l, bottom_r = ordered_corners

    # Determine width of new image which is the max distance between
    # (bottom right and bottom left) or (top right and top left) x-coordinates
    width_A = np.sqrt(((bottom_r[0] - bottom_l[0])
                      ** 2) + ((bottom_r[1] - bottom_l[1]) ** 2))
    width_B = np.sqrt(((top_r[0] - top_l[0]) ** 2) +
                      ((top_r[1] - top_l[1]) ** 2))
    width = max(int(width_A), int(width_B))

    # Determine height of new image which is the max distance between
    # (top right and bottom right) or (top left and bottom left) y-coordinates
    height_A = np.sqrt(((top_r[0] - bottom_r[0]) ** 2) +
                       ((top_r[1] - bottom_r[1]) ** 2))
    height_B = np.sqrt(((top_l[0] - bottom_l[0]) ** 2) +
                       ((top_l[1] - bottom_l[1]) ** 2))
    height = max(int(height_A), int(height_B))

    # Construct new points to obtain top-down view of image in
    # top_r, top_l, bottom_l, bottom_r order
    dimensions = np.array(object=[[0, 0], [width - 1, 0], [width - 1, height - 1],
                                  [0, height - 1]], dtype="float32")

    # Convert to Numpy format
    ordered_corners = np.array(object=ordered_corners, dtype="float32")

    # Find perspective transform matrix
    matrix = cv.getPerspectiveTransform(src=ordered_corners, dst=dimensions)

    # Return the transformed image
    return cv.warpPerspective(image, matrix, (width, height))


def gettingBlobs(frame):
    contours, _ = cv.findContours(
        image=frame, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv.contourArea, reverse=True)

    curve = contours[0]
    peri = cv.arcLength(curve=curve, closed=True)
    approx = cv.approxPolyDP(curve=curve, epsilon=0.015 * peri, closed=True)
    transformed = perspectiveTransform(image=frame, corners=approx)
    #flipped_h = cv.flip(src=transformed, flipCode=1)

    return transformed


img = cv.imread(filename='train/sdk8.jpg')
# creating a blank
blank = np.zeros(shape=rescaleFrame(frame=img, flag=False), dtype='uint8')
p_frame = preprocessingFrame(frame=img, superimposed=blank)
result = gettingBlobs(frame=p_frame)
cv.imshow(winname='result', mat=result)
cv.waitKey(10**5)


# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow(winname='Webcam', mat=preprocessingFrame(frame=frame))
#     # complete, matrix = get_sudoku(frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# capture.release()
# cv.destroyAllWindows()
