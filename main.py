import cv2
import cv2.aruco as aruco

img = cv2.imread('t1_page-0001.jpg')


if img is None:
    print("Error: Could not load image.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Image', gray)

    aruco_dict = aruco.Dictionary(aruco.DICT_4X4_100, 100)
    marker_image = aruco.generateImageMarker(aruco_dict, 0)
    cv2.imwrite("marker123.png", marker_image)

    parameters = aruco.DetectorParameters()

    detector = aruco.ArucoDetector(aruco_dict, parameters)

    marker_corners, marker_ids, rejected_candidates = detector.detectMarkers(gray)

    print(marker_corners)
    print(marker_ids)
    
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
