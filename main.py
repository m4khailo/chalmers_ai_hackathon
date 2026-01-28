import cv2
import cv2.aruco as aruco
import numpy as np

#img = cv2.imread('t1_page-0001.jpg')
img = cv2.imread('multiple_markers.png')

if img is None:
    print("Error: Could not load image.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Image', gray)

    # Correct dictionary creation
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_100)

    # Generate marker
    marker_image = aruco.generateImageMarker(aruco_dict, 0, 200)
    cv2.imwrite("marker123.png", marker_image)

    parameters = aruco.DetectorParameters()
    detector = aruco.ArucoDetector(aruco_dict, parameters)

    marker_corners, marker_ids, rejected = detector.detectMarkers(gray)

    print(marker_corners)
    print(marker_ids)

    # Draw detected markers on the original image
    if marker_ids is not None:
        #aruco.drawDetectedMarkers(img, marker_corners, marker_ids)
        #cv2.imshow("Detected Markers", img)

        # Use the first detected marker (or loop if you want multiple)
        corners = marker_corners[0][0]  # shape (4,2)
        

        # Extract x and y coordinates
        xs = corners[:, 0]
        ys = corners[:, 1]

        min_x = int(xs.max())
        min_y = int(ys.min())
        max_y = int(ys.max())

        # Crop everything to the right of the marker
        cropped = img[min_y:max_y, min_x:img.shape[1]]
        cropped_gray = gray[min_y:max_y, min_x:img.shape[1]]

        cv2.imshow("Cropped Region", cropped)

        # Find rectangles using contour detection
        # Apply thresholding to get binary image
        _, binary = cv2.threshold(cropped_gray, 127, 255, cv2.THRESH_BINARY_INV)
        
        # Find contours
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Filter for rectangular contours
        rectangles = []
        for contour in contours:
            # Approximate the contour
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
            
            # Check if it's a rectangle (4 vertices)
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(contour)
                # Filter by size to avoid noise
                if w > 20 and h > 20:  # Adjust these thresholds as needed
                    rectangles.append({
                        'x': x,
                        'y': y,
                        'w': w,
                        'h': h,
                        'contour': contour
                    })
        
        # Sort rectangles by x-coordinate (left to right)
        rectangles = sorted(rectangles, key=lambda r: r['x'])
        
        print(f"Found {len(rectangles)} rectangles")
        
        # Analyze each rectangle to find which is filled
        filled_boxes = []
        cropped_visual = cropped.copy()
        
        for i, rect in enumerate(rectangles):
            x, y, w, h = rect['x'], rect['y'], rect['w'], rect['h']
            
            # Extract the region of interest (the box)
            box_region = cropped_gray[y:y+h, x:x+w]
            
            # Calculate mean intensity
            mean_intensity = np.mean(box_region)
            
            # Count filled pixels (dark pixels)
            filled_ratio = np.sum(box_region < 127) / (w * h)
            
            print(f"Box {i+1}: Position=({x},{y}), Mean intensity={mean_intensity:.2f}, Filled ratio={filled_ratio:.2%}")
            
            # Determine if filled (low intensity or high filled ratio)
            is_filled = filled_ratio > 0.8  # Adjust threshold as needed
            
            if is_filled:
                filled_boxes.append(i + 1)
                cv2.rectangle(cropped_visual, (x, y), (x+w, y+h), (0, 255, 0), 2) #green
            else:
                cv2.rectangle(cropped_visual, (x, y), (x+w, y+h), (0, 0, 255), 2) #red
        
        print(f"\n✓ Filled box(es): {filled_boxes}")
        cv2.imshow("Detected Boxes", cropped_visual)

    else:
        print("No markers detected.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()