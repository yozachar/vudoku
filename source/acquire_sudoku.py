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


def gettingBlobs(frame):
    max_area = -1
    max_pt = ()
    width, height = rescaleFrame(frame=frame, flag=False)

    for x in range(width):
        for y in range(height):
            if frame[x][y] >= 128:
                area, frame = cv.floodFill(image=frame, mask=None, newVal=(
                    0, 0, 64), seedPoint=(y, x))[:2]
                if area > max_area:
                    max_area = area
                    max_pt = (y, x)

    frame = cv.floodFill(image=frame, mask=None,
                         newVal=(255, 255, 255), seedPoint=max_pt)[1]

    for x in range(width):
        for y in range(height):
            if frame[x][y] == 64 and x != max_pt[1] and y != max_pt[0]:
                area = cv.floodFill(image=frame, mask=None,
                                    newVal=(0, 0, 0), seedPoint=(y, x))[0]

    frame = cv. erode(src=frame, kernel=(5, 5), iterations=1)
    return frame


img = cv.imread(filename='train/sdk10.jpg')
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


# canny_sdk = cv.Canny(image=gaussian_sdk, threshold1=10,
#                      threshold2=40, apertureSize=3)
# dilated_sdk = cv.dilate(src=canny_sdk, kernel=(5, 5), iterations=1)
# eroded_sdk = cv.erode(src=dilated_sdk, kernel=(5, 5), iterations=1)

# lines = cv.HoughLines(eroded_sdk, 1, np.pi/180, 150)

# if filters:
#     rho_threshold = 15
#     theta_threshold = 0.1

#     # how many lines are similar to a given one
#     similar_lines = {i: [] for i in range(len(lines))}
#     for i in range(len(lines)):
#         for j in range(len(lines)):
#             if i == j:
#                 continue

#             rho_i, theta_i = lines[i][0]
#             rho_j, theta_j = lines[j][0]
#             if abs(rho_i - rho_j) < rho_threshold and abs(theta_i - theta_j) < theta_threshold:
#                 similar_lines[i].append(j)

#     # ordering the INDICES of the lines by how many are similar to them
#     indices = [i for i in range(len(lines))]
#     indices.sort(key=lambda x: len(similar_lines[x]))

#     # line flags is the base for the filtering
#     line_flags = len(lines)*[True]
#     for i in range(len(lines) - 1):
#         # if we already disregarded the ith element in the ordered list then we don't care (we will not delete anything based on it and we will never reconsider using this line again)
#         if not line_flags[indices[i]]:
#             continue

#         # we are only considering those elements that had less similar line
#         for j in range(i + 1, len(lines)):
#             # and only if we have not disregarded them already
#             if not line_flags[indices[j]]:
#                 continue

#             rho_i, theta_i = lines[indices[i]][0]
#             rho_j, theta_j = lines[indices[j]][0]
#             if abs(rho_i - rho_j) < rho_threshold and abs(theta_i - theta_j) < theta_threshold:
#                 # if it is similar and have not been disregarded yet then drop it now
#                 line_flags[indices[j]] = False

# print('Hough lines:', len(lines))

# filtered_lines = []

# if filters:
#     for i in range(len(lines)):  # filtering
#         if line_flags[i]:
#             filtered_lines.append(lines[i])

#     print('Filtered lines:', len(filtered_lines))
# else:
#     filtered_lines = lines

# for line in filtered_lines:
#     rho, theta = line[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))

#     cv.line(img=frame, pt1=(x1, y1), pt2=(
#         x2, y2), color=(0, 0, 255), thickness=2)
