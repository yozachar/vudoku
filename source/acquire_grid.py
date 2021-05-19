import cv2 as cv
import numpy as np


def rescaleFrame(frame, scale=1.0, flag=False):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    tr_dimensions = frame.shape[:2]
    sc_dimensions = (width, height)
    return cv.resize(src=frame, dsize=sc_dimensions, interpolation=cv.INTER_CUBIC) if flag else tr_dimensions


def preprocessFrame(frame, superimposed):
    # scaled_sdk = rescaleFrame(frame=frame)
    gray_sdk = cv.cvtColor(src=frame, code=cv.COLOR_BGR2GRAY)
    gaussian_sdk = cv.GaussianBlur(
        src=gray_sdk, ksize=(3, 3), sigmaX=cv.BORDER_DEFAULT)
    adaptive_sdk = cv.adaptiveThreshold(
        src=gaussian_sdk, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY, blockSize=9, C=3)
    superimposed = cv.bitwise_not(src=adaptive_sdk)
    cross = np.array([(0, 1, 0), (1, 1, 1), (0, 1, 0)], np.uint8)
    dilated_sdk = cv.dilate(src=superimposed, kernel=cross, iterations=1)
    return dilated_sdk


def getDistance(pt1, pt2):
    diff_x = pt2[0] - pt1[0]
    diff_y = pt2[1] - pt2[1]
    return np.sqrt((diff_x ** 2) + (diff_y ** 2))


def perspectiveTransform(image, corners):
    # Order points in clockwise order
    # Separate corners into individual points
    # Index 0 : top-right
    #       1 : top-left
    #       2 : bottom-left
    #       3 : bottom-right
    # Convert to Numpy format
    ordered_corners = np.array(
        object=[(corner[0][0], corner[0][1]) for corner in corners], dtype=np.float32)
    top_r, top_l, bottom_l, bottom_r = ordered_corners

    # Determine width of new image which is the max distance between
    # (bottom right and bottom left) or (top right and top left) x-coordinates
    width_A = getDistance(bottom_l, bottom_r)
    width_B = getDistance(top_l, top_r)

    # Determine height of new image which is the max distance between
    # (top right and bottom right) or (top left and bottom left) y-coordinates
    height_A = getDistance(top_l, bottom_l)
    height_B = getDistance(top_r, bottom_r)
    
    side = int(max(height_A, height_B, width_A, width_B))

    # Construct new points to obtain top-down view of image in
    # top_r, top_l, bottom_l, bottom_r order
    grid_dimn = np.array(object=[(0, 0), (side - 1, 0), (side - 1, side - 1),
                                 (0, side - 1)], dtype=np.float32)

    # Find perspective transform matrix
    matrix = cv.getPerspectiveTransform(src=ordered_corners, dst=grid_dimn)

    # Return the transformed image
    return cv.warpPerspective(src=image, M=matrix, dsize=(side, side))


def getBlobs(frame):
    contours, _ = cv.findContours(
        image=frame, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv.contourArea, reverse=True)

    curve = contours[0]
    peri = cv.arcLength(curve=curve, closed=True)
    # epsilon=0.12*peri is magic ?!
    approx = cv.approxPolyDP(curve=curve, epsilon=0.12*peri, closed=True)
    print(approx)
    drawn_cntrs = cv.drawContours(
        image=buffer_copy, contours=approx, contourIdx=-1, color=(0, 255, 0), thickness=10)
    cv.imshow(winname='contours', mat=drawn_cntrs)
    transformed = perspectiveTransform(image=frame, corners=approx)
    flipped_h = cv.flip(src=transformed, flipCode=1)

    return flipped_h


# 6 does not unpack, # 2 - 5 keeps flipping
img = cv.imread(filename='train/sdk11.jpg')  # test 10
buffer_copy = img.copy()
# creating a blank
blank = np.zeros(shape=rescaleFrame(frame=img, flag=False), dtype=np.uint8)
p_frame = preprocessFrame(frame=img, superimposed=blank)
result = getBlobs(frame=p_frame)
cv.imshow(winname='result', mat=result)
cv.imwrite(filename='result.jpg', img=result)
cv.waitKey(10**5)


# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow(winname='Webcam', mat=preprocessFrame(frame=frame))
#     # complete, matrix = get_sudoku(frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# capture.release()
# cv.destroyAllWindows()
