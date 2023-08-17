"""Scavenger."""

# standard
from typing import Any

# external
import cv2 as cv
from cv2.typing import MatLike
import numpy as np


class SudokuRecognizer:
    """Sudoku Recognizer."""

    def __init__(self):
        """Initialize Sudoku Recognizer."""
        pass

    def rescale_frame(self, frame: np.ndarray[Any, Any], scale: float = 1.0, flag: bool = False):
        """Rescale frame."""
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        tr_dimensions = frame.shape[:2]
        sc_dimensions = (width, height)
        return (
            cv.resize(src=frame, dsize=sc_dimensions, interpolation=cv.INTER_CUBIC)
            if flag
            else tr_dimensions
        )

    def get_distance(self, pt1: tuple[np.float32, np.float32], pt2: tuple[np.float32, np.float32]):
        """Get Distance."""
        diff_x = pt2[0] - pt1[0]
        diff_y = pt2[1] - pt2[1]
        return np.sqrt((diff_x**2) + (diff_y**2))

    def preprocess_frame(self, frame: MatLike, superimposed: np.ndarray[Any, Any]):
        """Preporcess frame."""
        # scaled_sdk = rescale_frame(frame=frame)
        gray_sdk = cv.cvtColor(src=frame, code=cv.COLOR_BGR2GRAY)
        gaussian_sdk = cv.GaussianBlur(src=gray_sdk, ksize=(3, 3), sigmaX=cv.BORDER_DEFAULT)
        adaptive_sdk = cv.adaptiveThreshold(
            src=gaussian_sdk,
            maxValue=255,
            adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,
            thresholdType=cv.THRESH_BINARY,
            blockSize=13,
            C=3,
        )
        superimposed = cv.bitwise_not(src=adaptive_sdk)
        kernel = np.ones((9, 9), np.uint8)
        dilated_sdk = cv.dilate(src=superimposed, kernel=kernel, iterations=1)
        cv.imwrite(filename="vudoku/assets/images/out/dilated.jpg", img=dilated_sdk)
        return dilated_sdk

    def perspective_transform(self, image: MatLike, corners: tuple[MatLike]):
        """Perspective Transform."""
        # Order points in clockwise order
        # Separate corners into individual points
        # Index 0 : top-right
        #       1 : top-left
        #       2 : bottom-left
        #       3 : bottom-right
        # Convert to Numpy format
        ordered_corners = np.array(
            object=[(corner[0][0], corner[0][1]) for corner in corners], dtype=np.float32
        )
        top_r, top_l, bottom_l, bottom_r = ordered_corners

        # Determine width of new image which is the max distance between
        # (bottom right and bottom left) or (top right and top left) x-coordinates
        width_a = self.get_distance(bottom_l, bottom_r)
        width_b = self.get_distance(top_l, top_r)

        # Determine height of new image which is the max distance between
        # (top right and bottom right) or (top left and bottom left) y-coordinates
        height_a = self.get_distance(top_l, bottom_l)
        height_b = self.get_distance(top_r, bottom_r)

        side = int(max(height_a, height_b, width_a, width_b))

        # Construct new points to obtain top-down view of image in
        # top_r, top_l, bottom_l, bottom_r order
        grid_dim = np.array(
            object=[(0, 0), (side - 1, 0), (side - 1, side - 1), (0, side - 1)], dtype=np.float32
        )

        # Find perspective transform matrix
        matrix = cv.getPerspectiveTransform(src=ordered_corners, dst=grid_dim)

        # Return the transformed image
        transformed = cv.warpPerspective(src=image, M=matrix, dsize=(side, side))
        flipped_h = cv.flip(src=transformed, flipCode=1)

        cv.imwrite(filename="vudoku/assets/images/out/flipped.jpg", img=flipped_h)
        return flipped_h

    def get_blobs(self, frame: MatLike, image: MatLike):
        """Get blobs."""
        contours, _ = cv.findContours(
            image=frame, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE
        )
        contours = sorted(contours, key=cv.contourArea, reverse=True)

        peri = cv.arcLength(curve=contours[0], closed=True)
        # epsilon=0.12*peri is magic ?!
        approx = (cv.approxPolyDP(curve=contours[0], epsilon=0.12 * peri, closed=True),)

        blob = cv.drawContours(
            image=image.copy(), contours=approx, contourIdx=-1, color=(0, 255, 0), thickness=10
        )
        cv.imwrite(filename="vudoku/assets/images/out/contours.jpg", img=blob)

        return frame, approx

    def relay(
        self, image: MatLike = cv.imread(filename="vudoku/assets/images/sample/sudoku10.jpg")
    ):
        """Relay."""
        # 6 does not unpack, # 2 - 5 keeps flipping
        resized_img = self.rescale_frame(frame=image, flag=False)
        blank = np.zeros(shape=resized_img, dtype=np.uint8)
        p_frame = self.preprocess_frame(frame=image, superimposed=blank)
        blob_img, apx_pts = self.get_blobs(frame=p_frame, image=image)
        return self.perspective_transform(image=blob_img, corners=apx_pts)
        # while True:
        #     isTrue, frame = capture.read()
        #     cv.imshow(winname='Webcam', mat=preprocess_frame(frame=frame))
        #     # complete, matrix = get_sudoku(frame)
        #     if cv.waitKey(1) & 0xFF == ord('q'):
        #         break
        # capture.release()
        # cv.destroyAllWindows()


srg = SudokuRecognizer()
